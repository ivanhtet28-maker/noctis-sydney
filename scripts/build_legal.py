#!/usr/bin/env python3
"""Build the 3 legal stub pages (privacy, terms, responsible driving)."""
from pathlib import Path

ROOT = Path(__file__).parent.parent
LEGAL = ROOT / "legal"

PAGES = {
    "privacy": {
        "title": "Privacy",
        "deck": "How we handle the details you share with us.",
        "updated": "Last updated 14 February 2026",
        "body": """
<h2>1. The short version.</h2>
<p>We collect your name, contact details, dates, and delivery address only to deliver the car you have asked for. Your inquiry is read by a single member of our concierge team. We do not sell, rent, or share your details with third parties for marketing purposes — ever.</p>

<h2>2. What we collect.</h2>
<p>When you submit an inquiry through this site, we collect the information you provide on the form: name, contact (email, phone, or Signal), suburb, dates, and any notes. If you become a guest, we additionally collect your driver's licence details, a copy of your photo ID, and a credit-card or wire authorisation for deposit and final settlement.</p>

<h2>3. How long we keep it.</h2>
<p>Inquiry data that does not become a booking is deleted within 30 days. Booking records are retained for seven years to comply with Australian Tax Office requirements (NAT 11580). Identity verification records are deleted within 60 days of the conclusion of your reservation, unless you ask us to keep them on file for future bookings.</p>

<h2>4. Who sees it.</h2>
<p>Only the three members of our concierge team and the head of fleet have access to guest data. Our payment processor (Stripe) and our identity verifier (Stripe Identity) hold limited records under their own privacy policies. We do not use third-party analytics, marketing platforms, or advertising networks on this site.</p>

<h2>5. Your rights.</h2>
<p>Under the Australian Privacy Act 1988, you may request a copy of all personal information we hold about you, ask for it to be corrected, or ask for it to be deleted (subject to the seven-year tax retention requirement). Email <a href="mailto:concierge@noctis.com.au">concierge@noctis.com.au</a> or write to us at the Walsh Bay address below. We respond within five business days.</p>

<h2>6. Cookies.</h2>
<p>This site sets one cookie: a session cookie used to remember whether you have closed the FAQ panels. We do not use tracking cookies, advertising cookies, or third-party analytics cookies.</p>

<h2>7. Updates.</h2>
<p>If we change this policy, the date at the top of this page will change with it. Substantive changes will be communicated to current guests by email.</p>
""",
    },
    "terms": {
        "title": "Terms of service",
        "deck": "The agreement that applies when you book a car.",
        "updated": "Last updated 14 February 2026",
        "body": """
<h2>1. Who we are.</h2>
<p>Noctis Automotive Pty Ltd (ACN 638 472 901), trading as Noctis, registered in New South Wales, with its principal place of business at Pier 6/7, Walsh Bay, Sydney NSW 2000.</p>

<h2>2. The agreement.</h2>
<p>Each reservation is a separate agreement between you and Noctis Automotive Pty Ltd, governed by the rental contract you sign on delivery. These terms apply to your use of the website and our concierge service prior to that contract being signed.</p>

<h2>3. Eligibility.</h2>
<p>You must be at least 30 years of age (35 for the McLaren 750S and Ferrari Purosangue), hold a full Australian or international driver's licence held continuously for at least three years, and have a clean driving record (no major offences in the last five years).</p>

<h2>4. Reservations.</h2>
<p>Submitting an inquiry through the website does not create a reservation. A reservation is confirmed only when you have received written confirmation from a member of our concierge team and your deposit has cleared. We reserve the right to decline any inquiry without explanation.</p>

<h2>5. Pricing &amp; deposits.</h2>
<p>All prices are in Australian dollars and inclusive of GST. A 30% deposit is held at the time of confirmation. Final settlement, including any kilometre overage, fuel charge, or fines, is processed by wire or card within seven days of the conclusion of the reservation.</p>

<h2>6. Cancellation.</h2>
<p>Full refund up to 48 hours before the scheduled delivery time. Inside 48 hours, the deposit is held against a future reservation, valid for 12 months. If we cancel for any reason within our control, you receive a full refund and a complimentary day on your next reservation.</p>

<h2>7. Damage &amp; insurance.</h2>
<p>Each vehicle is fully insured for the duration of your reservation. You are responsible for the standard excess (between A$5,000 and A$15,000 depending on vehicle) in the event of damage caused while the car is in your custody. Excess waiver is available on weekly bookings of the Spectre and Purosangue, and on request for other vehicles.</p>

<h2>8. Permitted use.</h2>
<p>The vehicle may be driven only by the named driver(s) listed on the rental contract. The vehicle may not be driven on unsealed roads, on race circuits, or outside the agreed area without our prior written consent. The vehicle may not be sub-let, used to carry paid passengers, or used in connection with any commercial filming or photography without prior written consent.</p>

<h2>9. Liability.</h2>
<p>To the maximum extent permitted by Australian Consumer Law, our liability is limited to the value of the reservation. Nothing in these terms excludes any guarantee that cannot be excluded under the ACL.</p>

<h2>10. Governing law.</h2>
<p>These terms are governed by the laws of New South Wales, Australia.</p>
""",
    },
    "responsible-driving": {
        "title": "Responsible driving",
        "deck": "What we ask of every guest behind the wheel.",
        "updated": "Last updated 14 February 2026",
        "body": """
<h2>An understanding, not a contract.</h2>
<p>This is not legal language. Those terms are <a href="terms.html">over here</a>. This page is the one we ask every guest to actually read.</p>

<h2>Drive within the law.</h2>
<p>Every car in our fleet is capable of speeds and accelerations that are illegal on every public road in Australia. The fact that they can do those things does not mean you should. Speed cameras, mobile cameras, average-speed cameras, and unmarked cars are everywhere on our roads. Fines are paid by you and forwarded to you within seven days of the offence.</p>

<h2>Drive within yourself.</h2>
<p>Many of our guests have driven cars like ours before, and many have not. The DB12, the McLaren, the Purosangue — they will hide their pace at low speeds and reveal it suddenly. Every car comes with a thirty-minute briefing from our delivery driver. Use it. Ask whatever you like. We do not assume.</p>

<h2>Drive within Sydney.</h2>
<p>The Sydney roads we have written about — the Old Pacific Highway, Royal National Park, West Head, the Cahill Expressway — were built before most of these cars existed. They will reward you, but they will also surprise you. Wet sandstone is slippery. Wallabies happen at dawn. The Sea Cliff Bridge has crosswinds.</p>

<h2>Three rules we will not bend on.</h2>
<p><strong>No alcohol.</strong> Zero blood alcohol when you are driving any car of ours. If you have been drinking, call us and we will collect the car at no charge. We do this once per reservation without question.</p>
<p><strong>No racing, no track use.</strong> Our cars are not insured for circuit driving and they will not be used for it. If you would like a track day in a similar car, we know three operators and we are happy to introduce you.</p>
<p><strong>No phones in your hand.</strong> Use the car's CarPlay or hand it to a passenger. Australia's mobile-phone laws are strict and the cameras have improved.</p>

<h2>If something happens.</h2>
<p>Call us first. The number is on the key fob, on the dashboard, and on the rental contract. We answer 24 hours. If anyone is hurt, call 000 first, then us. Police in NSW require attendance at any accident with injury. We will help you with the rest.</p>

<h2>Thank you.</h2>
<p>Most of this is obvious. We write it down because we have learned that most luxury rental businesses pretend it isn't, and that has always seemed strange to us. Drive well, drive home, and tell us what you noticed about the car. That last part is the most important.</p>
""",
    },
}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} · Noctis Sydney</title>
<meta name="description" content="{deck}" />
<meta name="theme-color" content="#0A0A0A" />
<link rel="canonical" href="https://noctis.com.au/legal/{slug}.html" />
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%230A0A0A'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='central' text-anchor='middle' font-family='Georgia,serif' font-size='42' font-style='italic' fill='%23F5F1EA'%3EN%3C/text%3E%3C/svg%3E" />
<meta name="robots" content="index, follow" />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />

