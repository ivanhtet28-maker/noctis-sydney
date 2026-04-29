#!/usr/bin/env python3
"""
rebuild_fleet.py

Rewrites the body of each fleet detail page to match the Forza Exotics
product-page LAYOUT (booking-focused), while preserving the existing
Noctis dark editorial DESIGN LANGUAGE.

What's kept (verbatim):
  - The entire <head> (OG meta, JSON-LD, Google Fonts, the shared
    Noctis stylesheet).
  - The <header class="noctis-nav"> nav bar.
  - The reserve link target (../index.html?car={slug}#reserve).
  - The image filenames used by the gallery
    (../images/{slug}-hero.jpg, -1, -2, -3, -4).
  - The minimal <footer>.

What's replaced:
  - Everything between </header> and </body>: the full-bleed 3D-style
    hero, the editorial story, the "three things most won't notice"
    pillars, the reviewer quote, the long specs grid, the
    "three drives" section, the now-redundant secondary gallery, and
    the standalone Reserve CTA section.

The new page body, top to bottom, is:
  1. Breadcrumb strip ("Home / The Fleet / {Name}")
  2. Big H1 ("{Brand} <em>{Model}</em>") in Fraunces .display-xl
  3. Two-column booking layout:
     - LEFT: large main image (id="gMain") + 5-up thumb strip
     - RIGHT: sticky booking card — strikethrough price + day price,
       date/time pickers, cash-on-delivery checkbox, full-width
       Reserve Now (links to ../index.html?car={slug}#reserve),
       Apple Pay & Google Pay, weekly/monthly discount footer
  4. Vehicle Details — 2-card grid (Terms + Minimum Days)
  5. 4-stat spec strip (Engine, Seats, 0-100, From)
  6. Vehicle Description — single tight paragraph with <strong> on key specs
  7. The original Reserve CTA section is REMOVED; the booking card is
     the primary call to action. The id="reserve" anchor still exists
     on the homepage (../index.html?car={slug}#reserve).
  8. Footer (unchanged from the original)

Usage:
  python3 scripts/rebuild_fleet.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
FLEET_DIR = ROOT / "fleet"


# --------------------------------------------------------------------------
# Per-car data
# --------------------------------------------------------------------------

@dataclass
class Car:
    file: str           # filename in fleet/
    slug: str           # short slug used in image filenames AND ?car= param
    brand: str
    model: str          # the italicised part of the H1
    eyebrow: str        # category line
    image_slug: str     # prefix used in /images/ (matches existing files)
    original: str
    day: str
    week_total: str
    engine: str
    seats: str
    zero_hundred: str
    description_html: str  # ~80 words, <strong> on key specs


CARS: list[Car] = [
    Car(
        file="rolls-royce-spectre.html",
        slug="spectre",
        brand="Rolls-Royce",
        model="Spectre.",
        eyebrow="No. 01 · Electric Coupe · 2025",
        image_slug="spectre",
        original="A$7,200",
        day="A$6,700",
        week_total="A$32,500",
        engine="577 hp dual-motor EV",
        seats="4",
        zero_hundred="4.5 s",
        description_html=(
            "The Spectre is Rolls-Royce's first fully-electric car — twenty-three "
            "feet of <strong>silent torque</strong>, riding on the same Architecture "
            "of Luxury that underpins the Phantom. <strong>577 horsepower</strong> "
            "and <strong>900 Nm</strong> arrive instantly from a "
            "<strong>dual-motor</strong> drivetrain, yet the cabin sits at a "
            "measured fifty-seven decibels at highway speed. "
            "<strong>0–100 km/h in 4.5 seconds</strong>, "
            "<strong>485 km of WLTP range</strong>, and a coachline that runs the "
            "full length of the body, hand-drawn in a single stroke."
        ),
    ),
    Car(
        file="aston-martin-db12.html",
        slug="db12",
        brand="Aston Martin",
        model="DB12 Volante.",
        eyebrow="No. 02 · Grand Tourer · 2024",
        image_slug="db12",
        original="A$5,400",
        day="A$4,950",
        week_total="A$24,000",
        engine="Twin-turbo V8 680 hp",
        seats="4",
        zero_hundred="3.6 s",
        description_html=(
            "Aston Martin's first \"super tourer,\" with the roof off. "
            "The 4.0-litre <strong>twin-turbo V8</strong> delivers "
            "<strong>680 horsepower</strong> and <strong>800 Nm</strong>, "
            "tuned at Gaydon for a softened note above 2,500 rpm — what Aston "
            "calls the conversation frequency. The eight-layer Z-fold roof "
            "retracts in <strong>14 seconds</strong> and preserves the original "
            "DB profile when raised. <strong>0–100 km/h in 3.6 seconds</strong>, "
            "<strong>325 km/h top speed</strong>, Bridge of Weir leather tanned "
            "in chestnut bark for thirty days."
        ),
    ),
    Car(
        file="mclaren-750s.html",
        slug="750s",
        brand="McLaren",
        model="750S Spider.",
        eyebrow="No. 03 · Supercar · 2024",
        image_slug="750s",
        original="A$6,800",
        day="A$6,250",
        week_total="A$30,000",
        engine="Twin-turbo V8 740 hp",
        seats="2",
        zero_hundred="2.7 s",
        description_html=(
            "The lightest car in its class — <strong>1,326 kg</strong> dry — "
            "and the loudest argument for the convertible supercar still "
            "being a category. The 4.0-litre <strong>twin-turbo V8</strong> "
            "delivers <strong>740 horsepower</strong> and <strong>800 Nm</strong> "
            "through a 7-speed dual-clutch. Roof down in "
            "<strong>11 seconds</strong> at speeds up to 50 km/h. "
            "<strong>0–100 km/h in 2.7 seconds</strong>, "
            "<strong>332 km/h top speed</strong>, carbon-fibre monocell, hydraulic "
            "steering rack, no rear screen — only what the pace demands."
        ),
    ),
    Car(
        file="ferrari-purosangue.html",
        slug="purosangue",
        brand="Ferrari",
        model="Purosangue.",
        eyebrow="No. 04 · Four-Seat V12 · 2024",
        image_slug="purosangue",
        original="A$8,300",
        day="A$7,700",
        week_total="A$37,000",
        engine="Naturally-aspirated V12 725 hp",
        seats="4",
        zero_hundred="3.3 s",
        description_html=(
            "Ferrari's first four-door, four-seat car — and the only one in the "
            "segment with a <strong>naturally-aspirated V12</strong> mounted "
            "behind the front axle. <strong>725 horsepower</strong> at 7,750 rpm, "
            "<strong>716 Nm</strong> at 6,250, with a 8,250 rpm redline that "
            "feels closer to a 12Cilindri than an SUV. Rear-hinged coach doors, "
            "active suspension borrowed from the Multimatic-developed "
            "spool-valve dampers, four individually-sculpted seats. "
            "<strong>0–100 km/h in 3.3 seconds</strong>, <strong>310 km/h top "
            "speed</strong>. Built in Maranello, by hand, in limited numbers."
        ),
    ),
    Car(
        file="mercedes-g63.html",
        slug="g63",
        brand="Mercedes-AMG",
        model="G 63.",
        eyebrow="No. 05 · Off-Road Icon · 2024",
        image_slug="g63",
        original="A$3,600",
        day="A$3,100",
        week_total="A$15,000",
        engine="Twin-turbo V8 577 hp",
        seats="5",
        zero_hundred="4.5 s",
        description_html=(
            "Forty-five years of the same silhouette and three exposed door hinges "
            "that AMG insisted on keeping. Underneath: a 4.0-litre "
            "<strong>twin-turbo V8</strong> delivering <strong>577 horsepower</strong> "
            "and <strong>850 Nm</strong>, three locking differentials, and a "
            "ladder-frame chassis that will outlive every road in Sydney. "
            "<strong>0–100 km/h in 4.5 seconds</strong>, "
            "<strong>240 km/h limited top speed</strong>. Hand-finished at AMG "
            "Affalterbach by a single technician — one engine, one builder, one "
            "signature on the cam cover."
        ),
    ),
    Car(
        file="porsche-911-gt3.html",
        slug="911",
        brand="Porsche",
        model="911 GT3 Touring.",
        eyebrow="No. 06 · Track-Bred 911 · 2024",
        image_slug="911",
        original="A$4,700",
        day="A$4,250",
        week_total="A$20,500",
        engine="Naturally-aspirated flat-six 510 hp",
        seats="2",
        zero_hundred="3.4 s",
        description_html=(
            "The GT3 without the wing — the same motorsport-derived "
            "<strong>4.0-litre naturally-aspirated flat-six</strong>, the same "
            "<strong>9,000 rpm redline</strong>, the same double-wishbone front "
            "axle from the 911 RSR race car. <strong>510 horsepower</strong>, "
            "<strong>470 Nm</strong>, and a 6-speed manual offered at no cost "
            "over the PDK — Porsche's quiet acknowledgement that some buyers "
            "still want to do the work themselves. "
            "<strong>0–100 km/h in 3.4 seconds</strong>, "
            "<strong>320 km/h top speed</strong>. The Touring trim adds an "
            "extendable rear lip in place of the fixed swan-neck wing — restraint, "
            "the Stuttgart way."
        ),
    ),
]


# --------------------------------------------------------------------------
# HTML fragments
# --------------------------------------------------------------------------

# Style additions injected into the existing <style> block (just before
# the closing </style>). Keeping them inline-per-page so we don't link
# any external CSS.
EXTRA_STYLE = """
/* ==========================================
   Fleet detail — Forza-style booking layout
   (added by scripts/rebuild_fleet.py)
   ========================================== */
