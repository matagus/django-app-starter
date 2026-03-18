import ast

import tomli as tomllib


EXPECTED_FILES = [
    "my_test_app/__init__.py",
    "my_test_app/__about__.py",
    "my_test_app/admin.py",
    "my_test_app/apps.py",
    "my_test_app/models.py",
    "my_test_app/urls.py",
    "my_test_app/views.py",
    "tests/__init__.py",
    "tests/settings.py",
    "tests/test_something.py",
    "tests/urls.py",
    "pyproject.toml",
    "README.md",
    ".pre-commit-config.yaml",
    ".coveragerc",
    ".gitignore",
    "example_project/manage.py",
    ".github/workflows/ci.yml",
]

# Key files that should have Jinja variables substituted
RENDERED_FILES = [
    "pyproject.toml",
    "README.md",
    "tests/settings.py",
]


def test_expected_files_exist(generated_app):
    for rel_path in EXPECTED_FILES:
        assert (generated_app / rel_path).exists(), f"Missing: {rel_path}"


def test_pyproject_toml_is_valid(generated_app):
    with open(generated_app / "pyproject.toml", "rb") as f:
        data = tomllib.load(f)
    assert data["project"]["name"] == "my-test-app"
    assert data["project"]["description"] == "A test Django app"


def test_jinja_variables_substituted(generated_app):
    for rel_path in RENDERED_FILES:
        content = (generated_app / rel_path).read_text()
        assert "{{" not in content, f"Unrendered Jinja2 '{{{{' found in {rel_path}"
        assert "}}" not in content, f"Unrendered Jinja2 '}}}}' found in {rel_path}"


def test_module_name_in_pyproject_toml(generated_app):
    content = (generated_app / "pyproject.toml").read_text()
    assert "my_test_app" in content


def test_module_name_in_settings(generated_app):
    content = (generated_app / "tests/settings.py").read_text()
    assert "my_test_app" in content


def test_python_files_have_valid_syntax(generated_app):
    for py_file in generated_app.rglob("*.py"):
        source = py_file.read_text()
        try:
            ast.parse(source)
        except SyntaxError as e:
            rel = py_file.relative_to(generated_app)
            raise AssertionError(f"Syntax error in {rel}: {e}") from e
