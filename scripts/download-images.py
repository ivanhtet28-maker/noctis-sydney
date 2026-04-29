#!/usr/bin/env python3
"""
Download all pollinations.ai images from the Noctis site HTML files and
replace remote URLs with local paths.
"""
import re
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

SITE_ROOT = Path(__file__).parent.parent
IMAGES_DIR = SITE_ROOT / "images"
IMAGES_DIR.mkdir(exist_ok=True)

# Map each HTML file to its image slots (local filename relative to images/)
# and the relative path prefix to use in that HTML file's src attributes
FILES = [
    {
        "html": SITE_ROOT / "index.html",
        "prefix": "images/",  # path from index.html to images/
        "slots": [
            "sydney-hero.jpg",
            "spectre-card.jpg",
            "db12-card.jpg",
            "750s-card.jpg",
            "purosangue-card.jpg",
            "g63-card.jpg",
            "911-card.jpg",
        ],
    },
    {
        "html": SITE_ROOT / "fleet" / "rolls-royce-spectre.html",
        "prefix": "../images/",
        "slots": ["spectre-hero.jpg", "spectre-1.jpg", "spectre-2.jpg", "spectre-3.jpg", "spectre-4.jpg"],
    },
    {
        "html": SITE_ROOT / "fleet" / "aston-martin-db12.html",
        "prefix": "../images/",
        "slots": ["db12-hero.jpg", "db12-1.jpg", "db12-2.jpg", "db12-3.jpg", "db12-4.jpg"],
    },
    {
        "html": SITE_ROOT / "fleet" / "mclaren-750s.html",
        "prefix": "../images/",
        "slots": ["750s-hero.jpg", "750s-1.jpg", "750s-2.jpg", "750s-3.jpg", "750s-4.jpg"],
    },
    {
        "html": SITE_ROOT / "fleet" / "ferrari-purosangue.html",
        "prefix": "../images/",
        "slots": ["purosangue-hero.jpg", "purosangue-1.jpg", "purosangue-2.jpg", "purosangue-3.jpg", "purosangue-4.jpg"],
    },
    {
        "html": SITE_ROOT / "fleet" / "mercedes-g63.html",
        "prefix": "../images/",
        "slots": ["g63-hero.jpg", "g63-1.jpg", "g63-2.jpg", "g63-3.jpg", "g63-4.jpg"],
    },
    {
        "html": SITE_ROOT / "fleet" / "porsche-911-gt3.html",
        "prefix": "../images/",
        "slots": ["911-hero.jpg", "911-1.jpg", "911-2.jpg", "911-3.jpg", "911-4.jpg"],
    },
]

POLLINATIONS_RE = re.compile(r"url\('(https://image\.pollinations\.ai/prompt/[^']+)'\)")


def extract_pollinations_urls(html_text):
    return POLLINATIONS_RE.findall(html_text)


def download_image(url, dest_path, retries=4):
    if dest_path.exists():
        print(f"  ✓ skip {dest_path.name} (exists)")
        return True
    print(f"  ↓ {dest_path.name} …", flush=True)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
            dest_path.write_bytes(data)
            size_kb = len(data) // 1024
            print(f"  ✓ {dest_path.name} ({size_kb} KB)")
            return True
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 8 * (attempt + 1)
                print(f"  ⏳ rate-limited, waiting {wait}s …", flush=True)
                time.sleep(wait)
            else:
                print(f"  ✗ {dest_path.name}: HTTP {e.code}")
                return False
        except Exception as e:
            print(f"  ✗ {dest_path.name}: {e}")
            return False
    print(f"  ✗ {dest_path.name}: gave up after {retries} attempts")
    return False


def patch_html(html_path, url_to_local):
    text = html_path.read_text(encoding="utf-8")
    original = text
    for remote_url, local_path in url_to_local.items():
        text = text.replace(f"url('{remote_url}')", f"url('{local_path}')")
    if text != original:
        html_path.write_text(text, encoding="utf-8")
        print(f"  ✎ patched {html_path.name}")


def main():
    # Phase 1: collect all (url, dest_path, html_path, local_src) tuples
    download_tasks = []  # (url, dest_path)
    patch_map = {}       # html_path -> {remote_url: local_src}

    for entry in FILES:
        html_path = entry["html"]
        prefix = entry["prefix"]
        slots = entry["slots"]

        html_text = html_path.read_text(encoding="utf-8")
        urls = extract_pollinations_urls(html_text)

        if len(urls) != len(slots):
            print(f"WARNING: {html_path.name} has {len(urls)} URLs but {len(slots)} slots defined")
            n = min(len(urls), len(slots))
            urls = urls[:n]
            slots = slots[:n]

        for url, slot in zip(urls, slots):
            dest_path = IMAGES_DIR / slot
            local_src = prefix + slot
            download_tasks.append((url, dest_path))
            patch_map.setdefault(html_path, {})[url] = local_src

    # De-duplicate download tasks (same URL may appear in multiple slots, unlikely here)
    seen = set()
    unique_tasks = []
    for url, path in download_tasks:
        if path not in seen:
            seen.add(path)
            unique_tasks.append((url, path))

    print(f"\nDownloading {len(unique_tasks)} images to images/ …\n")

    # Phase 2: download sequentially to avoid rate limiting
    failed = []
    for i, (url, path) in enumerate(unique_tasks, 1):
        print(f"[{i}/{len(unique_tasks)}]", end=" ")
        if not download_image(url, path):
            failed.append(path.name)
        time.sleep(1.5)  # polite delay between requests

    # Phase 3: patch HTML files (only for successfully downloaded images)
    print(f"\nPatching HTML files …\n")
    for html_path, url_map in patch_map.items():
        # Only replace URLs whose local file actually downloaded
        filtered = {url: local for url, local in url_map.items()
                    if (IMAGES_DIR / Path(local).name).exists()}
        if filtered:
            patch_html(html_path, filtered)

    print(f"\nDone. {len(unique_tasks) - len(failed)}/{len(unique_tasks)} images downloaded.")
    if failed:
        print(f"Failed: {', '.join(failed)}")


if __name__ == "__main__":
    main()
