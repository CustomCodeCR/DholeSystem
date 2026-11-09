import assert from 'node:assert/strict'
import { test } from 'node:test'
import { validateTarget } from './f3_staging_wss_verify.mjs'
const ID = 'aaaaaaaa-1111-4111-8111-111111111111'
test('valid HTTPS staging origin and owner resource GET', () => {
  assert.equal(validateTarget('https://staging.example.com/', 'crm.account',
    ID, '/api/crm/accounts/' + ID).hostname, 'staging.example.com')
})
test('reject production and unencrypted targets', () => {
  for (const url of ['https://sistema.example.com/', 'http://staging.example.com/',
    'https://staging.example.com:8443/', 'https://u:p@staging.example.com/',
    'https://staging.example.com/?token=secret'])
    assert.throws(() => validateTarget(url, 'crm.account', ID, '/api/crm/accounts/' + ID))
})
test('reject unsafe REST paths and invalid identifiers', () => {
  for (const path of ['//evil', '/../../secret', '/api?id=abc', 'https://prod.test/'])
    assert.throws(() => validateTarget('https://staging.example.com/', 'crm.account', ID, path))
  assert.throws(() => validateTarget('https://staging.example.com/', 'crm.account',
    '00000000-0000-0000-0000-000000000000', '/api/crm/accounts'))
})
