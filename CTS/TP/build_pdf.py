"""Genera el PDF del TP a partir del Markdown.

Uso:  python build_pdf.py
Requiere Microsoft Edge (para imprimir a PDF) y pdftotext (para numerar el índice).
"""
import html
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "TPF-Megacentros-de-datos-Patagonia.md"
OUT = HERE / "TPF-Megacentros-de-datos-Patagonia.pdf"
COVER_IMG = HERE / "img" / "dcd-neuquen.jpg"
COVER_CREDIT = "Foto: DatacenterDynamics"
EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page {
  size: A4;
  margin: 26mm 25mm 24mm 25mm;
  @top-right { content: "Megacentros de datos para IA en la Patagonia"; font: 8.5pt "Segoe UI", Arial, sans-serif; color: #6b7f86; }
  @bottom-center { content: counter(page); font: 9.5pt "Segoe UI", Arial, sans-serif; color: #40545b; }
}
@page cover { margin: 0; @top-right { content: none; } @bottom-center { content: none; } }

* { box-sizing: border-box; }
html { font-family: Cambria, Georgia, "Times New Roman", serif; font-size: 11.5pt; line-height: 1.52; color: #1b2327; }
body { margin: 0; }
p { margin: 0 0 9pt; text-align: justify; hyphens: auto; orphans: 3; widows: 3; }
strong { font-weight: 700; }

h2, h3 { font-family: "Segoe UI", Arial, sans-serif; color: #0a2a36; break-after: avoid; }
h2 { font-size: 16.5pt; line-height: 1.2; margin: 26pt 0 11pt; padding-bottom: 5pt; border-bottom: 1.6pt solid #1f8a8f; }
h2 .n { color: #1f8a8f; margin-right: 7pt; }
h3 { font-size: 12.3pt; margin: 17pt 0 7pt; }
h4 { font-family: "Segoe UI", Arial, sans-serif; font-size: 9pt; letter-spacing: .1em; text-transform: uppercase; color: #1f8a8f; margin: 16pt 0 7pt; break-after: avoid; }
.newpage { break-before: page; margin-top: 0; }

ul { margin: 0 0 10pt; padding-left: 15pt; }
li { margin-bottom: 5.5pt; text-align: justify; hyphens: auto; }
li::marker { color: #1f8a8f; }

/* carátula */
.cover { page: cover; height: 297mm; position: relative; break-after: page; font-family: "Segoe UI", Arial, sans-serif; }
.cover .photo { height: 118mm; background-size: cover; background-position: center; position: relative; }
.cover .photo span { position: absolute; right: 8mm; bottom: 4mm; font-size: 7.5pt; color: #fff; text-shadow: 0 0 3px rgba(0,0,0,.9), 0 0 1px #000; }
.cover .band { background: #0a2a36; color: #fff; padding: 7mm 25mm; font-size: 9.5pt; letter-spacing: .14em; text-transform: uppercase; }
.cover .band b { color: #6fd3d6; font-weight: 600; }
.cover .main { padding: 17mm 25mm 0; }
.cover h1 { font-family: Cambria, Georgia, serif; font-size: 31pt; line-height: 1.1; margin: 0 0 9mm; color: #0a2a36; }
.cover .sub { font-size: 14.5pt; line-height: 1.35; color: #a86a12; margin: 0; text-align: left; hyphens: none; }
.cover .meta { position: absolute; left: 25mm; right: 25mm; bottom: 22mm; border-top: 1.6pt solid #1f8a8f; padding-top: 6mm; display: grid; grid-template-columns: 34mm 1fr; row-gap: 2.2mm; font-size: 10.5pt; }
.cover .meta dt { color: #6b7f86; font-size: 8.5pt; letter-spacing: .1em; text-transform: uppercase; padding-top: 1.4pt; }
.cover .meta dd { margin: 0; }
.cover .inst { position: absolute; left: 25mm; bottom: 9mm; font-size: 8.5pt; color: #6b7f86; }

/* resumen e índice */
.abstract { background: #eef5f5; border-left: 3pt solid #1f8a8f; padding: 11pt 14pt 4pt; margin-bottom: 8pt; }
.abstract p { font-size: 10.6pt; }
.plain { border: 0; padding: 0; }
.toc { list-style: none; padding: 0; margin: 0; font-family: "Segoe UI", Arial, sans-serif; font-size: 10.6pt; }
.toc li { display: flex; align-items: baseline; margin: 0 0 6pt; text-align: left; }
.toc li.sub { padding-left: 15pt; font-size: 9.8pt; color: #40545b; margin-bottom: 4pt; }
.toc .dots { flex: 1; border-bottom: 1px dotted #9db0b5; margin: 0 6pt; transform: translateY(-3pt); }
.toc .pg { font-variant-numeric: tabular-nums; }

/* bibliografía */
.refs { list-style: none; padding: 0; }
.refs li { padding-left: 18pt; text-indent: -18pt; text-align: left; hyphens: none; font-size: 10.2pt; line-height: 1.42; margin-bottom: 6.5pt; break-inside: avoid; }
.refs a { color: #1a6c70; text-decoration: none; overflow-wrap: anywhere; font-size: 9pt; }
"""


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"(https?://\S+)", r'<a href="\1">\1</a>', text)
    return text


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def parse(md):
    lines = md.splitlines()
    meta = {"title": "", "sub": "", "fields": []}
    i = 0
    while i < len(lines) and not lines[i].startswith("## Resumen"):
        ln = lines[i].strip()
        if ln.startswith("# "):
            meta["title"] = ln[2:]
        elif ln.startswith("## "):
            meta["sub"] = ln[3:]
        else:
            m = re.match(r"- \*\*(.+?):\*\*\s*(.*)", ln)
            if m:
                meta["fields"].append((m.group(1), m.group(2)))
        i += 1

    blocks, para, items = [], [], []

    def flush():
        nonlocal para, items
        if para:
            blocks.append(("p", " ".join(para)))
            para = []
        if items:
            blocks.append(("ul", items))
            items = []

    section = None
    for ln in lines[i:]:
        s = ln.rstrip()
        if s.startswith("## "):
            flush()
            section = s[3:]
            blocks.append(("h2", section))
        elif s.startswith("### "):
            flush()
            blocks.append(("h3", s[4:]))
        elif s.strip() == "---":
            flush()
        elif s.startswith("- "):
            if para:
                flush()
            items.append(s[2:])
        elif re.match(r"\d+\. ", s) and section == "Índice":
            continue  # el índice se genera con los títulos reales
        elif not s.strip():
            flush()
        else:
            if items:
                flush()
            para.append(s.strip())
    flush()
    return meta, blocks


def build(meta, blocks, pages):
    heads = [(k, t) for k, t in blocks if k in ("h2", "h3") and re.match(r"\d", t)]
    toc = ['<ol class="toc">']
    for kind, t in heads:
        cls = ' class="sub"' if kind == "h3" else ""
        toc.append(f'<li{cls}><span>{inline(t)}</span><span class="dots"></span><span class="pg">{pages.get(t, "")}</span></li>')
    toc.append("</ol>")

    fields = "".join(f"<dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd>" for k, v in meta["fields"])
    out = [f"""<section class="cover">
  <div class="photo" style="background-image:url('{COVER_IMG.as_uri()}')"><span>{COVER_CREDIT}</span></div>
  <div class="band"><b>Ciencia, Tecnología y Sociedad</b> &nbsp;·&nbsp; Trabajo Práctico Final</div>
  <div class="main"><h1>{html.escape(meta['title'])}</h1><p class="sub">{html.escape(meta['sub'])}</p></div>
  <dl class="meta">{fields}</dl>
  <div class="inst">Universidad Nacional de San Martín · Escuela de Ciencia y Tecnología · 2.º cuatrimestre de 2026</div>
</section>"""]

    section = None
    first_numbered = True
    for kind, val in blocks:
        if kind == "h2":
            section = val
            if val == "Resumen":
                out.append('<h2 class="plain" style="margin-top:0">Resumen</h2><div class="abstract">')
            elif val == "Índice":
                out.append('</div><h2 class="plain">Índice</h2>' + "\n".join(toc))
            else:
                m = re.match(r"(\d+)\.\s+(.*)", val)
                brk = first_numbered or "ibliograf" in val
                first_numbered = False
                cls = ' class="newpage"' if brk else ""
                out.append(f'<h2{cls}><span class="n">{m.group(1)}</span>{inline(m.group(2))}</h2>')
        elif kind == "h3":
            tag = "h3" if re.match(r"\d", val) else "h4"
            out.append(f"<{tag}>{inline(val)}</{tag}>")
        elif kind == "p":
            out.append(f"<p>{inline(val)}</p>")
        elif kind == "ul":
            cls = ' class="refs"' if section and "ibliograf" in section else ""
            out.append(f"<ul{cls}>" + "".join(f"<li>{inline(x)}</li>" for x in val) + "</ul>")

    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>{html.escape(meta['title'])}</title><style>{CSS}</style></head><body>
{chr(10).join(out)}
</body></html>"""


def print_pdf(edge, html_path, pdf_path, profile):
    subprocess.run(
        [edge, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--user-data-dir={profile}", f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120,
    )


def heading_pages(pdf_path, blocks):
    """Busca en qué página cae cada título numerado."""
    exe = shutil.which("pdftotext")
    if not exe:
        return {}
    txt = subprocess.run([exe, "-enc", "UTF-8", "-layout", str(pdf_path), "-"],
                         capture_output=True, check=True).stdout.decode("utf-8", "replace")
    page_lines = [[norm(l) for l in pg.splitlines()] for pg in txt.split("\f")]
    pages = {}
    start = 2  # después de la carátula y de la página del índice
    for kind, t in blocks:
        if kind not in ("h2", "h3") or not re.match(r"\d", t):
            continue
        key = norm(t)[:28]
        for n in range(start, len(page_lines)):
            if any(l.startswith(key) for l in page_lines[n]):
                pages[t] = n + 1
                start = n
                break
    return pages


def main():
    edge = next((p for p in EDGE_CANDIDATES if Path(p).exists()), None)
    if not edge:
        sys.exit("No encontré Edge ni Chrome para imprimir a PDF.")
    meta, blocks = parse(SRC.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        tmp = Path(tmp)
        page, draft = tmp / "tp.html", tmp / "draft.pdf"
        page.write_text(build(meta, blocks, {}), encoding="utf-8")
        print_pdf(edge, page, draft, tmp / "profile")
        pages = heading_pages(draft, blocks)
        page.write_text(build(meta, blocks, pages), encoding="utf-8")
        print_pdf(edge, page, OUT, tmp / "profile")
    print(f"OK: {OUT.name} ({len(pages)} títulos numerados en el índice)")


if __name__ == "__main__":
    main()
