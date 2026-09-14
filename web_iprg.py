#!/usr/bin/env python3
"""
Genera i serveix una web MkDocs global a partir de les carpetes ud0, ud1, ud2...

Ús:
    python3 web_iprg.py
    python3 web_iprg.py --generate-only

El script NO modifica els apunts originals.
Crea tot el necessari dins de:
    _web_global/
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: falta PyYAML. Instal·la MkDocs amb:")
    print("  python3 -m pip install mkdocs mkdocs-material")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent
GLOBAL = ROOT / "_web_global"
DOCS = GLOBAL / "docs"
CONFIG = GLOBAL / "mkdocs.yml"
CSS = DOCS / "stylesheets" / "extra.css"

UNIT_RE = re.compile(r"^ud(\d+)\b", re.IGNORECASE)

# Unitats que es publicaran en la web global. Per exemple, {0, 1, 2} per a ud0, ud1 i ud2.
PUBLISHED_UNITS = {0,1,2,5}

# Fitxers que no té sentit copiar/enllaçar a la web global.
EXCLUDED_SUFFIXES = {
    ".docx", ".odt", ".zip", ".DS_Store",
}
EXCLUDED_NAMES = {
    ".DS_Store", "mkdocs.yml",
}


def natural_key(text: str):
    """Ordenació natural: 2 abans de 10."""
    return [
        int(part) if part.isdigit() else part.casefold()
        for part in re.split(r"(\d+)", text)
    ]


def contains_markdown(folder: Path) -> bool:
    return folder.is_dir() and any(folder.rglob("*.md"))


def choose_content_root(unit: Path) -> Path | None:
    """
    Tria on estan els apunts Markdown d'una UD.
    Prioritat:
      1) udX/docs
      2) arrel de la UD, si hi ha .md directes
      3) qualsevol carpeta 'docs' interna que continga .md
      4) arrel de la UD si hi ha .md en subcarpetes
    """
    direct_docs = unit / "docs"
    if contains_markdown(direct_docs):
        return direct_docs

    if any(unit.glob("*.md")):
        return unit

    candidates = [
        p for p in unit.rglob("docs")
        if p.is_dir() and contains_markdown(p)
    ]
    if candidates:
        candidates.sort(key=lambda p: (len(p.relative_to(unit).parts), natural_key(str(p))))
        return candidates[0]

    if contains_markdown(unit):
        return unit

    return None


def first_h1(md_file: Path) -> str | None:
    """Extrau el primer H1 Markdown normal (# Títol)."""
    try:
        with md_file.open("r", encoding="utf-8") as f:
            in_fence = False
            for line in f:
                stripped = line.strip()
                if stripped.startswith("```") or stripped.startswith("~~~"):
                    in_fence = not in_fence
                    continue
                if not in_fence and stripped.startswith("# "):
                    title = stripped[2:].strip()
                    # Lleva una possible negreta/itálica simple de tot el títol.
                    title = re.sub(r"^\*{1,2}(.*?)\*{1,2}$", r"\1", title)
                    return title
    except (OSError, UnicodeDecodeError):
        pass
    return None


def pretty_stem(path: Path) -> str:
    stem = path.stem
    if stem.lower() == "index":
        return "Inici"
    stem = re.sub(r"^\d+[._ -]*", "", stem)
    stem = stem.replace("_", " ").replace("-", " ")
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem or path.stem


def page_title(path: Path) -> str:
    return first_h1(path) or pretty_stem(path)


def should_link(path: Path) -> bool:
    if path.name in EXCLUDED_NAMES:
        return False
    if path.name.startswith("."):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    return True


def mirror_with_file_symlinks(src: Path, dst: Path):
    """
    Crea directoris reals i enllaços simbòlics per als fitxers.
    Això evita duplicar els apunts i és més fiable per a MkDocs
    que enllaçar simbòlicament el directori complet.
    """
    for current, dirs, files in os.walk(src):
        current_path = Path(current)

        # No entres en ocults ni en possibles carpetes generades.
        dirs[:] = [
            d for d in dirs
            if not d.startswith(".") and d not in {"site", "_web_global", "__pycache__"}
        ]

        rel_dir = current_path.relative_to(src)
        target_dir = dst / rel_dir
        target_dir.mkdir(parents=True, exist_ok=True)

        for filename in files:
            source_file = current_path / filename
            if not should_link(source_file):
                continue

            target_file = target_dir / filename
            if target_file.exists() or target_file.is_symlink():
                target_file.unlink()

            # Enllaç relatiu: el projecte es pot moure sencer.
            relative_target = os.path.relpath(source_file, start=target_file.parent)
            target_file.symlink_to(relative_target)


def build_nested_nav(md_files: list[Path], content_root: Path, url_prefix: str):
    """
    Construeix nav niuat segons les subcarpetes.
    Retorna una llista compatible amb YAML/MkDocs.
    """
    tree = {}

    for file in md_files:
        rel = file.relative_to(content_root)
        parts = list(rel.parts)
        cursor = tree

        for folder in parts[:-1]:
            cursor = cursor.setdefault(folder, {})

        cursor.setdefault("__files__", []).append(file)

    def render(node: dict, rel_parts: list[str]):
        items = []

        files = sorted(
            node.get("__files__", []),
            key=lambda p: (
                0 if p.name.lower() == "index.md" else 1,
                natural_key(str(p.relative_to(content_root))),
            ),
        )

        for f in files:
            rel = f.relative_to(content_root).as_posix()
            items.append({page_title(f): f"{url_prefix}/{rel}"})

        folders = sorted(
            (k for k in node if k != "__files__"),
            key=natural_key,
        )
        for folder in folders:
            child = render(node[folder], rel_parts + [folder])
            if child:
                folder_title = folder.replace("_", " ").replace("-", " ")
                items.append({folder_title: child})

        return items

    return render(tree, [])


def discover_units():
    units = []
    for p in ROOT.iterdir():
        if not p.is_dir():
            continue
        m = UNIT_RE.match(p.name)
        if not m:
            continue

        number = int(m.group(1))
        content = choose_content_root(p)
        if content is None:
            units.append((number, p, None))
        else:
            units.append((number, p, content))

    units.sort(key=lambda x: x[0])
    return units


def unit_label(unit: Path, number: int) -> str:
    rest = UNIT_RE.sub("", unit.name, count=1).strip()
    if rest:
        return f"UD{number} — {rest}"
    return f"UD{number}"


def generate():
    units = discover_units()

    if GLOBAL.exists():
        shutil.rmtree(GLOBAL)
    DOCS.mkdir(parents=True, exist_ok=True)

    nav = []
    watch = []
    included = []
    skipped = []

    # CSS personalitzat per diferenciar visualment els nivells de títol.
    CSS.parent.mkdir(parents=True, exist_ok=True)
    CSS.write_text(
        """
.md-typeset h1 {
    color: #555;
    font-weight: 300;
}

.md-typeset h2 {
    color: #1f3b8f;
    font-weight: 500;
    border-bottom: 1px solid #ddd;
    padding-bottom: 0.2em;
}

.md-typeset h3 {
    color: #4f6190;
    font-weight: 500;
}

.md-typeset h4 {
    color: #555;
    font-weight: 500;
}
""".strip() + "\\n",
        encoding="utf-8",
    ) 

    # Pàgina inicial global.
    index_lines = [
        "# Introducció a la Programació (IPRG)",
        "",
        "Apunts del mòdul organitzats per unitats didàctiques.",
        "",
        "## Unitats disponibles",
        "",
    ]

    for number, unit, content in units:
        label = unit_label(unit, number)

        if number not in PUBLISHED_UNITS:
            skipped.append(label + " (no publicada)")
            continue

        if content is None:
            skipped.append(label)
            continue

        md_files = sorted(
            [p for p in content.rglob("*.md") if not any(part.startswith(".") for part in p.parts)],
            key=lambda p: natural_key(str(p.relative_to(content))),
        )
        if not md_files:
            skipped.append(label)
            continue

        prefix = f"ud{number}"
        mirror_with_file_symlinks(content, DOCS / prefix)

        unit_nav = build_nested_nav(md_files, content, prefix)
        nav.append({label: unit_nav})
        watch.append(os.path.relpath(content, start=GLOBAL))
        included.append((label, len(md_files), content))

        first_page = next(
            (p for p in md_files if p.name.lower() == "index.md"),
            md_files[0],
        )
        first_rel = first_page.relative_to(content).as_posix()
        index_lines.append(f"- [{label}]({prefix}/{first_rel})")

    (DOCS / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    nav.insert(0, {"Inici": "index.md"})

    config = {
        "site_name": "Introducció a la Programació (IPRG)",
        "theme": {
            "name": "material",
            "language": "ca",
            "features": ["content.code.copy"],
            "palette": {
                "accent": "deep purple",
                "primary": "amber",
            },
        },
        "extra_css": [
            "https://joamuran.net/curs24_25/css/material-just.#css",
            "stylesheets/extra.css",
        ],
        "plugins": ["search"],
        "markdown_extensions": [
            "attr_list",
            "md_in_html",
            "admonition",
            "pymdownx.details",
            {
                "pymdownx.highlight": {
                    "anchor_linenums": True,
                    "line_spans": "__span",
                    "pygments_lang_class": True,
                }
            },
            "pymdownx.inlinehilite",
            "pymdownx.snippets",
            "pymdownx.superfences",
            {
                "pymdownx.tabbed": {
                    "alternate_style": True,
                }
            },
            {
                "toc": {
                    "baselevel": 1,
                    "toc_depth": 3,
                }
            },
        ],
        "nav": nav,
        "watch": watch,
    }

    CONFIG.write_text(
        yaml.safe_dump(
            config,
            allow_unicode=True,
            sort_keys=False,
            width=120,
        ),
        encoding="utf-8",
    )

    print("\nWeb global generada.")
    print(f"  Configuració: {CONFIG}")
    print(f"  Documents:    {DOCS}")
    print("\nUnitats incloses:")
    for label, count, content in included:
        print(f"  ✓ {label}: {count} fitxer(s) Markdown")
        print(f"    {content.relative_to(ROOT)}")

    if skipped:
        print("\nUnitats encara sense Markdown utilitzable:")
        for label in skipped:
            print(f"  - {label}")

    return included


def serve():
    cmd = [
        sys.executable,
        "-m",
        "mkdocs",
        "serve",
        "-f",
        str(CONFIG),
    ]
    print("\nArrancant MkDocs...")
    print("Obri al navegador: http://127.0.0.1:8000/")
    print("Per parar-lo: Ctrl+C\n")
    subprocess.run(cmd, cwd=ROOT)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--generate-only",
        action="store_true",
        help="Genera la web global però no arranca el servidor.",
    )
    args = parser.parse_args()

    generate()

    if not args.generate_only:
        serve()


if __name__ == "__main__":
    main()
