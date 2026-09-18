#!/usr/bin/env python3
"""
Generates the eight project pages from one template.

The pages were previously eight near-identical hand-maintained files, so a
change to the nav or footer meant eight edits and the inevitable drift. Edit the
PROJECTS list below and re-run:

    python3 tools/build-project-pages.py

It writes projects/*.html. Nothing else in the site depends on it at runtime —
the output is plain static HTML, exactly as before.
"""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "projects"
SITE = "https://tryxis.github.io/portfolio"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} &mdash; David Butterworth</title>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="{meta}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} — David Butterworth">
<meta property="og:description" content="{meta}">
<meta property="og:image" content="{site}/images/covers/{cover}">
<meta property="og:url" content="{site}/projects/{slug}.html">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="icon" href="../images/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/project.css">
</head>
<body>

<a href="#project-main" class="skip-link">Skip to content</a>

<nav class="nav">
  <div class="nav-inner">
    <a href="../index.html" class="nav-brand">david<span class="dot">.</span>butterworth</a>
    <ul class="nav-links" id="navLinks">
      <li><a href="../index.html">Home</a></li>
      <li><a href="../index.html#section-portfolio">Work</a></li>
      <li><a href="../index.html#section-resume">CV</a></li>
      <li><a href="../index.html#section-about">About</a></li>
      <li><a href="../index.html#section-contact">Contact</a></li>
    </ul>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">&#9776;</button>
  </div>
</nav>

<main id="project-main" class="project-hero">
  <div class="wrap project-grid">
    <div class="project-media">
      <img src="../images/covers/{hero}" alt="{alt}" width="1400" height="875">
    </div>
    <div class="project-info">
      <span class="project-back"><a href="../index.html#section-portfolio">&larr; Back to work</a></span>
      <h1>{title}</h1>
      <p class="project-tagline">{tagline}</p>
{description}
      <div class="project-tags">
        {tags}
      </div>
      <div class="project-actions">
{actions}
      </div>
    </div>
  </div>
</main>

<section class="section project-notes" id="build-notes">
  <div class="wrap">
    <div class="notes-grid">
      <div class="notes-main">
        <h2>Build notes</h2>
{notes}
      </div>
      <aside class="notes-meta" aria-label="Project details">
        <dl>
{meta_rows}
        </dl>
      </aside>
    </div>

    <nav class="project-pager" aria-label="Other projects">
      <a class="pager-prev" href="./{prev_slug}.html"><span class="pager-label">&larr; Previous</span><span class="pager-title">{prev_title}</span></a>
      <a class="pager-next" href="./{next_slug}.html"><span class="pager-label">Next &rarr;</span><span class="pager-title">{next_title}</span></a>
    </nav>
  </div>
</section>

<footer>
  <div class="wrap footer-inner">
    <p>&copy; 2026 David Butterworth</p>
    <div class="social-links">
      <a href="https://www.linkedin.com/in/david-butterworth-5b9950203/">LinkedIn</a>
      <a href="https://github.com/Tryxis">GitHub</a>
    </div>
  </div>
</footer>

<script src="../js/main.js" defer></script>

<!-- 100% privacy-first analytics -->
<script async defer src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
<noscript><img src="https://queue.simpleanalyticscdn.com/noscript.gif" alt="" referrerpolicy="no-referrer-when-downgrade" /></noscript>