.breadcrumb {
  border-top: 1px solid var(--line);
  padding: 96px 0 24px;
  font-size: 12px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}
.breadcrumb a { color: var(--muted); text-decoration: none; transition: color 200ms ease; }
.breadcrumb a:hover { color: var(--cream); }
.breadcrumb .sep { margin: 0 12px; color: var(--subtle); }

.product-title {
  padding: 8px 0 56px;
}
.product-title h1 {
  margin: 0;
  color: var(--cream);
}

.booking-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 48px;
  padding-bottom: 96px;
}
@media (min-width: 960px) {
  .booking-grid { grid-template-columns: 1.4fr 1fr; gap: 56px; align-items: start; }
}

.booking-gallery .gallery-main {
  aspect-ratio: 16/10;
  border: 1px solid var(--line);
}
.booking-gallery .gallery-thumbs {
  margin-top: 8px;
  background: transparent;
  padding: 0;
  gap: 8px;
}
.booking-gallery .gallery-thumb {
  border: 1px solid var(--line);
}

.booking-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 32px;
}
@media (min-width: 960px) {
  .booking-card { position: sticky; top: 96px; }
}

.price-row {
  display: flex;
  align-items: baseline;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 28px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--line);
}
.price-strike {
  font-family: 'Fraunces', serif;
  font-size: 22px;
  color: var(--subtle);
  text-decoration: line-through;
  letter-spacing: -0.02em;
}
.price-day {
  font-family: 'Fraunces', serif;
  font-size: 36px;
  letter-spacing: -0.025em;
  line-height: 1;
  color: var(--cream);
}
.price-day .unit { font-size: 14px; color: var(--muted); font-family: 'Inter', sans-serif; letter-spacing: normal; margin-left: 6px; }

