import os
import shutil
from datetime import datetime
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
ASSETS = ROOT / "assets"
DATA = ROOT / "data"
DIST = ROOT / "dist"


def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def copy_assets():
    dst_assets = DIST / "assets"
    if dst_assets.exists():
        shutil.rmtree(dst_assets)
    shutil.copytree(ASSETS, dst_assets)


def ensure_dist():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)


def env() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html", "xml"]),
    )


def render_pages():
    e = env()

    # Load data
    products = load_yaml(DATA / "products.yaml")
    locations = load_yaml(DATA / "locations.yaml")
    founder = load_yaml(DATA / "founder.yaml")

    common_ctx = {
        "year": datetime.now().year,
    }

    # Index
    tpl = e.get_template("index.html")
    html = tpl.render(popular=products.get("popular", []), **common_ctx)
    (DIST / "index.html").write_text(html, encoding="utf-8")

    # Menu
    tpl = e.get_template("menu.html")
    items = products.get("items", [])
    categories = products.get("categories", [])
    html = tpl.render(items=items, categories=categories, **common_ctx)
    (DIST / "menu.html").write_text(html, encoding="utf-8")

    # Locations
    tpl = e.get_template("locations.html")
    html = tpl.render(locations=locations.get("locations", []), **common_ctx)
    (DIST / "locations.html").write_text(html, encoding="utf-8")

    # About
    tpl = e.get_template("about.html")
    html = tpl.render(**common_ctx)
    (DIST / "about.html").write_text(html, encoding="utf-8")

    # Contact
    tpl = e.get_template("contact.html")
    html = tpl.render(**common_ctx)
    (DIST / "contact.html").write_text(html, encoding="utf-8")

    # Founder
    tpl = e.get_template("founder.html")
    html = tpl.render(founder=founder or {}, **common_ctx)
    (DIST / "founder.html").write_text(html, encoding="utf-8")


def main():
    ensure_dist()
    copy_assets()
    render_pages()
    print(f"Built site to {DIST}")


if __name__ == "__main__":
    main()
