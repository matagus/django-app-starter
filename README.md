# django-app-starter

![Python Compatibility](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg) ![Django Compatibility](https://img.shields.io/badge/django-5.x%20%7C%206.x-green.svg) [![License](https://img.shields.io/badge/MIT-blue.svg)](https://opensource.org/licenses/MIT) [![We use Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**GitHub Template Repository**: Click "Use this template" to instantly create a new Django app with all the goodies you need to start developing, testing, and publishing to PyPI and GitHub. No local setup required.

## Features

- [x] Compatibility with Python 3.10 to 3.14 and Django 5.x to 6.x
- [x] Package management and dynamic versioning using [Hatch](https://hatch.pypa.io/latest/install/).
- [x] Testing with `hatch` for all possible combinations of Python and Django versions.
- [x] Code coverage reporting to using [Coverage.py](https://coverage.readthedocs.io/en/latest/).
- [x] Ready to use [GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions) pipelines for:
  * [x] CI + reporting code coverage to codecov.io
  * [x] Building and publishing to Pypi when a new tag is pushed
  * [x] Creating a draft release
- [x] `pre-commit` configuration with:
  - [x] `black` for code formatting
  - [x] Linting and formatting with [`ruff`](https://github.com/charliermarsh/ruff)
  - [x] `codespell`, `pyupgrade` and several standard checks.
- [x] Consistent coding styles for multiple editors and IDEs via [.editorconfig](https://editorconfig.org/) file.
- [x] Configuration using `pyproject.toml` file.
- [x] `README.md` file with instructions on how to start developing, testing and publishing your app.
- [x] An `example_project` fully configured to try you app from the start.
- [x] Dependency updates with [Dependabot](https://github.com/dependabot).
- [x] Issues templates for bugs and features, a Code of conduct file referencing Django's CoC, and a Security Policy config.
- [x] Documentation with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and docstring reference support with [mkdocstrings](https://mkdocstrings.github.io/).
- [x] Latest stable documentation published to [GitHub](https://docs.github.com/en/pages)/[GitLab](https://docs.gitlab.com/ee/user/project/pages/) Pages.
- [x] GitHub Actions automation that renders the template on first use (no local Copier needed)

## Coming Soon

- [ ] [Versioned documentation](https://docs.readthedocs.io/en/stable/versions.html) and [pull request previews](https://docs.readthedocs.io/en/stable/pull-requests.html) with [Read the Docs](https://readthedocs.org/).
- [ ] Containerization for development and deployment with [dev container](https://containers.dev/).
- [ ] Follow the [all-contributors](https://github.com/all-contributors/all-contributors) specification.

## Usage

### Create a New Django App from Template

1. Click the **"Use this template"** button on GitHub
2. Enter your project details when prompted:
   - **Project name**: Your Django app name
   - **Module name**: Your Python module name
   - **Project description**: Brief description of your app
3. GitHub Actions will automatically render the template and initialize your new repository

`django-app-starter` comes with an example project you can use to test your app. To run it just do:

```bash
cd <app-name>
hatch run project:migrate
hatch run project:createsuperuser
hatch run project:runserver
```

Also, you can run the tests (for all the Python + Django valid combinations: from 3.10 to 3.14 and 5.x to 6.x) with:

```bash
hatch run test:test
```

And you can check the coverage with:

```bash
hatch run test:cov
```

To run tests for a specific Python and Django version, for instance Python 3.14 and Django 6.0, you can use:

```bash
hatch run test.py3.14-6.0:test
```

### Optional: Use Copier Locally

If you prefer to use Copier locally instead of the GitHub template workflow:

```bash
pip install copier hatch
copier copy https://github.com/matagus/django-app-starter <app-name>
```

Learn more about `hatch` and its commands in the [official documentation](https://hatch.pypa.io/latest/) or just ask for help in our [Discussion section](https://github.com/matagus/django-app-starter/discussions).

### How It Works

This template uses GitHub Actions to automatically render the Copier template when you create a new repository. The workflow installs Copier, runs it with your inputs, and commits the rendered result to your new repo.

## Contributing

Contributions are welcome! ❤️

## License

`django-app-starter` is released under an MIT License - see the `LICENSE` file for more information.

## Webliography

- [Copier Documentation](https://copier.readthedocs.io/en/stable/)