.field-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 16px;
}
.field { display: flex; flex-direction: column; gap: 6px; }
.field label {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--muted);
}
.field input, .field select {
  background: #0E0D0C;
  border: 1px solid var(--line);
  border-radius: 4px;
  padding: 11px 12px;
  color: var(--cream);
  font-family: inherit;
  font-size: 14px;
  outline: none;
  transition: border-color 200ms ease;
  -webkit-appearance: none;
  appearance: none;
}
.field select {
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'><path d='M1 1l4 4 4-4' stroke='%238C8576' stroke-width='1.4' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 30px;
}
.field input:focus, .field select:focus { border-color: var(--cream); }
.field input::-webkit-calendar-picker-indicator { filter: invert(0.5); cursor: pointer; }

.cod-row {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin: 18px 0 6px;
  padding: 14px;
  background: #0E0D0C;
  border: 1px solid var(--line);
  border-radius: 4px;
}
.cod-row input[type="checkbox"] {
  margin-top: 3px;
  accent-color: var(--accent);
  width: 14px; height: 14px;
}
.cod-row label {
  font-size: 13px; color: var(--cream); cursor: pointer; line-height: 1.4;
}
.cod-row .cod-explainer {
  font-size: 11px; color: var(--muted); margin-top: 6px; line-height: 1.5;
}

