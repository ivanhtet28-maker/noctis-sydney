#!/usr/bin/env python3
"""Build the three journal articles from data."""
from pathlib import Path

ROOT = Path(__file__).parent.parent
JOURNAL = ROOT / "journal"

ENTRIES = {
    "db12-harbour-bridge": {
        "tag": "Essay",
        "issue": "No. 03",
        "date": "04 March 2026",
        "readtime": "6 min read",
        "title": "Why a DB12 is wasted <em>on the Harbour Bridge.</em>",
        "title_plain": "Why a DB12 is wasted on the Harbour Bridge",
        "deck": "A note on the difference between a road that asks for speed and one that asks for restraint.",
        "byline": "Tom Fairbairn",
        "byline_role": "Head of Fleet, Noctis",
        "body": """
<p>Every Tuesday, somebody takes one of our DB12s across the Harbour Bridge.</p>

<p>It is not, on paper, the wrong choice. The bridge is photogenic. The car is photogenic. From the southern pylon to North Sydney is exactly the length of a song. Most guests, on collection, want to be seen — which is the one thing a DB12 in Iridescent Emerald, hood down, on the apex of the Cahill, will reliably accomplish.</p>

<p>And yet. We have been quietly steering people away from the Bridge for three years now. The reason is simple, and worth saying clearly:</p>

<p class="pull">The DB12 is not a car for being looked at. It is a car for looking out of.</p>

<p>The Harbour Bridge is a beautiful piece of infrastructure, but it is also — and there is no polite way to put this — a four-lane traffic artery with a 70 km/h limit and a camera every 200 metres. You cannot drive a DB12 on it. You can only sit in one, in third gear, with your foot light on the throttle, while the V8 does the very thing it was designed not to do: idle.</p>

<h2>What a great road actually asks for</h2>

<p>The DB12 was designed around something specific. Aston call it "Cygnet" cornering — a reference, mostly inside-jokey, to a stretch of road outside Aston's Gaydon factory where every chassis is signed off. The car wants a road with an arc to it. A road where, between corners, you can let the engine go up the rev range without immediately running into another car, and where, in a corner, you can let the rear axle do the slight unloading thing it does so beautifully.</p>

<p>The Harbour Bridge offers none of this. What it offers is a straight line, a posted limit, and a postcard view. You can have those things in a Toyota.</p>

<p>The instruction we now give every concierge: <em>if your guest's plan is to drive a DB12 over the Harbour Bridge, please very gently re-route them through the Eastern Distributor and out toward Mosman first.</em></p>

<h2>Three roads we'd rather they took</h2>

<p>This is not advice for everyone. It is advice for someone who has paid roughly a thousand pounds a day for a particular kind of mechanical pleasure, and who deserves, frankly, to actually receive it.</p>

<p><strong>Mona Vale Road, between Terrey Hills and Mona Vale.</strong> Forty-three minutes from Walsh Bay. Sweeping, sandstone-cut, mostly empty before nine on a weekday. The DB12 settles into a rhythm here that it cannot find on the Bridge. Take it once each way and stop for coffee at Whale Beach. (Avoid the school holidays.)</p>

<p><strong>The Old Pacific Highway, between the M1 turnoff and the river.</strong> A motorbike road, technically — but the surface is good, the cambers are honest, and the early morning light through the eucalyptus is the closest Sydney gets to Tuscan. About forty minutes from the city if you leave before the school run.</p>

<p><strong>Royal National Park, the ridge from Sutherland to Audley and back.</strong> The slowest of the three on the clock, but the one most guests come back asking for again. The road is narrow, the surface is patchy, and the speed limits are inconveniently low. None of which matters. The DB12 will spend the whole loop in third gear and you will spend the whole loop happy.</p>

<h2>What the Bridge is for</h2>

<p>None of this is to say the Harbour Bridge is a bad place to drive. It is, in fact, an exceptionally good place to drive — but in a different car, and at a different time. We tend to recommend it for the Spectre, because the Spectre is built around the experience of being a passenger in your own car, and the bridge is essentially a passenger experience.</p>

<p>For the DB12, save the Bridge for the way home. Drive the loop properly, in the mountains or by the sea, where the car can be what it is. Then, on the way back, when you've made your peace with what the engine can do, take the Bridge at a calm seventy and let the rest of Sydney watch.</p>

<p>That is what the Bridge is for. Not the drive. The arrival.</p>
""",
    },
    "breakfast-drives": {
        "tag": "Guide",
        "issue": "No. 02",
        "date": "18 February 2026",
        "readtime": "9 min read",
        "title": "The three best breakfast drives <em>out of Sydney.</em>",
        "title_plain": "The three best breakfast drives out of Sydney",
        "deck": "Old Pacific Highway before 7. West Head via Akuna Bay. Royal National Park when the season turns.",
        "byline": "The Concierge Desk",
        "byline_role": "Walsh Bay, Sydney",
        "body": """
<p>This is the list we give over the phone, when a guest asks where to take a car at six in the morning and would like a coffee at the end of it. Three drives, all under ninety minutes from Walsh Bay, all repeatable on a weekday before traffic. Distances and timings are honest.</p>

<h2>01 — The Old Pacific Highway, before seven.</h2>

<p>From the city, take the M1 north and exit at Berowra. The Old Pacific Highway picks up shortly after — a fifteen-kilometre stretch of bitumen winding alongside the Hawkesbury River, cut into sandstone cliffs and lit, at this hour, by light coming up sideways through gum trees.</p>

<p>The road is technically a motorbike road. On a Sunday, between nine and three, it will be full of them. On a Tuesday at six-thirty, it is yours. The surface is excellent. The cambers are kind. There are three or four corners that will reveal whatever car you are in.</p>

<p>Stop at the Pie in the Sky lookout — a roadhouse, of all things, that does a flat white and a sausage roll roughly the size of a small dog. Not luxurious. Wonderful.</p>

<p><strong>Distance:</strong> 84 km from Walsh Bay return. <strong>Time:</strong> 90 minutes including the stop. <strong>Best for:</strong> the 911 GT3, the DB12.</p>

<h2>02 — West Head via Akuna Bay.</h2>

<p>Slightly closer to the city, slightly less obvious. From Mona Vale, head west into Ku-ring-gai Chase National Park, drop down into Akuna Bay (a small marina, mostly silent at dawn), then climb back out toward West Head. The road is narrower than the Old Pacific. The corners are tighter. The forest closes in over the road, and at the end of West Head Road there is a lookout pointing south, across Pittwater, with the Barrenjoey lighthouse pinned to the horizon.</p>

<p>You will share this road with kookaburras and the occasional cyclist. Drive accordingly.</p>

<p>For breakfast, double back to the bakery at Avalon — Bookoccino, three doors up, opens at six-thirty and makes the only proper croissant north of the Bridge. Take it with you and eat it on the sand at Whale Beach.</p>

<p><strong>Distance:</strong> 78 km return. <strong>Time:</strong> 100 minutes. <strong>Best for:</strong> the Spectre, the Purosangue.</p>

<h2>03 — Royal National Park, when the season turns.</h2>

<p>This one is for autumn — late March through May — when the eucalyptus drops its red leaves over the road and the morning fog lifts off the Hacking River in the half-hour after sunrise. From the city, take the F6 south to Sutherland, then drop into the park at Audley.</p>

<p>The loop runs Audley → Sir Bertram Stevens Drive → Lady Wakehurst Drive → Bundeena → back. Slow corners, low limits, almost no traffic before nine. This is not a fast drive. It is a meditative one. The Spectre, in particular, will thank you for taking it here.</p>

<p>Coffee at Garie Beach kiosk if it is open (mornings only, weather-dependent). Otherwise, the cafe at Stanwell Park overlooking the coast. From there, you can climb back to the city via Sea Cliff Bridge and Bald Hill, which is the closest thing Sydney has to Big Sur.</p>

<p><strong>Distance:</strong> 130 km return. <strong>Time:</strong> 2 hours, with the coast detour. <strong>Best for:</strong> any car you own.</p>

<h2>A note on timing.</h2>

<p>All three drives go cold somewhere around 8:15 AM, when the school traffic starts and the cyclists wake up. Be back in the city by nine, or commit to a longer day. The middle option — back at noon, lunch in Mosman — is rarely worth it. Better to be home by nine, or out until five.</p>
""",
    },
    "badges-come-off": {
        "tag": "Conversation",
        "issue": "No. 01",
        "date": "30 January 2026",
        "readtime": "12 min read",
        "title": "Our head of fleet <em>on why badges come off.</em>",
        "title_plain": "Our head of fleet on why badges come off",
        "deck": "Tom Fairbairn — who has run the workshop since the beginning — on quiet luxury, the British art of underplaying, and the reason every Noctis car wears the same nameplate.",
        "byline": "In conversation with Tom Fairbairn",
        "byline_role": "Walsh Bay · 30 January 2026",
        "body": """
<p><strong>Q. Every car in the Noctis fleet is unbadged. Why?</strong></p>

<p>A. We get asked that a lot. The honest answer is that the badges came off because we couldn't agree on what to do with them. We had a Spectre come in the first week we opened, and it had a dealer plate on the back, and a Greenwich Rolls-Royce sticker, and a Bridgestone branded valve cap. None of which the manufacturer put there. We took those off. And once you start doing that, it becomes hard to know where to stop.</p>

<p><strong>Q. So why not put your own badges on?</strong></p>

<p>A. We thought about it. There was a weekend in 2021 where we genuinely considered a small etched 'N' on the rear quarter glass. Then we went out for dinner and somebody at the next table said, very loudly, "I love that little Bentley logo." And the Bentley in question was twenty years old, and the logo had nothing to do with anyone at the table, but it gave him license to talk about it. We decided we didn't want to give anyone license to talk about our cars.</p>

<p class="pull">A car you can't see the badge on is a car the right people will recognise anyway.</p>

<p><strong>Q. The line on the website — "modern-classic, immaculate, unbadged, booked by invitation" — what does "booked by invitation" mean in practice?</strong></p>

<p>A. It means we ask for a referral, or we don't. The form on the website goes through to one of three of us. About a third of the requests we get, we politely decline — usually because the timing doesn't work, sometimes because the request itself has told us we'd be a bad fit. We're not trying to be rude. We're just trying to keep the experience consistent for the people who do book.</p>

<p><strong>Q. The fortnightly servicing — is that real?</strong></p>

<p>A. Yes. Every car in the fleet comes through the workshop every fourteen days. We rotate them out at 18,000 km, regardless of condition. The maths on this is brutal — it's the single largest line item we have — but we worked out very early on that the difference between a luxury car at 5,000 km and the same car at 25,000 km is everything. Steering weight, the way the doors close, the smell. We sell that difference, and we will not let it slip.</p>

<p><strong>Q. Walsh Bay is a strange place for a workshop.</strong></p>

<p>A. It's an excellent place for a workshop. We're in one of the original wool stores at Pier 6/7 — the building has fifteen-foot ceilings, brick walls, an old goods lift that we still use for the McLaren. The light through the windows in the afternoon, off the harbour, is the kind of light you can't get anywhere else in Sydney. People come in to drop off keys and stay for forty-five minutes.</p>

<p>Also, it means our drivers can walk out the front door and be on the Cahill Expressway in nine minutes, which we have measured.</p>

<p><strong>Q. The fleet is small. Do you ever get asked for things you don't have?</strong></p>

<p>A. Constantly. We've been asked for a Pagani, a 250 SWB, a Range Rover Classic. The first we said no to. The second we tried very hard for and failed. The third we sourced for one weekend in 2023 and have been trying to get back ever since. We will probably add one more car each year, very slowly. The fleet is meant to be a list of opinions, not a catalogue.</p>

<p><strong>Q. What's the next opinion?</strong></p>

<p>A. I'm not going to tell you. But it's quieter than people would guess.</p>
""",
    },
}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title_plain} · The Noctis Journal</title>
<meta name="description" content="{deck}" />
<meta name="theme-color" content="#0A0A0A" />
<link rel="canonical" href="https://noctis.com.au/journal/{slug}.html" />
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%230A0A0A'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='central' text-anchor='middle' font-family='Georgia,serif' font-size='42' font-style='italic' fill='%23F5F1EA'%3EN%3C/text%3E%3C/svg%3E" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{title_plain} · The Noctis Journal" />
<meta property="og:description" content="{deck}" />
<meta property="og:image" content="https://noctis.com.au/images/sydney-hero.jpg" />
<meta name="twitter:card" content="summary_large_image" />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />

<style>
:root{{--ink:#0A0A0A;--surface:#111;--cream:#F5F1EA;--muted:#8C8576;--subtle:#5A564F;--accent:#6B0F1A;--line:#1F1E1B;}}
*{{box-sizing:border-box}}
html,body{{background:var(--ink);color:var(--cream);margin:0;padding:0}}
body{{font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.font-serif{{font-family:'Fraunces',serif}}
.eyebrow{{font-size:11px;text-transform:uppercase;letter-spacing:0.22em;color:var(--muted)}}
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
.btn-ghost{{display:inline-block;color:rgba(245,241,234,0.9);border-bottom:1px solid rgba(245,241,234,0.35);padding-bottom:4px;text-decoration:none;font-size:14px;transition:border-color .3s}}

.article-hero{{padding:160px 0 64px;border-bottom:1px solid var(--line);max-width:880px;margin:0 auto;text-align:center}}
.article-hero .meta{{display:flex;justify-content:center;gap:16px;margin-bottom:32px;color:var(--muted);font-size:12px;letter-spacing:0.15em;text-transform:uppercase}}
.article-hero h1{{font-family:'Fraunces',serif;font-size:clamp(40px,6vw,68px);line-height:1.05;letter-spacing:-0.028em;margin:0 0 32px;color:var(--cream)}}
.article-hero h1 em{{font-style:italic;font-weight:300}}
.article-hero .deck{{font-size:18px;line-height:1.55;color:rgba(245,241,234,0.7);max-width:46ch;margin:0 auto}}
.article-byline{{padding:32px 0;text-align:center;border-bottom:1px solid var(--line);color:var(--muted);font-size:13px;letter-spacing:0.04em}}
.article-byline strong{{color:var(--cream);font-weight:500;letter-spacing:0}}

.article-body{{max-width:680px;margin:0 auto;padding:80px 24px 80px;font-family:'Fraunces',serif;font-size:20px;line-height:1.65;color:rgba(245,241,234,0.85);font-weight:300}}
.article-body h2{{font-family:'Fraunces',serif;font-size:28px;font-style:italic;font-weight:300;letter-spacing:-0.022em;color:var(--cream);margin:64px 0 24px;line-height:1.2}}
.article-body p{{margin:0 0 28px}}
.article-body p.pull{{font-size:26px;line-height:1.3;color:var(--cream);font-style:italic;border-left:2px solid var(--accent);padding:8px 0 8px 28px;margin:48px 0}}
.article-body strong{{font-weight:500;color:var(--cream)}}
.article-body em{{font-style:italic}}

.article-foot{{max-width:680px;margin:0 auto;padding:0 24px 96px;text-align:center}}
.article-foot p{{color:var(--muted);font-size:13px;letter-spacing:0.04em;margin:0 0 32px}}

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
      <a href="index.html" class="link" style="color:var(--cream);">Journal</a>
    </div>
    <a href="../index.html#reserve" class="btn-primary">Reserve</a>
  </nav>
</header>

<article>
  <header class="article-hero">
    <div class="container">
      <div class="meta">
        <span>{tag}</span><span>·</span><span>{issue}</span><span>·</span><span>{date}</span>
      </div>
      <h1>{title}</h1>
      <p class="deck">{deck}</p>
    </div>
  </header>

  <div class="article-byline">
    <span>By <strong>{byline}</strong> · {byline_role}</span>
  </div>

  <div class="article-body">
{body}
  </div>

  <div class="article-foot">
    <p>{readtime} · Filed under <em>{tag}</em></p>
    <a href="index.html" class="btn-ghost">More from the Journal &nbsp;→</a>
  </div>
</article>

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
    for slug, e in ENTRIES.items():
        out = HEAD.format(slug=slug, **e)
        path = JOURNAL / f"{slug}.html"
        path.write_text(out)
        print(f"  ✓ {slug}.html")


if __name__ == "__main__":
    main()
