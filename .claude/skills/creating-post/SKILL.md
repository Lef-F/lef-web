---
name: creating-post
description: Create a new blog post with the standard Tufte CSS template and update all references.
---

# Creating a Blog Post

## When to Use
When creating a new page or blog post for lef.fyi.

## Steps

1. **Create the HTML file**
   - Path: `src/pages/posts/YYYYMMDD-slug.html`
   - Use today's date (YYYYMMDD format) and a URL-friendly slug
   - Start from the page template in `.claude/context/tufte-patterns.md`

2. **Create media directory** (if the post has images)
   - Path: `src/media/YYYYMMDD-slug/`
   - Name must match the post filename (without `.html`)

3. **Write the content**
   - Use `<article>` > `<section>` structure
   - Add sidenotes for supplementary information (see tufte-patterns.md)
   - Each sidenote `id` must be unique within the page
   - Use external link pattern (`target="_blank" rel="noopener noreferrer"`) for off-site links

4. **Add to homepage**
   - Edit `src/index.html`
   - Add a link to the new post in the appropriate section

5. **Update sitemap**
   - Run: `cd tools && uv run python src/sitemap_generator.py https://lef.fyi ../src --except "et-book"`
   - Or manually add the URL to `src/sitemap.txt`

6. **Preview locally**
   - Run: `npm run start`
   - Check at http://127.0.0.1:8080/pages/posts/YYYYMMDD-slug.html
   - Verify sidenotes toggle correctly on narrow viewport

## Verification
- Page loads without errors
- Banner image displays and links to homepage
- Sidenotes display in margin on desktop, toggle on mobile
- Footer "Return home" link works
- Post appears on homepage
