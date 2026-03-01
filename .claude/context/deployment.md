# Deployment

## Pipeline

GitHub Actions workflow: `.github/workflows/cicd.yml`

**Trigger**: Push to `src/**` or `.github/workflows/**`

**Steps**:
1. Checkout repo (with Git LFS)
2. Detect branch name
3. Configure AWS credentials
4. Create/select S3 bucket (main → production bucket, branches → `{branch}.{bucket}`)
5. Sync `src/` directory to S3 with public-read ACL
6. Configure S3 static website hosting (index: `index.html`, error: `404.html`)
7. Apply bucket policy from `.github/workflows/policy.json`
8. For non-main branches: create Cloudflare CNAME record for subdomain
9. Purge Cloudflare cache

## Branch Strategy

| Branch | URL | Auto-created |
|--------|-----|-------------|
| `main` | https://lef.fyi | No (production) |
| `feature-x` | https://feature-x.lef.fyi | Yes (DNS + S3 bucket) |

## Secrets (referenced in CI, never stored in repo)

- `AWS_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` — S3 access
- `AWS_S3_BUCKET` — production bucket name
- `CLOUDFLARE_ZONE_ID`, `CLOUDFLARE_DNS_SECRET_API_TOKEN` — DNS + cache management
- `EMAIL` — Cloudflare auth email
