# lef-web — lef.fyi

Static personal website built with hand-coded HTML and Tufte CSS. Hosted on AWS S3 with Cloudflare CDN.

**Repo**: `git@github.com:Lef-F/lef-web.git`
**Live**: https://lef.fyi

## Architecture

```
src/            → Deployable website (HTML, CSS, fonts, media)
tools/          → Python utilities (sitemap generator)
.github/        → CI/CD (GitHub Actions → S3 + Cloudflare)
.claude/        → Claude context, skills, settings
```

All pages are hand-written HTML — no static site generator, no templating engine, no JavaScript.

## Development Commands

```shell
npm run start       # Local server at http://127.0.0.1:8080
npm run cssmin      # Minify tufte.css → tufte.min.css (MUST run after CSS changes)
```

Sitemap generation (requires uv in `tools/`):
```shell
cd tools && uv run python src/sitemap_generator.py https://lef.fyi ../src --except "et-book"
```

## Conventions

### File Naming
- Blog posts: `src/pages/posts/YYYYMMDD-slug.html`
- Post media: `src/media/YYYYMMDD-slug/` (matching the post date+slug)
- Shared media: `src/media/00-common/`

### HTML Patterns
Every page follows this structure:
- `<head>` with viewport meta, charset, title (`Page Title | Lef adores you ❤️`), favicon, tufte.min.css
- Banner: clickable full-width image linking to `/` + invisible duplicate for spacing
- Blog posts: content in `<article>` > `<section>` elements
- Homepage: uses `<section>` elements directly (no `<article>` wrapper)
- `<footer>` with "Return home" link

Sidenotes use the Tufte CSS checkbox toggle pattern (no JS). Each needs a unique `id`/`for` pair.
See `.claude/context/tufte-patterns.md` for all HTML patterns (sidenotes, images, blockquotes, links, etc).

### Content Style
- Warm, personal tone with emoji
- Tufte philosophy: prefer sidenotes over footnotes, value clean typography

### CSS
- Edit `src/tufte.css` for styling changes
- **Always** run `npm run cssmin` after editing — both files must be committed together
- Pages reference `tufte.min.css`, not the source file
- Key colors: background `#f9fefc`, text `#443b36`, accent red `#dc5945`
- ET Book font family with Palatino/Georgia fallbacks

## Deployment

Automated via GitHub Actions (`.github/workflows/cicd.yml`). Two triggers, two jobs:

- **Push to `main`** → `deploy` job syncs to production S3 bucket (lef.fyi) and purges cache.
- **PR `opened` / `synchronize` / `reopened`** → `deploy` job creates or updates a preview at `{branch}.lef.fyi`.
- **PR `closed`** (merged or not) → `cleanup` job empties/removes the preview bucket and deletes its Cloudflare CNAME.

Pushes to non-`main` branches without an open PR do not deploy anything on their own. Open a PR to get a preview.

Pipeline (deploy job): checkout with LFS → configure bucket + policy → S3 sync → Cloudflare CNAME upsert → cache purge.

### Branch naming constraints

Branch names become S3 bucket prefixes and Cloudflare subdomain labels, so they must be:
- **lowercase** — S3 bucket names reject mixed case
- **no slashes** — `feature/foo` breaks bucket naming; use `feature-foo` instead
- **no underscores, no leading/trailing hyphens** — DNS label rules
- **short enough** — bucket is `{branch}.{base}`, must fit in 63 chars total

Stick to flat kebab-case (`post-quiet-world`, `ci-pr-previews`) and you never think about it.

## Git

- Images (png, jpg, jpeg) tracked with Git LFS
- Conventional commit messages, lowercase, imperative
- No co-author lines in commits
