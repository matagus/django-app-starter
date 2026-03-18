import os
import subprocess
import sys


def test_django_check_passes(generated_app):
    # PYTHONPATH must include both the app root (for `tests` and `my_test_app` packages)
    # and example_project/ (so the `example_project` package referenced by
    # WSGI_APPLICATION = "example_project.wsgi.application" is importable).
    pythonpath = os.pathsep.join(
        [
            str(generated_app),
            str(generated_app / "example_project"),
        ]
    )
    result = subprocess.run(
        [sys.executable, "-m", "django", "check", "--settings", "tests.settings"],
        cwd=str(generated_app),
        env={**os.environ, "PYTHONPATH": pythonpath},
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
    assert (
        result.returncode == 0
    ), f"django check failed:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
