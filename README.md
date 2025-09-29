# django-app-starter

![Demo.gif](https://raw.githubusercontent.com/matagus/django-app-starter/main/screenshots/demo.gif)

![Python Compatibility](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg) [![License](https://img.shields.io/badge/MIT-blue.svg)](https://opensource.org/licenses/MIT) [![We use Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Generate a new Django app with all the goodies you need to start developing, testing and publishing your app to PyPI
and Github.


## Features

- [x] Compatibility with Python 3.10 to 3.13 and Django 5.x.
- [x] Package management and dynamic versioning using [Hatch](https://hatch.pypa.io/latest/install/).
- [x] Testing with `hatch` for all possible combinations of Python and Django versions.
- [x] Code coverage reporting to using [Coverage.py](https://coverage.readthedocs.io/en/latest/).
- [x] Ready to use [GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions)
pipelines for:
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
- [x] Issues templates for bugs and features, a Code of conduct file referencing Django's CoC, and a Security Policy
config.
- [x] Sync updates from newest versions of this template with [Copier](https://copier.readthedocs.io/en/stable/updating/).
- [x] Standardised list of GitHub labels synchronised on push to main branch using [the labels CLI](https://github.com/hackebrot/labels).
- [x] Documentation with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and docstring reference
support with [mkdocstrings](https://mkdocstrings.github.io/).
- [x] Latest stable documentation published to [GitHub](https://docs.github.com/en/pages)/[GitLab](https://docs.gitlab.com/ee/user/project/pages/) Pages.


## Coming Soon

- [ ] [Versioned documentation](https://docs.readthedocs.io/en/stable/versions.html) and [pull request previews](https://docs.readthedocs.io/en/stable/pull-requests.html) with [Read the Docs](https://readthedocs.org/).
- [ ] Containerization for development and deployment with [dev container](https://containers.dev/).
- [ ] Follow the [all-contributors](https://github.com/all-contributors/all-contributors) specification.
- [ ] Turn Github repository in to a [Template Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
that does all the setup so people don't need to install copier and run it locally. Similar to what Simon Willison did
with [his cookicutter template](https://github.com/simonw/python-lib-template-repository)


## Usage

### Prerequisites

You need to have `copier` and `hatch` installed in your system. If you don't have them, you can install them with:

```
pip install copier
pip install hatch
```

Then generating a new Django app is as simple as running:

```
copier copy https://github.com/matagus/django-app-starter <app-name>
```

You will be prompted to enter some data needed to generate your app, and then you will have a new directory with your
app ready to go.

`django-app-starter` comes wwith an example project you can use to test your app. To run it just do:

```
cd <app-name>
hatch run project:migrate
hatch run project:createsuperuser
hatch run project:runserver
```

Also, you can run the tests (for all the Python + Django valid combinations) with:

```
hatch run test:test
```

And you can check the coverage with:

```
hatch run test:cov
```

To run tests for a specific Python and Django version, for instance Python 3.12 and Django 5.0, you can use:

```
hatch run test.py3.12-5.0:test
```

Learn more about `hatch` and its commands in the [official documentation](https://hatch.pypa.io/latest/) or
just ask for help in our [Discussion section](https://github.com/matagus/django-app-starter/discussions).

## Contributing

Contributions are welcome! ❤️


## License

`django-app-starter` is released under an MIT License - see the `LICENSE` file for more information.


## Webliography

- [Copier Documentation](https://copier.readthedocs.io/en/stable/)
- [Project templating tools: Cookiecutter, Yeoman, and Copier](https://www.cookiecutter.io/article-post/cookiecutter-alternatives)
