#!/usr/bin/env python3
"""Update Reserve links on fleet pages to carry ?car= query param."""
from pathlib import Path

ROOT = Path(__file__).parent.parent
FLEET = ROOT / "fleet"

# Map filename -> slug used by index.html prefillReserve()
SLUGS = {
    "rolls-royce-spectre.html": "spectre",
    "aston-martin-db12.html":   "db12",
    "mclaren-750s.html":        "750s",
    "ferrari-purosangue.html":  "purosangue",
    "mercedes-g63.html":        "g63",
    "porsche-911-gt3.html":     "911",
}


def main():
    for filename, slug in SLUGS.items():
        path = FLEET / filename
        text = path.read_text()

        # Nav Reserve button: change in-page #reserve to homepage with car param
        text = text.replace(
            '<a href="#reserve" class="btn-primary" style="padding:10px 20px;">Reserve</a>',
            f'<a href="../index.html?car={slug}#reserve" class="btn-primary" style="padding:10px 20px;">Reserve</a>',
            1,
        )

        # Bottom Reserve CTA (Begin reservation)
        text = text.replace(
            '<a href="../index.html#reserve"',
            f'<a href="../index.html?car={slug}#reserve"',
            1,  # only update the first occurrence (the begin reservation link)
        )

        path.write_text(text)
        print(f"  ✓ {filename} -> car={slug}")


if __name__ == "__main__":
    main()
