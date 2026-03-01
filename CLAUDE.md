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
- Content in `<article>` > `<section>` elements
- `<footer>` with "Return home" link

Sidenotes use the Tufte CSS checkbox toggle pattern (no JS):
```html
<label class="sidenote-number"></label>
<label for="unique-id" class="margin-toggle">⊕</label>
<input type="checkbox" id="unique-id" class="margin-toggle">
<span class="marginnote sidenote"><em>Note content</em></span>
```

Each sidenote needs a unique `id`/`for` pair. See `.claude/context/tufte-patterns.md` for full reference.

### Content Style
- Warm, personal tone with emoji
- Tufte philosophy: prefer sidenotes over footnotes, value clean typography
- Images can go inline or in sidenotes via `<img>` inside the `<span class="marginnote sidenote">`

### CSS
- Edit `src/tufte.css` for styling changes
- **Always** run `npm run cssmin` after editing — both files must be committed together
- Pages reference `tufte.min.css`, not the source file
- Key colors: background `#f9fefc`, text `#443b36`, accent red `#dc5945`
- ET Book font family with Palatino/Georgia fallbacks

## Deployment

Automated via GitHub Actions (`.github/workflows/cicd.yml`):
- **Trigger**: Push to `src/` or `.github/workflows/`
- **main branch** → production S3 bucket (lef.fyi)
- **Other branches** → `{branch}.lef.fyi` subdomain (auto-created)
- Pipeline: checkout with LFS → S3 sync → configure static hosting → Cloudflare DNS + cache purge

## Git

- Images (png, jpg, jpeg) tracked with Git LFS
- Conventional commit messages, lowercase, imperative
- No co-author lines in commits
