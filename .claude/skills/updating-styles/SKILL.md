---
name: updating-styles
description: Modify the Tufte CSS stylesheet and regenerate the minified version.
---

# Updating Styles

## When to Use
When making any CSS changes to the website's appearance.

## Steps

1. **Edit the source stylesheet**
   - Path: `src/tufte.css`
   - Never edit `tufte.min.css` directly — it's generated

2. **Regenerate minified CSS**
   - Run: `npm run cssmin`
   - This overwrites `src/tufte.min.css` from `src/tufte.css`

3. **Preview changes**
   - Run: `npm run start`
   - Check multiple pages (homepage + a post) to verify nothing broke
   - Test responsive behavior at narrow widths (sidenote toggles, full-width images)

4. **Commit both files**
   - Always commit `tufte.css` and `tufte.min.css` together

## Key CSS Architecture
- Base width: 55% for text, right margin reserved for sidenotes
- Responsive: orientation-based media queries (portrait mode triggers mobile layout)
- Sidenotes use CSS counters for automatic numbering
- Full-width images use `max-width: none` to escape the text column
- Colors: background `#f9fefc`, text `#443b36`, accent `#dc5945`
- Font: ET Book (custom, loaded from `et-book/` directory)
