# Dhole deployment environments

The server keeps the private base file at `/opt/dhole/.env`. It is never committed to GitHub.

`deploy/prepare-environments.sh` creates two runtime files while preserving the server-only passwords, JWT secret, SMTP credentials and internal keys.

## Production (`master`)

- ASPNETCORE_ENVIRONMENT=Production
- DOTNET_ENVIRONMENT=Production
- DHOLE_WEB_HOST=sistema.logisticacastrofallas.com
- DHOLE_API_HOST=api.logisticacastrofallas.com
- DHOLE_WEB_PUBLIC_URL=https://sistema.logisticacastrofallas.com
- DHOLE_API_PUBLIC_URL=https://api.logisticacastrofallas.com
- VITE_API_URL=https://api.logisticacastrofallas.com
- VITE_FRONTEND_DOMAIN=https://sistema.logisticacastrofallas.com
- CORS_WEB_ORIGIN=https://sistema.logisticacastrofallas.com
- Runtime env: `/opt/dhole/.env.production`
- Docker project: `dhole`
- Docker network: `dhole`
- Image tag: `latest`

## Staging (`develop`)

- ASPNETCORE_ENVIRONMENT=Staging
- DOTNET_ENVIRONMENT=Staging
- DHOLE_WEB_HOST=dhole.customcodecr.com
- DHOLE_API_HOST=dhole-api.customcodecr.com
- DHOLE_WEB_PUBLIC_URL=https://dhole.customcodecr.com
- DHOLE_API_PUBLIC_URL=https://dhole-api.customcodecr.com
- VITE_API_URL=https://dhole-api.customcodecr.com
- VITE_FRONTEND_DOMAIN=https://dhole.customcodecr.com
- CORS_WEB_ORIGIN=https://dhole.customcodecr.com
- DATA_EXTRACTION_EMAIL_ENABLED=false
- NOTIFICATIONS_EMAIL_ENABLED=false
- Runtime env: `/opt/dhole/.env.staging`
- Docker project: `dhole-staging`
- Docker network: `dhole-staging`
- Image tag: `staging`

Staging has its own PostgreSQL, MongoDB, Redis and MinIO volumes. This prevents development deployments from using production data. Ollama is shared read-only at the infrastructure level by attaching the existing Ollama container to the staging network.

Cloudflare/Tunnel hostnames must point the production domains to the production API Gateway/Web origins and the CustomCodeCR domains to the staging API Gateway/Web origins. DNS/Tunnel configuration is intentionally not stored with application secrets.