.btn-reserve {
  display: block;
  width: 100%;
  background: var(--accent);
  color: var(--cream);
  text-align: center;
  text-decoration: none;
  padding: 16px 20px;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  border-radius: 4px;
  margin-top: 18px;
  transition: background 220ms ease, transform 220ms var(--ease);
  border: none;
  cursor: pointer;
  font-family: inherit;
}
.btn-reserve:hover { background: var(--accent-hover); transform: translateY(-1px); }

.pay-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  background: #000;
  color: #fff;
  border: 1px solid #000;
  border-radius: 4px;
  padding: 12px 16px;
  font-size: 14px;
  font-family: inherit;
  cursor: pointer;
  margin-top: 10px;
  text-decoration: none;
  transition: opacity 200ms ease;
}
.pay-btn:hover { opacity: 0.85; }
.pay-btn svg { display: block; }

.discount-footer {
  margin-top: 22px;
  padding: 14px 16px;
  background: #0E0D0C;
  border: 1px solid var(--line);
  border-radius: 4px;
  font-size: 12px;
  color: var(--muted);
  line-height: 1.55;
  letter-spacing: 0.02em;
}

.detail-cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
  padding: 24px 0 96px;
  border-top: 1px solid var(--line);
}
@media (min-width: 720px) { .detail-cards { grid-template-columns: 1fr 1fr; gap: 20px; padding-top: 48px; } }
.detail-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 4px;
  padding: 24px 26px;
}
.detail-card .dc-head {
  display: flex; align-items: center; gap: 10px; margin-bottom: 12px;
}
.detail-card .dc-glyph {
  width: 22px; height: 22px;
  display: inline-flex; align-items: center; justify-content: center;
  color: var(--accent);
}
.detail-card h3 {
  font-family: 'Fraunces', serif;
  font-size: 18px;
  letter-spacing: -0.01em;
  margin: 0;
  color: var(--cream);
  font-weight: 400;
}
.detail-card p {
  margin: 0;
  font-size: 14px;
  line-height: 1.65;
  color: rgba(245, 241, 234, 0.7);
}

.spec-strip {
  display: grid;
  grid-template-columns: 1fr;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}
@media (min-width: 720px) { .spec-strip { grid-template-columns: repeat(4, 1fr); } }
.spec-strip .cell {
  padding: 32px 28px;
  border-bottom: 1px solid var(--line);
}
@media (min-width: 720px) {
  .spec-strip .cell { border-bottom: none; border-right: 1px solid var(--line); }
  .spec-strip .cell:last-child { border-right: none; }
}
.spec-strip .cell:last-child { border-bottom: none; }
.spec-strip .cell .lbl {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.22em;
  color: var(--muted);
  margin-bottom: 12px;
}
.spec-strip .cell .val {
  font-family: 'Fraunces', serif;
  font-size: 26px;
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: var(--cream);
}

