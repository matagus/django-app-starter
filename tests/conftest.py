from pathlib import Path

import copier
import pytest


TEMPLATE_ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="session")
def generated_app(tmp_path_factory):
    dst = tmp_path_factory.mktemp("app")
    copier.run_copy(
        src_path=str(TEMPLATE_ROOT),
        dst_path=str(dst),
        data={
            "project_name": "my-test-app",
            "module_name": "my_test_app",
            "project_description": "A test Django app",
            "secret_key": "test-secret-key-12345678901234567890",
        },
        defaults=True,
        overwrite=True,
        quiet=True,
    )
    return dst