<style>
:root{{--ink:#0A0A0A;--surface:#111;--cream:#F5F1EA;--muted:#8C8576;--subtle:#5A564F;--accent:#6B0F1A;--line:#1F1E1B}}
*{{box-sizing:border-box}}
html,body{{background:var(--ink);color:var(--cream);margin:0;padding:0}}
body{{font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.font-serif{{font-family:'Fraunces',serif}}
.eyebrow{{font-size:11px;text-transform:uppercase;letter-spacing:0.22em;color:var(--muted)}}
a{{color:var(--cream)}}
.container{{max-width:1200px;margin:0 auto;padding:0 24px}}
@media(min-width:768px){{.container{{padding:0 40px}}}}

.noctis-nav{{position:fixed;top:0;left:0;right:0;z-index:50;backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);background:rgba(10,10,10,0.7);border-bottom:1px solid var(--line)}}
.noctis-nav-inner{{max-width:1280px;margin:0 auto;padding:0 24px;height:72px;display:flex;align-items:center;justify-content:space-between}}
@media(min-width:768px){{.noctis-nav-inner{{padding:0 40px}}}}
.noctis-nav a.link{{color:rgba(245,241,234,0.85);text-decoration:none;font-size:14px;transition:color .2s}}
.noctis-nav a.link:hover{{color:var(--cream)}}
.noctis-nav .links{{display:none;gap:40px}}
@media(min-width:900px){{.noctis-nav .links{{display:flex}}}}

.btn-primary{{display:inline-block;background:var(--accent);color:var(--cream);padding:10px 20px;font-size:13px;text-transform:uppercase;letter-spacing:0.16em;text-decoration:none;transition:background .2s}}
.btn-primary:hover{{background:#821426}}
.btn-ghost{{display:inline-block;color:rgba(245,241,234,0.9);border-bottom:1px solid rgba(245,241,234,0.35);padding-bottom:4px;text-decoration:none;font-size:14px}}

.legal-hero{{padding:160px 0 64px;border-bottom:1px solid var(--line);text-align:center}}
.legal-hero h1{{font-family:'Fraunces',serif;font-size:clamp(40px,6vw,68px);line-height:1.05;letter-spacing:-0.028em;margin:0 0 24px;color:var(--cream)}}
.legal-hero .deck{{font-size:18px;line-height:1.6;color:rgba(245,241,234,0.7);max-width:46ch;margin:0 auto 16px}}
.legal-hero .updated{{color:var(--muted);font-size:12px;letter-spacing:0.1em;text-transform:uppercase}}

.legal-body{{max-width:760px;margin:0 auto;padding:80px 24px 96px;font-size:16px;line-height:1.75;color:rgba(245,241,234,0.78)}}
.legal-body h2{{font-family:'Fraunces',serif;font-size:22px;font-weight:500;letter-spacing:-0.018em;color:var(--cream);margin:48px 0 16px;line-height:1.2}}
.legal-body h2:first-child{{margin-top:0}}
.legal-body p{{margin:0 0 20px}}
.legal-body strong{{color:var(--cream);font-weight:500}}
.legal-body a{{color:var(--cream);text-decoration:underline;text-decoration-color:rgba(245,241,234,0.3);text-underline-offset:3px}}
.legal-body a:hover{{text-decoration-color:var(--cream)}}

.legal-foot{{max-width:760px;margin:0 auto;padding:0 24px 96px;text-align:center}}
.legal-foot p{{color:var(--muted);font-size:12px;letter-spacing:0.04em;line-height:1.6;margin:0}}

footer{{border-top:1px solid var(--line);padding:64px 0;text-align:center}}
footer .name{{font-family:'Fraunces',serif;font-size:32px;letter-spacing:-0.03em}}
footer p{{margin-top:12px;color:var(--muted);font-size:12px}}
</style>
</head>
<body>

<header class="noctis-nav">
  <nav class="noctis-nav-inner">
    <a href="../index.html" style="display:flex;align-items:center;gap:10px;text-decoration:none;">
      <span class="font-serif" style="font-size:26px;color:var(--cream);letter-spacing:-0.03em;">Noctis</span>
    </a>
    <div class="links">
      <a href="../index.html#fleet" class="link">The Fleet</a>
      <a href="../index.html#standard" class="link">The Standard</a>
      <a href="../index.html#experience" class="link">Experience</a>
      <a href="../journal/index.html" class="link">Journal</a>
    </div>
    <a href="../index.html#reserve" class="btn-primary">Reserve</a>
  </nav>
</header>

<section class="legal-hero">
  <div class="container">
    <p class="eyebrow" style="margin:0 0 24px;">House documents</p>
    <h1>{title}</h1>
    <p class="deck">{deck}</p>
    <p class="updated">{updated}</p>
  </div>
</section>

<div class="legal-body">
{body}
</div>

<div class="legal-foot">
  <p>Noctis Automotive Pty Ltd · ACN 638 472 901<br />
  Pier 6/7, Walsh Bay, Sydney NSW 2000, Australia<br />
  <a href="mailto:concierge@noctis.com.au">concierge@noctis.com.au</a></p>
</div>

<footer>
  <div class="container">
    <p class="name">Noctis</p>
    <p>© 2026 Noctis Automotive Pty Ltd · Sydney, Australia</p>
  </div>
</footer>

</body>
</html>
"""


def main():
    for slug, p in PAGES.items():
        out = HEAD.format(slug=slug, **p)
        path = LEGAL / f"{slug}.html"
        path.write_text(out)
        print(f"  ✓ {slug}.html")


if __name__ == "__main__":
    main()
