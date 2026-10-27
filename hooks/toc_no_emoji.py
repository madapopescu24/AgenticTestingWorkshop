"""
MkDocs hook — strip emojis from the table of contents.

Headings keep their emoji on the page, but the left panel (toc.integrate)
shows the heading text without it: "🧩 SAP Testing" → "SAP Testing".
"""

import re

# Emoji, pictographs, and the joiners and variation selectors that combine them.
_EMOJI = re.compile(
    "["
    "\U0001F000-\U0001FAFF"  # pictographs, emoticons, transport, symbols
    "☀-➿"          # misc symbols and dingbats (☕, ⚙, ✅)
    "⌀-⏿"          # misc technical (⏱, ⏩, ⏳)
    "⬀-⯿"          # arrows and shapes (⭐)
    "■-◿"          # geometric shapes (▶)
    "←-⇿"          # arrows
    "️‍⃣"     # variation selector, zero-width joiner, keycap
    "]+"
)


def _clean(items):
    for item in items:
        item.title = _EMOJI.sub("", item.title).strip()
        _clean(item.children)


def on_page_content(html, page, config, files):
    _clean(page.toc)
    return html
