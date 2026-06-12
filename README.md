# giampaolo_site

Sito statico personale per `giampaolomangiaracina.com` — vetrina da consulente
AI/GenAI. Generato da un micro-generatore Python (markdown -> HTML) e servito
da GitHub Pages.

## Struttura

```
build.py            generatore: legge content/posts/*.md -> scrive docs/
content/posts/*.md  i post (front-matter: title, date, excerpt)
templates/          base.html, index.html, post.html
static/style.css    foglio di stile (minimale, nero su bianco)
docs/               OUTPUT generato (committato: e' cio' che Pages serve)
```

La config del sito (nome, tagline, email, LinkedIn) sta in cima a `build.py`,
nel dict `SITE`.

## Aggiungere un post

1. Crea `content/posts/AAAA-MM-GG-slug.md` con front-matter:

   ```
   ---
   title: Titolo del pezzo
   date: 2026-06-20
   excerpt: Una o due righe di estratto per la home.
   ---

   Corpo in markdown...
   ```

2. Rigenera: `python3 build.py`
3. Commit + push: GitHub Pages pubblica `docs/`.

I post sono ordinati per `date` decrescente.

## Build

```
pip install -r requirements.txt   # una volta (serve markdown)
python3 build.py
```

L'output finisce in `docs/`, inclusi `CNAME` (dominio custom) e `.nojekyll`.

## Deploy (GitHub Pages)

- Repo GitHub, Pages servito da branch `main`, cartella `/docs`.
- Dominio custom `giampaolomangiaracina.com` (record DNS A su Namecheap verso
  GitHub Pages; i record email MX/SPF restano invariati).
- SSL emesso automaticamente da GitHub.

Deploy = `git push` dopo il build.
