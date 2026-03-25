# Getting Started

## Prerequisites

You need `copier` and `hatch` installed:

```bash
pip install copier
pip install hatch
```

## Generate a New App

```bash
copier copy https://github.com/matagus/django-app-starter <your-app-name>
```

You'll be prompted for:

- **Project name** — the Python package name (e.g. `django-my-app`)
- **Module name** — the Python module name (auto-derived, e.g. `django_my_app`)
- **Description** — a short description of what your app does
- **GitHub username** — your GitHub username or org name (used in badge URLs and clone paths)

After answering the prompts, a new directory is created with your app ready to develop.

## Run the Example Project

The generated app includes an `example_project` you can use to test your app immediately:

```bash
cd <your-app-name>
hatch run project:migrate
hatch run project:createsuperuser
hatch run project:runserver
```

## Run the Tests

Run tests across all supported Python + Django version combinations:

```bash
hatch run test:test
```

Run tests for a specific combination (e.g. Python 3.14 + Django 6.0):

```bash
hatch run test.py3.14-6.0:test
```

See all available environments:

```bash
hatch env show
```

## Check Coverage

```bash
hatch run test:cov
```

## Next Steps

Your app is ready to develop — but a few one-time setup steps are needed to activate the full CI/CD pipeline:

- [Post-Generation Setup Guide](setup/index.md) — GitHub Pages, Codecov, PyPI publishing
- [GitHub Actions Overview](workflows.md) — understand what each workflow does
- [Release Process](release-process.md) — how to cut a release and publish to PyPI
