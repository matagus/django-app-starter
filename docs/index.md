# django-app-starter

Generate a new Django app with everything you need to start developing, testing, and publishing — batteries included.

![Demo.gif](https://raw.githubusercontent.com/matagus/django-app-starter/main/screenshots/demo.gif)

## What You Get

A freshly generated app comes with:

- **CI/CD** — GitHub Actions for testing, coverage, docs, releases, and PyPI publishing
- **Testing** — pytest via Hatch, covering Python 3.10–3.14 × Django 5.x–6.x
- **Coverage** — Coverage.py + Codecov integration
- **Documentation** — Material for MkDocs, deployed to GitHub Pages
- **Code quality** — pre-commit hooks with Ruff, Black, codespell, and pyupgrade
- **Releases** — automated draft releases on tag push, one-click PyPI publish
- **Labels** — standardised GitHub labels synced from config
- **Dependabot** — automatic dependency update PRs

## Quick Start

```bash
pip install copier
copier copy https://github.com/matagus/django-app-starter <your-app-name>
```

After generating, follow the **[Post-Generation Setup Guide](setup/index.md)** to activate GitHub Pages, Codecov, and PyPI publishing.

See [Getting Started](getting-started.md) for the full walkthrough.

## Coming Soon

- Versioned documentation with [Read the Docs](https://readthedocs.org/)
- Dev containers for local development
- [all-contributors](https://github.com/all-contributors/all-contributors) support
- GitHub Template Repository mode
