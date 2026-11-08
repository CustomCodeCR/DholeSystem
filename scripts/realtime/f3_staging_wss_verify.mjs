import { writeFile, mkdir } from 'node:fs/promises'
import { pathToFileURL } from 'node:url'

const RS = '\u001e'
const GUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i

export function validateTarget(host, kind, resource, path) {
  const base = new URL(host)
  if (base.protocol !== 'https:' || base.port || base.username || base.password ||
      base.pathname !== '/' || base.search || base.hash ||
      !/(^|[.-])(staging|stage|stg)([.-]|$)/i.test(base.hostname))
    throw Error('Refusing non-staging HTTPS target')
  if (!/^[a-z][a-z0-9-]+\.[a-z][a-z0-9-]+$/.test(kind) || !GUID.test(resource) ||
      /^0{8}-0{4}-0{4}-0{4}-0{12}$/i.test(resource) ||
      !path.startsWith('/') || path.startsWith('//') || path.includes('..') ||
      path.includes('?') || path.includes('#') || path.includes('://'))
    throw Error('Invalid resource or owner REST GET path')
  return base
}

async function request(url, token, method = 'GET') {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), 8000)
  try {
    return await fetch(url, { method, signal: controller.signal,
      headers: { Authorization: 'Bearer ' + token, 'Cache-Control': 'no-store' } })
  } finally { clearTimeout(timer) }
}

async function subscribe(base, token, kind, resource) {
  const negotiate = await request(new URL('/hubs/realtime/negotiate?negotiateVersion=1', base),
    token, 'POST')
  if (negotiate.status !== 200) throw Error('Hub negotiate not HTTP 200')
  const connection = await negotiate.json()
  const id = connection.connectionToken ?? connection.connectionId
  if (typeof id !== 'string' || !id || id.length > 200) throw Error('Invalid connection ID')
  const issued = await request(new URL('/hubs/realtime/ticket', base), token, 'POST')
  if (issued.status !== 200) throw Error('WSS ticket not HTTP 200')
  const { ticket } = await issued.json()
  if (typeof ticket !== 'string' || !/^[A-Za-z0-9_-]{43}$/.test(ticket))
    throw Error('Invalid WSS ticket')
  const url = new URL('/hubs/realtime', base)
  url.protocol = 'wss:'
  url.searchParams.set('id', id)
  url.searchParams.set('ticket', ticket)
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(url)
    let complete = false, handshake = false
    const timer = setTimeout(() => finish(new Error('WSS timed out')), 12000)
    function finish(err, allow) {
      if (complete) return
      complete = true
      clearTimeout(timer)
      ws.close()
      if (err) reject(err)
      else resolve(allow)
    }
    ws.addEventListener('open', () => ws.send('{"protocol":"json","version":1}' + RS))
    ws.addEventListener('error', () => finish(new Error('WSS TLS/upgrade failed')))
    ws.addEventListener('close', () => finish(new Error('WSS closed early')))
    ws.addEventListener('message', event => {
      try {
        const frames = String(event.data).split(RS).filter(Boolean)
        for (const frame of frames) {
          if (frame.length > 8192) throw Error('Oversize signal frame')
          const msg = JSON.parse(frame)
          if (!handshake) {
            if (msg.error) return finish(new Error('SignalR handshake denied'))
            handshake = true
            ws.send(JSON.stringify({ type: 1, invocationId: '1', target: 'Subscribe',
              arguments: [kind, resource] }) + RS)
          } else if (msg.type === 3 && msg.invocationId === '1') {
            return finish(null, !msg.error)
          }
        }
      } catch { finish(new Error('Invalid SignalR protocol frame')) }
    })
  })
}

export async function verify() {
  const env = process.env
  const vars = ['DHOLE_RT_STAGING_ORIGIN', 'DHOLE_RT_RESOURCE_KIND',
    'DHOLE_RT_RESOURCE_ID', 'DHOLE_RT_OWNER_GET_PATH',
    'DHOLE_RT_ALLOWED_JWT', 'DHOLE_RT_DENIED_JWT']
  if (vars.some(k => !env[k]?.trim()) || env.DHOLE_RT_ALLOWED_JWT === env.DHOLE_RT_DENIED_JWT)
    throw Error('Missing staging QA configuration or distinct accounts')
  const base = validateTarget(env.DHOLE_RT_STAGING_ORIGIN, env.DHOLE_RT_RESOURCE_KIND,
    env.DHOLE_RT_RESOURCE_ID, env.DHOLE_RT_OWNER_GET_PATH)
  const get = new URL(env.DHOLE_RT_OWNER_GET_PATH, base)
  const [allowed, denied] = await Promise.all([
    request(get, env.DHOLE_RT_ALLOWED_JWT), request(get, env.DHOLE_RT_DENIED_JWT) ])
  if (allowed.status !== 200 || ![403,404].includes(denied.status))
    throw Error('Owner REST isolation not established')
  const [allowSub, denySub] = await Promise.all([
    subscribe(base, env.DHOLE_RT_ALLOWED_JWT, env.DHOLE_RT_RESOURCE_KIND, env.DHOLE_RT_RESOURCE_ID),
    subscribe(base, env.DHOLE_RT_DENIED_JWT, env.DHOLE_RT_RESOURCE_KIND, env.DHOLE_RT_RESOURCE_ID) ])
  if (!allowSub || denySub) throw Error('SignalR resource ACL isolation failed')
  await mkdir('F3Results', { recursive: true })
  await writeFile('F3Results/staging-wss-evidence.json',
    JSON.stringify({ releaseId: 'rt-20261107-01', environment: 'staging',
      allowedOwnerGetStatus: 200, deniedOwnerGetStatus: denied.status,
      authorizedSignalRSubscribe: true, unauthorizedSignalRSubscribeRejected: true,
      wssTlsReal: true, twoRealQaUsers: true, noBusinessWrites: true,
      formalF3Approved: false, formalF7Approved: false, observedAtUtc: new Date().toISOString() }, null, 2) + '\n')
  console.log('STAGING_WSS_JWT_ACL_CANDIDATE_PASS: two QA identities and TLS/WSS; formal gates still need review')
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href)
  verify().catch(() => {
    console.error('STAGING_WSS_JWT_ACL_BLOCKED; no tokens or event payloads logged')
    process.exitCode = 1
  })
