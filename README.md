# django-app-starter

![Python Compatibility](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg) [![License](https://img.shields.io/badge/MIT-blue.svg)](https://opensource.org/licenses/MIT) [![We use Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A copier template for generating a Django app.


## Features

The resulting Django app will:

- Be compatible with Python 3.9 to 3.12 and Django 4 to 5.0.2.
- A `pyproject.toml` with all the metadata for your app.
- Have a `tests` folder where you can place your app's tests, with coverage report and an `example_project` fully
  configured to try you app.
- Use `hatch` for managing virtual environments, testing your library ion every possible & valid combination of
  Python and Django, and provide you with some util commands.
- Use dynamic version management via `hatch`.
- Provide `pre-commit` configuration with `black`, `ruff`, `codespell`, `pyupgrade` and several standard checks.
- Provide a  `.editorconfig`.
- Have a quite complete README file.
- Setup up for using Github Actions for testing your app in the test matrix mentioned above (CI) reporting code
  coverage to codecov.io, building and publishing to Pypi and creating a draft release for your repo.
- Have other goodies for your Github repo like: security policy, issues templates for bugs and features, a Code of
  conduct file referencing Django's CoC, and Dependabot configuration.
- `LICENSE` and `AUTHORS.md` files you should customize to your needs.


## Usage

Generating a new Django app is as simple as doing the following

```bash
pip install copier
copier copy https://github.com/matagus/django-app-starter <app name>
```

You will be prompted to enter some data needed to generate your app:

![Copier copy prompt](https://raw.githubusercontent.com/matagus/django-app-starter/main/screenshots/prompt.png)

Followed by this output:

![Copier copy output](https://raw.githubusercontent.com/matagus/django-app-starter/main/screenshots/output.png)

And at the end you'll get an app in a directory with the following structure:

![App folder structure](https://raw.githubusercontent.com/matagus/django-app-starter/main/screenshots/structure.png)

Now you're all set. See your new app's README for instructions on how to start developing, testing and finally build
and publish your Django application.


## Contributing

Contributions are welcome! ❤️


## Roadmap

- Turn Github repository in to a [Template Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
that does all the setup so people don't need to install copier and run it locally. Similar to what Simon Willison did
with [his cookicutter template](https://github.com/simonw/python-lib-template-repository)
- Enhance generated README file to document all the possible commands and options.


## License

`django-app-starter` is released under an MIT License - see the `LICENSE` file for more information.


## Webliography

- [Copier Documentation](https://copier.readthedocs.io/en/stable/)
- [Project templating tools: Cookiecutter, Yeoman, and Copier](https://www.cookiecutter.io/article-post/cookiecutter-alternatives)