.description-block {
  padding: 96px 0;
  max-width: 760px;
}
.description-block .eyebrow { margin-bottom: 18px; }
.description-block h2 {
  font-family: 'Fraunces', serif;
  font-size: clamp(28px, 3.5vw, 38px);
  letter-spacing: -0.02em;
  margin: 0 0 24px;
  color: var(--cream);
  font-weight: 400;
}
.description-block p {
  font-size: 16px;
  line-height: 1.7;
  color: rgba(245, 241, 234, 0.78);
  margin: 0;
}
.description-block p strong {
  color: var(--cream);
  font-weight: 500;
}
"""


def render_body(car: Car) -> str:
    """Render the new <body> contents (everything between </header> and </body>)."""
    slug = car.slug
    img = car.image_slug

    return f"""
<!-- BREADCRUMB -->
<section class="breadcrumb">
  <div class="container">
    <a href="../index.html">Home</a><span class="sep">/</span><a href="../index.html#fleet">The Fleet</a><span class="sep">/</span><span style="color:var(--cream);">{car.brand} {car.model.rstrip('.')}</span>
  </div>
</section>

<!-- TITLE -->
<section class="product-title">
  <div class="container">
    <p class="eyebrow" style="margin-bottom:16px;">{car.eyebrow}</p>
    <h1 class="display-xl">
      {car.brand}<br /><em class="italic-light">{car.model}</em>
    </h1>
  </div>
</section>

