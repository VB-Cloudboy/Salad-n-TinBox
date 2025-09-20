# Salad in Tin Box — Static Site

Premium pre-packaged healthy food (salads, hearty bowls, sandwiches, healthy snacks), prepared daily by our in-house chef and restocked to 160+ vending machines across Singapore. Sealed airtight for freshness.

## What is this?
A small, Pythonic static site generator using Jinja2 templates and YAML data.

- Templates: `templates/`
- Assets: `assets/`
- Content data: `data/`
- Build output: `dist/`
- Build script: `build.py`

## Quick start

1) Create a virtual environment and install deps

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) Build the site

```powershell
python build.py
```

3) Preview locally (any static server)

```powershell
# Option A: Python simple server
python -m http.server --directory dist 8080

# Option B: PowerShell
Start-Process http://localhost:8080
```

Then open `http://localhost:8080`.

## Customizing
- Edit menu items in `data/products.yaml`
- Edit locations in `data/locations.yaml`
- Update styles in `assets/css/styles.css`
- Pages are in `templates/` (`index.html`, `menu.html`, `locations.html`, `about.html`, `contact.html`)

## License
See `LICENSE`.
