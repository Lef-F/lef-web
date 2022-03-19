import os
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    dest="domain",
    type=str,
    help="The domain name of your website e.g. https://lef.fyi",
)

parser.add_argument(
    dest="src",
    type=str,
    help="The full path to the source code of your website.",
)

parser.add_argument(
    "--except",
    type=str,
    help="Items to exclude declared with relative paths from the root folder or your website source code.",
    nargs="*",
    dest="skip",
    default=[],
)

args = parser.parse_args()

src_path = args.src


def path_is_skipped(path: str) -> bool:
    for path_to_skip in args.skip:
        if path.lower() in path_to_skip.lower():
            return True
        if path_to_skip.lower() in path.lower():
            return True
    return False


def crawl_site(path: str, map: list = []) -> list:
    path_contents = os.listdir(path)
    for item in path_contents:
        item = os.path.join(path, item)
        if os.path.isdir(item):
            crawl_site(item, map)
        else:
            if not path_is_skipped(item):
                map.append(item)
    return map


website_paths = crawl_site(src_path)

if args.domain[-1] == "/":
    domain = args.domain
else:
    domain = args.domain + "/"

website_paths = [
    path.replace(
        src_path,
        domain,
    )
    for path in website_paths
]

print("Here are all the files identified in your website:", website_paths)

sitemap_file = os.path.join(args.src, "sitemap.txt")
with open(sitemap_file, "w") as f:
    f.write("\n".join(website_paths))

print(f"They have succesfully been written to {sitemap_file}")