<!-- BOOKING (gallery + reservation card) -->
<section>
  <div class="container">
    <div class="booking-grid">

      <!-- LEFT: gallery -->
      <div class="booking-gallery">
        <div class="gallery-main" id="gMain" style="background-image:url('../images/{img}-hero.jpg')"></div>
        <div class="gallery-thumbs">
          <div class="gallery-thumb active" data-src="../images/{img}-hero.jpg" style="background-image:url('../images/{img}-hero.jpg')"></div>
          <div class="gallery-thumb" data-src="../images/{img}-1.jpg" style="background-image:url('../images/{img}-1.jpg')"></div>
          <div class="gallery-thumb" data-src="../images/{img}-2.jpg" style="background-image:url('../images/{img}-2.jpg')"></div>
          <div class="gallery-thumb" data-src="../images/{img}-3.jpg" style="background-image:url('../images/{img}-3.jpg')"></div>
          <div class="gallery-thumb" data-src="../images/{img}-4.jpg" style="background-image:url('../images/{img}-4.jpg')"></div>
        </div>
      </div>

      <!-- RIGHT: booking card -->
      <aside class="booking-card" aria-label="Reserve {car.brand} {car.model.rstrip('.')}">
        <div class="price-row">
          <span class="price-strike">{car.original}</span>
          <span class="price-day">{car.day}<span class="unit">/ day</span></span>
        </div>

        <form onsubmit="event.preventDefault(); window.location.href='../index.html?car={slug}#reserve';">
          <div class="field-row">
            <div class="field">
              <label for="puDate">Pick-up date</label>
              <input type="date" id="puDate" />
            </div>
            <div class="field">
              <label for="puTime">Pick-up time</label>
              <select id="puTime">
                <option>09:00</option><option>10:00</option><option>11:00</option>
                <option>12:00</option><option>14:00</option><option>16:00</option><option>18:00</option>
              </select>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="rtDate">Return date</label>
              <input type="date" id="rtDate" />
            </div>
            <div class="field">
              <label for="rtTime">Return time</label>
              <select id="rtTime">
                <option>09:00</option><option>10:00</option><option>11:00</option>
                <option>12:00</option><option>14:00</option><option>16:00</option><option>18:00</option>
              </select>
            </div>
          </div>

          <div class="cod-row">
            <input type="checkbox" id="cod" />
            <div>
              <label for="cod">I would like to pay with Cash on Delivery</label>
              <p class="cod-explainer">By selecting this option, you agree to pay an initial deposit of A$500 now. The remainder is settled on delivery.</p>
            </div>
          </div>

          <button type="submit" class="btn-reserve">Reserve Now</button>
        </form>

        <button type="button" class="pay-btn" aria-label="Pay with Apple Pay" onclick="window.location.href='../index.html?car={slug}#reserve'">
          <svg width="14" height="16" viewBox="0 0 14 16" fill="currentColor" aria-hidden="true"><path d="M11.5 8.5c0-1.6 1.3-2.4 1.4-2.4-0.8-1.1-2-1.3-2.4-1.3-1-0.1-2 0.6-2.5 0.6s-1.3-0.6-2.2-0.6c-1.1 0-2.2 0.7-2.8 1.7-1.2 2.1-0.3 5.2 0.9 6.9 0.6 0.8 1.3 1.7 2.2 1.7 0.9 0 1.2-0.6 2.3-0.6s1.4 0.6 2.3 0.5c1 0 1.6-0.8 2.2-1.7 0.7-1 1-2 1-2-0-0-2-0.8-2-3 zM10 3.5c0.5-0.6 0.8-1.4 0.7-2.2-0.7 0-1.5 0.5-2 1-0.4 0.5-0.8 1.3-0.7 2.1 0.8 0.1 1.5-0.4 2-0.9z"/></svg>
          <span style="font-weight:500;">Pay</span>
        </button>
        <button type="button" class="pay-btn" aria-label="Pay with Google Pay" onclick="window.location.href='../index.html?car={slug}#reserve'">
          <svg width="16" height="16" viewBox="0 0 18 18" aria-hidden="true"><path d="M17.6 9.2c0-.6-.1-1.2-.2-1.7H9v3.3h4.8c-.2 1.1-.8 2-1.8 2.6v2.2h2.9c1.7-1.5 2.7-3.8 2.7-6.4z" fill="#fff"/><path d="M9 18c2.4 0 4.5-.8 6-2.2l-2.9-2.2c-.8.5-1.8.9-3.1.9-2.4 0-4.4-1.6-5.1-3.8H.9v2.3C2.4 16 5.5 18 9 18z" fill="#fff"/><path d="M3.9 10.7c-.2-.5-.3-1.1-.3-1.7s.1-1.2.3-1.7V5H.9C.3 6.2 0 7.6 0 9s.3 2.8.9 4l3-2.3z" fill="#fff"/><path d="M9 3.6c1.4 0 2.6.5 3.5 1.4l2.6-2.6C13.5.9 11.4 0 9 0 5.5 0 2.4 2 .9 5l3 2.3C4.6 5.2 6.6 3.6 9 3.6z" fill="#fff"/></svg>
          <span style="font-weight:500;">Pay</span>
        </button>

        <div class="discount-footer">
          Weekly Discount (7+ days, 15% off) &nbsp;·&nbsp; Monthly Discount (28+ days, 25% off)
        </div>
      </aside>

    </div>
  </div>
</section>

<!-- VEHICLE DETAILS -->
<section>
  <div class="container">
    <div class="detail-cards">
      <div class="detail-card">
        <div class="dc-head">
          <span class="dc-glyph" aria-hidden="true">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M9 13h6"/><path d="M9 17h6"/></svg>
          </span>
          <h3>Terms</h3>
        </div>
        <p>300 km included per day · A$3.50 per additional km · Security deposit A$5,000–A$15,000, refunded on return.</p>
      </div>
      <div class="detail-card">
        <div class="dc-head">
          <span class="dc-glyph" aria-hidden="true">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/></svg>
          </span>
          <h3>Minimum days</h3>
        </div>
        <p>Weekend (Friday–Sunday): 2 days minimum · Weekdays (Monday–Thursday): 1 day minimum.</p>
      </div>
    </div>
  </div>
