# Tufte CSS HTML Patterns

Reference for all HTML patterns used in this project. Copy and adapt as needed.

## Page Template

```html
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">
<title>PAGE TITLE | Lef adores you ❤️</title>
<link rel="icon" href="/favicon.ico" type="image/x-icon">
<link rel="stylesheet" href="/tufte.min.css"/>
</head>
<body>
    <a href="/">
        <img class="full-width" src="/media/00-common/lef_eyes_2021-06.jpg">
    </a>
    <img style="position: relative; opacity: 0; z-index: -9;" src="/media/00-common/lef_eyes_2021-06.jpg">
    <article>
        <section>
            <h1>PAGE TITLE</h1>
            <p>First paragraph.</p>
        </section>
    </article>
    <footer><a href="/">Return home</a></footer>
</body>
</html>
```

Note: The invisible duplicate banner image is a spacing hack — do not remove it.

## Sidenote (Numbered Marginal Note)

Each sidenote needs a **unique id** within the page. Place inline within a `<p>`:

```html
<label class="sidenote-number"></label>
<label for="unique-id" class="margin-toggle">⊕</label>
<input type="checkbox" id="unique-id" class="margin-toggle">
<span class="marginnote sidenote">
    <em>Note content here.</em>
</span>
```

- Desktop: appears in the right margin with a superscript number
- Mobile: collapses behind a ⊕ toggle button (CSS-only, no JS)

## Sidenote with Image

```html
<label class="sidenote-number"></label>
<label for="unique-id" class="margin-toggle">⊕</label>
<input type="checkbox" id="unique-id" class="margin-toggle">
<span class="marginnote sidenote">
    <img src="/media/YYYYMMDD-slug/image.png">
</span>
```

## Full-Width Image

```html
<img class="full-width" src="/media/YYYYMMDD-slug/image.jpg">
```

## Blockquote

```html
<blockquote>
    <h3>Title</h3>
    Content here.
</blockquote>
```

## Inline Code

```html
<code>some_command</code>
```

## Links

Same tab:
```html
<a href="/pages/posts/YYYYMMDD-slug.html">Link text</a>
```

New tab (external links):
```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Link text</a>
```

## Section Structure

Posts use `<article>` with multiple `<section>` children. Each section typically has a heading:

```html
<article>
    <section>
        <h1>Post Title</h1>
        <p>Intro content...</p>
    </section>
    <section>
        <h2>Subsection</h2>
        <p>More content...</p>
    </section>
</article>
```
