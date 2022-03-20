# Lef's web 🕷

This maybe the beginning of something fun.
Who knows?
Not me, lol.
You look dashing ❤️

Find me at [lef.fyi](https://lef.fyi/) 👾

## Dev Setup

1. Run `npm install clean-css-cli -g` in order to produce the minified version of the CSS files.
    - `cleancss -o src/tufte.min.css src/tufte.css`
    - Needs to be run only if you made changes to `src/tufte.css`
2. _(Optional)_ Install the necessary Python tools by running [`poetry install`](https://python-poetry.org/) inside the `tools/` folder.
    - _Note: There's currently no other dependencies than [`black`](https://black.readthedocs.io/en/stable/)_

## Resources

I used the following to do stuff so far:

- [AWS S3 static web hosting with CloudFlare](https://support.cloudflare.com/hc/en-us/articles/360037983412-Configuring-an-Amazon-Web-Services-static-site-to-use-Cloudflare)
- [AWS S3 static web hosting _clicky-clicky_ walkthrough](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html)
- [More AWS S3 web hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- Color palette generated from [huemint](https://huemint.com/brand-2/#palette=f9fefc-443b36-dc5945)
- CSS style from [Edward Tufte](https://edwardtufte.github.io/tufte-css/)

## ToDos

- [ ] terraform ALL the infra
- [ ] every branch gets a published subdomain automagically
- [ ] switch away from writting crude HTML/CSS to some fancy markdown to HTML tool
- [ ] start some sort of blog
