#!/usr/bin/env python3
# Micro static-site generator per giampaolomangiaracina.com.
# Legge i post markdown da content/posts/ e genera docs/ (servito da GitHub Pages).
#
# Uso:
#     python3 build.py
#
# Dipendenze: markdown  (pip install -r requirements.txt)

import html
import re
import shutil
from pathlib import Path

import markdown as md

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content" / "posts"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "docs"

DOMAIN = "giampaolomangiaracina.com"

# --- config sito (modificabile a mano) ---
SITE = {
    "name": "Giampaolo Mangiaracina",
    "intro": "CTO e AI/GenAI engineer. Costruisco prodotti AI-driven e coordino i team che li realizzano — oggi attorno ai sistemi multi-agente. Fondatore di FadPro e CityAdvisor.ai. Qui condivido metodo, esperimenti e risultati.",
    "email": "giampaolo@giampaolomangiaracina.com",
    "linkedin": "https://www.linkedin.com/in/giampaolo-mangiaracina/",
}

MONTHS = ["", "gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
          "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def format_date(iso):
    # "2026-06-09" -> "9 giugno 2026"; lascia invariato se non riconosciuto
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", iso.strip())
    if not m:
        return iso
    year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return "{} {} {}".format(day, MONTHS[month], year)


def read_template(name):
    return (TEMPLATES / name).read_text(encoding="utf-8")


def render(tpl, **variables):
    out = tpl
    for key, value in variables.items():
        out = out.replace("{{ %s }}" % key, value)
    return out


def parse_front_matter(text):
    # Front-matter delimitato da ---, righe "key: value". Ritorna (meta, body).
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            front, body = parts[1], parts[2]
            for line in front.strip().splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip()
    return meta, body.strip()


def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def load_posts():
    posts = []
    for path in sorted(CONTENT.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_front_matter(raw)
        slug = meta.get("slug") or slugify(path.stem)
        html_body = md.markdown(body, extensions=["extra", "sane_lists"])
        posts.append({
            "slug": slug,
            "title": meta.get("title", path.stem),
            "date": meta.get("date", ""),
            "date_display": format_date(meta.get("date", "")),
            "excerpt": meta.get("excerpt", ""),
            "html": html_body,
        })
    # ordina per data decrescente (stringa ISO YYYY-MM-DD)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    if STATIC.exists():
        shutil.copytree(STATIC, OUT / "static")

    base = read_template("base.html")
    index_tpl = read_template("index.html")
    post_tpl = read_template("post.html")

    posts = load_posts()

    cards = []
    for p in posts:
        cards.append(
            '<a class="post-card" href="/post/{slug}/">'
            '<div class="post-meta">{date}</div>'
            '<h3 class="post-link">{title}<span class="arrow">&rarr;</span></h3>'
            '<p class="post-excerpt">{excerpt}</p>'
            '</a>'.format(
                slug=p["slug"],
                title=html.escape(p["title"]),
                date=html.escape(p["date_display"]),
                excerpt=html.escape(p["excerpt"]),
            )
        )
    posts_html = "\n".join(cards) if cards else '<p class="empty">Presto.</p>'

    index_content = render(
        index_tpl,
        name=html.escape(SITE["name"]),
        intro=html.escape(SITE["intro"]),
        email=SITE["email"],
        linkedin=SITE["linkedin"],
        posts=posts_html,
    )
    index_page = render(
        base,
        title=html.escape(SITE["name"]),
        content=index_content,
        name=html.escape(SITE["name"]),
        email=SITE["email"],
        linkedin=SITE["linkedin"],
    )
    (OUT / "index.html").write_text(index_page, encoding="utf-8")

    for p in posts:
        post_content = render(
            post_tpl,
            title=html.escape(p["title"]),
            date=html.escape(p["date_display"]),
            body=p["html"],
        )
        page = render(
            base,
            title=html.escape(p["title"]) + " - " + html.escape(SITE["name"]),
            content=post_content,
            name=html.escape(SITE["name"]),
            email=SITE["email"],
            linkedin=SITE["linkedin"],
        )
        post_dir = OUT / "post" / p["slug"]
        post_dir.mkdir(parents=True, exist_ok=True)
        (post_dir / "index.html").write_text(page, encoding="utf-8")

    # CNAME per il dominio custom + .nojekyll per servire docs/ as-is
    (OUT / "CNAME").write_text(DOMAIN + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    print("Build OK: {} post -> {}".format(len(posts), OUT))


if __name__ == "__main__":
    build()