</section>

<!-- SPEC STRIP -->
<section>
  <div class="container">
    <div class="spec-strip">
      <div class="cell">
        <p class="lbl">Engine</p>
        <p class="val">{car.engine}</p>
      </div>
      <div class="cell">
        <p class="lbl">Seats</p>
        <p class="val">{car.seats}</p>
      </div>
      <div class="cell">
        <p class="lbl">0–100 km/h</p>
        <p class="val">{car.zero_hundred}</p>
      </div>
      <div class="cell">
        <p class="lbl">From</p>
        <p class="val">{car.day}<span class="unit" style="font-size:13px; color:var(--muted); font-family:'Inter',sans-serif; letter-spacing:normal; margin-left:4px;">/ day</span></p>
      </div>
    </div>
  </div>
</section>

<!-- VEHICLE DESCRIPTION -->
<section>
  <div class="container">
    <div class="description-block">
      <p class="eyebrow">Vehicle description</p>
      <h2>The {car.model.rstrip('.')}, briefly.</h2>
      <p>{car.description_html}</p>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer style="border-top:1px solid var(--line); padding:64px 0; text-align:center;">
  <div class="container">
    <p class="font-serif" style="font-size:32px; letter-spacing:-0.03em; line-height:1; margin:0;">Noctis</p>
    <p class="eyebrow" style="margin-top:12px;">Sydney · Palm Beach · Southern Highlands</p>
    <p style="margin-top:40px; color:var(--muted); font-size:12px;">© 2026 Noctis Automotive Pty Ltd · Sydney, Australia</p>
  </div>
</footer>

<!-- Gallery thumbnail swap -->
<script>
(function () {{
  var main = document.getElementById('gMain');
  if (!main) return;
  var thumbs = document.querySelectorAll('.gallery-thumb');
  thumbs.forEach(function (t) {{
    t.addEventListener('click', function () {{
      main.style.opacity = '0';
      setTimeout(function () {{
        main.style.backgroundImage = "url('" + t.dataset.src + "')";
        main.style.opacity = '1';
      }}, 160);
      thumbs.forEach(function (x) {{ x.classList.remove('active'); }});
      t.classList.add('active');
    }});
  }});
}})();
</script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# Rebuild
# --------------------------------------------------------------------------

# Pattern that captures the file from start through </header> (the nav close).
# Everything after the first </header> is the old editorial body — we
# discard it and write a fresh body in its place.
HEAD_NAV_PATTERN = re.compile(
    r"^(?P<head>.*?</style>)(?P<rest_of_head>.*?</head>\s*<body>.*?<header class=\"noctis-nav\">.*?</header>)",
    re.DOTALL,
)


def rebuild_one(path: Path) -> None:
    car = next((c for c in CARS if c.file == path.name), None)
    if car is None:
        raise SystemExit(f"No CARS entry for {path.name}")

    original = path.read_text(encoding="utf-8")

    m = HEAD_NAV_PATTERN.match(original)
    if not m:
        raise SystemExit(f"Could not locate </style>...</header> in {path.name}")

    head_with_style = m.group("head")           # ...up to and including </style>
    rest_of_head_and_nav = m.group("rest_of_head")  # </head><body>...<header>...</header>

    # Inject EXTRA_STYLE just before the closing </style>.
    head_with_style = head_with_style.replace(
        "</style>",
        EXTRA_STYLE.rstrip() + "\n</style>",
    )

    new_body = render_body(car)

    new_html = head_with_style + rest_of_head_and_nav + new_body

    path.write_text(new_html, encoding="utf-8")
    print(f"  rebuilt {path.name}")


def main() -> None:
    print(f"Rebuilding fleet pages in {FLEET_DIR}/ ...")
    for car in CARS:
        rebuild_one(FLEET_DIR / car.file)
    print(f"Done. {len(CARS)} pages rebuilt.")


if __name__ == "__main__":
    main()
