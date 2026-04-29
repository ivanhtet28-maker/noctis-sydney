#!/usr/bin/env python3
"""Inject OG meta tags, favicon, and Vehicle JSON-LD into each fleet page."""
from pathlib import Path

ROOT = Path(__file__).parent.parent
FLEET = ROOT / "fleet"

CARS = {
    "rolls-royce-spectre": {
        "name": "Rolls-Royce Spectre",
        "year": "2025",
        "price": "6700",
        "image": "spectre-hero.jpg",
        "model": "Spectre",
        "brand": "Rolls-Royce",
        "vehicleType": "Coupe",
        "description": "The 2025 Rolls-Royce Spectre — silent, twenty-three feet of electric tension. From Noctis Sydney, by appointment.",
    },
    "aston-martin-db12": {
        "name": "Aston Martin DB12 Volante",
        "year": "2024",
        "price": "4950",
        "image": "db12-hero.jpg",
        "model": "DB12 Volante",
        "brand": "Aston Martin",
        "vehicleType": "Convertible",
        "description": "The Aston Martin DB12 Volante — 680hp, roof down, the last great V8 grand tourer. From Noctis Sydney.",
    },
    "mclaren-750s": {
        "name": "McLaren 750S Spider",
        "year": "2024",
        "price": "6250",
        "image": "750s-hero.jpg",
        "model": "750S Spider",
        "brand": "McLaren",
        "vehicleType": "Convertible",
        "description": "The McLaren 750S Spider — 740hp twin-turbo V8, dihedral doors, chassis honed for the road. From Noctis Sydney.",
    },
    "ferrari-purosangue": {
        "name": "Ferrari Purosangue",
        "year": "2025",
        "price": "7700",
        "image": "purosangue-hero.jpg",
        "model": "Purosangue",
        "brand": "Ferrari",
        "vehicleType": "SUV",
        "description": "The Ferrari Purosangue — naturally-aspirated V12, four doors, the only Ferrari of its kind. From Noctis Sydney.",
    },
    "mercedes-g63": {
        "name": "Mercedes-AMG G 63",
        "year": "2024",
        "price": "3100",
        "image": "g63-hero.jpg",
        "model": "G 63",
        "brand": "Mercedes-AMG",
        "vehicleType": "SUV",
        "description": "The Mercedes-AMG G 63 — Obsidian Black, 577hp V8, the icon. From Noctis Sydney, delivered to your door.",
    },
    "porsche-911-gt3": {
        "name": "Porsche 911 GT3 Touring",
        "year": "2024",
        "price": "4250",
        "image": "911-hero.jpg",
        "model": "911 GT3 Touring",
        "brand": "Porsche",
        "vehicleType": "Coupe",
        "description": "The Porsche 911 GT3 Touring — 9,000rpm flat-six, manual gearbox, no rear wing. The driver's car. From Noctis Sydney.",
    },
}

FAVICON = ('<link rel="icon" type="image/svg+xml" '
           'href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 64 64\'%3E'
           '%3Crect width=\'64\' height=\'64\' rx=\'10\' fill=\'%230A0A0A\'/%3E'
           '%3Ctext x=\'50%25\' y=\'50%25\' dominant-baseline=\'central\' text-anchor=\'middle\' '
           'font-family=\'Georgia,serif\' font-size=\'42\' font-style=\'italic\' fill=\'%23F5F1EA\'%3EN%3C/text%3E'
           '%3C/svg%3E" />')


def build_meta(slug, car):
    url = f"https://noctis.com.au/fleet/{slug}.html"
    img = f"https://noctis.com.au/images/{car['image']}"
    return f'''<meta name="theme-color" content="#0A0A0A" />
<link rel="canonical" href="{url}" />

{FAVICON}

<meta property="og:type" content="product" />
<meta property="og:locale" content="en_AU" />
<meta property="og:url" content="{url}" />
<meta property="og:site_name" content="Noctis Sydney" />
<meta property="og:title" content="{car['name']} · Noctis Sydney" />
<meta property="og:description" content="{car['description']}" />
<meta property="og:image" content="{img}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{car['name']} · Noctis Sydney" />
<meta name="twitter:description" content="{car['description']}" />
<meta name="twitter:image" content="{img}" />

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Vehicle",
  "name": "{car['name']}",
  "brand": {{"@type": "Brand", "name": "{car['brand']}"}},
  "model": "{car['model']}",
  "vehicleModelDate": "{car['year']}",
  "bodyType": "{car['vehicleType']}",
  "image": "{img}",
  "description": "{car['description']}",
  "offers": {{
    "@type": "Offer",
    "price": "{car['price']}",
    "priceCurrency": "AUD",
    "priceSpecification": {{
      "@type": "UnitPriceSpecification",
      "price": "{car['price']}",
      "priceCurrency": "AUD",
      "unitText": "per day"
    }},
    "availability": "https://schema.org/InStock",
    "seller": {{"@type": "AutomotiveBusiness", "name": "Noctis Automotive", "url": "https://noctis.com.au/"}}
  }}
}}
</script>
'''


def main():
    anchor = '<link rel="preconnect" href="https://fonts.googleapis.com" />'
    for slug, car in CARS.items():
        path = FLEET / f"{slug}.html"
        text = path.read_text()
        if 'og:title' in text:
            print(f"  skip {slug} (already has OG)")
            continue
        block = build_meta(slug, car)
        new = text.replace(anchor, block + anchor, 1)
        if new == text:
            print(f"  ✗ {slug}: anchor not found")
            continue
        path.write_text(new)
        print(f"  ✓ {slug}")


if __name__ == "__main__":
    main()