</body>
</html>
"""


def btn(href, label, primary=False, title=""):
    cls = "btn btn-primary" if primary else "btn btn-ghost"
    return (
        '        <a href="{href}" class="{cls}" target="_blank" rel="noopener" '
        'aria-label="{label} for {title} (opens in a new tab)">{label}</a>'
    ).format(href=href, cls=cls, label=label, title=title)


PROJECTS = [
    dict(
        slug="bones_and_bolters",
        title="Bones and Bolters",
        cover="bones-and-bolters.svg",
        alt="Bones and Bolters cover art",
        tagline="Club site for a Kill Team group",
        meta="Bones and Bolters — a static club site for a local Kill Team group, with a crew roster and a filterable campaign calendar.",
        tags=['<span class="tag">Site</span>'],
        description=[
            "A home on the web for a local Kill Team group: who runs it, and what is coming up. "
            "The crew roster introduces the people you will actually meet across the table, and the "
            "campaign calendar lists game nights and tournaments so nobody has to scroll back through "
            "a chat thread to find a date.",
            "Built and hosted by me for the group, and deliberately kept to plain HTML, CSS and "
            "JavaScript so anyone can open the file and change a date without installing anything.",
        ],
        actions=[
            ("https://tryxis.github.io/bones-and-bolters/", "Live site", True),
            ("https://github.com/Tryxis/Bones-and-Bolters", "View Repo", False),
        ],
        notes=[
            ("No framework, no build step",
             "Three files &mdash; one HTML, one stylesheet, one script. The whole thing is served straight "
             "from GitHub Pages. For a site that changes when someone adds an event, a build pipeline "
             "would be a tax on every edit and would give nothing back."),
            ("A carousel without a carousel library",
             "The crew roster is a horizontally scrollable row with dot indicators. The dots are generated "
             "from whatever members exist in the markup, and the active one is worked out from scroll "
             "position on each frame, throttled through <code>requestAnimationFrame</code>. Adding a new "
             "member means adding one block of HTML &mdash; the navigation follows on its own."),
            ("Calendar that filters in place",
             "Events carry a <code>data-type</code> of casual or tournament and the filter buttons toggle "
             "visibility against it. Same idea as the filters on this portfolio, which is where it came from."),
        ],
        meta_rows=[("Stack", "HTML, CSS, vanilla JavaScript"),
                   ("Hosting", "GitHub Pages"),
                   ("Role", "Built it and keep it running"),
                   ("Status", "Live")],
    ),
    dict(
        slug="reckoner",
        title="Reckoner",
        cover="reckoner.svg",
        alt="Reckoner cover art",
        tagline="Attack-sequence probability calculator",
        meta="Reckoner — an offline-capable attack sequence probability calculator for tabletop wargames, installable as a phone app.",
        tags=['<span class="tag">App</span>'],
        description=[
            "Put in a weapon profile and a target, toggle the keywords in play, and Reckoner gives you the "
            "rolls you need, the damage you can expect, and how many models are likely to fall. It answers "
            "the question every wargamer asks mid-turn &mdash; <em>is this actually worth shooting at?</em> "
            "&mdash; faster than working it out on paper.",
            "It installs to a phone home screen and works with no signal, because the place you need it is a "
            "club table, not a desk.",
        ],
        actions=[
            ("https://tryxis.github.io/Reckoner/", "Open app", True),
            ("https://github.com/Tryxis/Reckoner", "View Repo", False),
        ],
        notes=[
            ("Closed form where it can be, simulation where it can&#8217;t",
             "The hit &rarr; wound &rarr; save chain is solved algebraically, so those numbers are exact and "
             "instant. <em>Models slain</em> is not: damage spills across models, and rules like Feel No Pain "
             "and damage reduction interact awkwardly with that spill. So the app runs a Monte Carlo pass for "
             "the slain distribution and reports it as a probability spread rather than a single misleading "
             "average."),
            ("Keywords as data, not branches",
             "Around forty keywords &mdash; Sustained Hits, Lethal Hits, Anti-X, Twin-linked, cover, Feel No "
             "Pain and the rest &mdash; are declared in one table, along with which of them are mutually "
             "exclusive and which carry a numeric value. Adding a new rule is an entry in that table rather "
             "than another branch through the maths."),
            ("One folder, two products",
             "The <code>www/</code> folder is the entire app: four files, no dependencies, no build step. "
             "That is what lets the same folder be published to GitHub Pages by an Action <em>and</em> wrapped "
             "as an iOS or Android app with Capacitor, without a single line changing between them."),
            ("Offline by design",
             "A service worker precaches every file and serves cache-first, so the app opens instantly and "
             "keeps working in a venue with no reception. The cache name is versioned, which is what makes an "
             "already-installed copy pick up a new release."),
        ],
        meta_rows=[("Stack", "Vanilla JavaScript, PWA (manifest + service worker), Capacitor"),
                   ("Deploy", "GitHub Actions to GitHub Pages"),
                   ("Dependencies", "None at runtime"),
                   ("Status", "Live")],
    ),
    dict(
        slug="dungeon_helper",
        title="Davey&#8217;s Dungeon Helper",
        cover="dungeon-helper.svg",
        alt="Davey&#8217;s Dungeon Helper cover art",
        tagline="Node.js Discord bot",
        meta="Davey's Dungeon Helper — a Discord bot for D&D 5e groups: dice rolling, spell lookup, conditions and rules reminders.",
        tags=['<span class="tag">Bot</span>'],
        description=[
            "A handy toolkit for Dungeons &amp; Dragons players, conveniently accessible within Discord. It "
            "handles dice-rolling commands &mdash; including commentary on certain rolls &mdash; and gives "
            "instant access to spells, conditions and rules within just two prompts.",
            "It isn&#8217;t hosted outside of Discord at the moment, so it&#8217;s limited to servers it&#8217;s "
            "been added to. The repo has details on how to run it in your own server.",
        ],
        actions=[("https://github.com/Tryxis/Dungeon-Helper-Bot", "View Repo", False)],
        notes=[
            ("Slash commands, not message parsing",
             "Everything is a registered slash command, so Discord does the argument validation and players "
             "get autocomplete and inline help without the bot needing permission to read message content."),
            ("The reference data is local",
             "Spell text ships with the bot as JSON rather than being fetched from an API at request time. "
             "A table that has stopped mid-combat to wait on someone else&#8217;s rate limit is a table that "
             "stops using the bot."),
            ("State that survives a restart",
             "The running counters are written back to disk, so a redeploy doesn&#8217;t quietly reset the "
             "numbers people have been building up all campaign."),
        ],
        meta_rows=[("Stack", "Node.js, discord.js v14"),
                   ("Data", "Local JSON spell reference"),
                   ("Hosting", "Self-hosted per server"),
                   ("Status", "Working, actively tinkered with")],
    ),
    dict(
        slug="delivery_davey",
        title="Delivery Davey",
        cover="delivery-davey.svg",
        alt="Delivery Davey cover art",
        tagline="Small driving and delivery prototype",
        meta="Delivery Davey — a small Unity driving prototype where parcels buy you speed and crashes take it away.",
        tags=['<span class="tag">Game</span>'],
        description=[
            "Zoom around a neighbourhood picking up and delivering packages as quickly as possible. Picking "
            "up packages generates speed, crashing loses it &mdash; so drive carefully!",
        ],
        actions=[("https://tryxis.itch.io/delivery-davey", "Play Me", True),
                 ("https://github.com/Tryxis/delivery-davey", "View Repo", False)],
        notes=[
            ("The risk/reward loop is the whole game",
             "Speed is the score and the hazard at once. Collecting a package boosts you; clipping the scenery "
             "drops you back down. One tuned number in each direction is enough to make a player decide "
             "whether that shortcut is worth it, which is more interesting than a timer."),
            ("Kept deliberately small",
             "Three scripts: one drives the car, one handles pickup and drop-off triggers, one follows the "
             "camera. Every tuning value is exposed in the Unity inspector, so balancing the thing is done by "
             "playing it rather than by recompiling."),
        ],
        meta_rows=[("Engine", "Unity (2D)"),
                   ("Language", "C#"),
                   ("Published", "itch.io"),
                   ("Status", "Prototype, playable")],
    ),
    dict(
        slug="downhill_davey",
        title="Downhill Davey",
        cover="downhill-davey.svg",
        alt="Downhill Davey cover art",
        tagline="Small platform prototype",
        meta="Downhill Davey — a small Unity physics game about flipping and tricking your way down a mountain.",
        tags=['<span class="tag">Game</span>'],
        description=[
            "Flip and trick your way down Mount Muckle. Bonking your head will send you back to the top.",
        ],
        actions=[("https://tryxis.itch.io/downhill-davey", "Play Me", True),
                 ("https://github.com/Tryxis/downhill-davey", "View Repo", False)],
        notes=[
            ("Physics does the animating",
             "The rider is a 2D rigidbody. Steering applies torque rather than setting a rotation, so landings, "
             "wipeouts and the satisfying wobble at the top of a jump all fall out of the physics rather than "
             "being hand-animated."),
            ("A crash rule you can feel",
             "A separate collider on the head turns a bad landing into an instant restart. Making the failure "
             "condition a body part rather than a health bar means players learn it in one go."),
        ],
        meta_rows=[("Engine", "Unity (2D physics)"),
                   ("Language", "C#"),
                   ("Published", "itch.io"),
                   ("Status", "Prototype, playable")],
    ),
    dict(
        slug="the_question",
        title="The Question",
        cover="the-question.svg",
        alt="The Question cover art",
        tagline="Interface-based quiz game",
        meta="The Question — a Unity pop culture quiz built so that new questions are authored as data rather than code.",
        tags=['<span class="tag">Game</span>'],
        description=[
            "Test your popular culture knowledge in rounds of multiple choice questions.",
        ],
        actions=[("https://tryxis.itch.io/the-question", "Play Me", True),
                 ("https://github.com/Tryxis/the-question", "View Repo", False)],
        notes=[
            ("Questions are data, not code",
             "Each question is a Unity ScriptableObject holding the prompt, four answers and the index of the "
             "right one. Writing a new round is filling in assets in the editor &mdash; no programmer needed, "
             "and no rebuild to change a typo in an answer."),
            ("One state machine drives the round",
             "The quiz script owns the whole cycle: draw a random unasked question, run the timer, lock the "
             "buttons on an answer, reveal the correct one, advance the progress bar, and hand over to the end "
             "screen when the pool runs dry."),
        ],
        meta_rows=[("Engine", "Unity"),
                   ("Language", "C#"),
                   ("Published", "itch.io"),
                   ("Status", "Prototype, playable")],
    ),
    dict(
        slug="stock_flock",
        title="Stock Flock",
        cover="stock-flock.svg",
        alt="Stock Flock cover art",
        tagline=".NET stocks and shares social platform",
        meta="Stock Flock — a .NET Web API backing a social platform for share portfolios, with Identity, JWT auth and EF Core.",
        tags=['<span class="tag">API</span>'],
        description=[
            "Backend endpoints to facilitate a social media style application to display stock portfolios. "
            "Operates against a SQL Server database, with authorisation handled via JWT.",
        ],
        actions=[("https://github.com/Tryxis/StocksApi", "View Repo", False)],
        notes=[
            ("Conventional layering, on purpose",
             "Controllers for accounts, stocks, portfolios and comments sit on top of repositories, with DTOs "
             "at the boundary so the EF entities never leak out of the API. It is the standard shape for a "
             "reason: anyone who has worked in a .NET codebase can find their way around it on the first read."),
            ("Identity and tokens",
             "ASP.NET Core Identity handles users and password rules; a token service issues JWTs and the API "
             "validates them as bearer tokens. Claims extensions keep &#8220;who is this request&#8221; out of "
             "the controllers."),
            ("Prices come from outside",
             "A dedicated service calls an external market data provider and maps the response onto the "
             "internal stock model, so a change of data supplier touches one class rather than every controller."),
        ],
        meta_rows=[("Stack", ".NET Web API, EF Core, SQL Server"),
                   ("Auth", "ASP.NET Identity + JWT bearer"),
                   ("Docs", "Swagger / OpenAPI"),
                   ("Status", "Backend complete")],
    ),
    dict(
        slug="zoom_and_broom",
        title="Zoom and Broom",
        cover="zoom-and-broom.svg",
        alt="Zoom and Broom cover art",
        tagline=".NET microservices application",
        meta="Zoom and Broom — a car auction site split into .NET microservices with RabbitMQ messaging, running under Docker.",
        tags=['<span class="tag">API</span>', '<span class="tag-status">In progress</span>'],
        description=[
            "Part of an on-going learning course to build an auction site for cars. Built with .NET 8, Next.js, "
            "IdentityServer and RabbitMQ, and currently running via Docker.",
        ],
        actions=[("https://github.com/Tryxis/zoom-and-broom", "View Repo", False)],
        notes=[
            ("Separate services, separate stores",
             "The auction service owns its data in Postgres; the search service keeps its own read-optimised "
             "copy in MongoDB. Each picks the database that suits its job instead of sharing one and pretending "
             "the services are independent."),
            ("Kept in step by messages",
             "Auction created, updated and deleted events are published to RabbitMQ and consumed by search. The "
             "event contracts live in a shared project so both ends compile against the same definition and a "
             "breaking change fails the build rather than production."),
            ("Identity as its own service",
             "Authentication is a service in its own right rather than a concern bolted onto each API, which is "
             "what makes adding the next service cheap."),
            ("The whole stack comes up with one command",
             "Postgres, MongoDB and RabbitMQ are all declared in docker-compose, so a clean machine goes from "
             "checkout to running system without a setup document."),
        ],
        meta_rows=[("Stack", ".NET 8, Next.js, RabbitMQ"),
                   ("Data", "PostgreSQL + MongoDB"),
                   ("Identity", "IdentityServer"),
                   ("Runs on", "Docker Compose"),
                   ("Status", "In progress")],
    ),
]


def render():
    OUT.mkdir(exist_ok=True)
    for i, p in enumerate(PROJECTS):
        prev = PROJECTS[i - 1]
        nxt = PROJECTS[(i + 1) % len(PROJECTS)]
        html = PAGE.format(
            site=SITE,
            slug=p["slug"],
            title=p["title"],
            cover=p["cover"],
            hero=p.get("hero", p["cover"]),
            alt=p["alt"],
            tagline=p["tagline"],
            meta=p["meta"],
            tags="".join(p["tags"]),
            description="\n".join(
                '      <p class="project-description">%s</p>' % d for d in p["description"]
            ),
            actions="\n".join(
                btn(href, label, primary, p["title"]) for href, label, primary in p["actions"]
            ),
            notes="\n".join(
                '        <h3>%s</h3>\n        <p>%s</p>' % (h, b) for h, b in p["notes"]
            ),
            meta_rows="\n".join(
                '          <dt>%s</dt><dd>%s</dd>' % (k, v) for k, v in p["meta_rows"]
            ),
            prev_slug=prev["slug"], prev_title=prev["title"],
            next_slug=nxt["slug"], next_title=nxt["title"],
        )
        (OUT / ("%s.html" % p["slug"])).write_text(html, encoding="utf-8")
        print("wrote projects/%s.html" % p["slug"])


if __name__ == "__main__":
    render()
