# PyPI Publishing

The generated app includes a `publish.yml` workflow that automatically builds and uploads your package to [PyPI](https://pypi.org) whenever you publish a GitHub Release. This requires a one-time setup.

## Steps

### 1. Create a PyPI account

Go to [pypi.org](https://pypi.org/account/register/) and create an account if you don't have one.

### 2. Generate an API token

1. Log in to PyPI and go to **Account settings** → **API tokens**
2. Click **Add API token**
3. Give it a name (e.g. `github-actions-<your-repo-name>`)
4. For scope, choose **Entire account** for the first publish; you can scope it to the project afterward
5. Click **Create token** and copy the token (it starts with `pypi-`)

!!! warning
    Copy the token now — PyPI will not show it again.

### 3. Create a `release` environment in GitHub

The `publish.yml` workflow uses a GitHub Environment called `release` for extra protection:

1. Go to your GitHub repository → **Settings** → **Environments**
2. Click **New environment**
3. Name it exactly `release`
4. Optionally add protection rules (e.g. require manual approval before deploying)
5. Click **Configure environment**

### 4. Add the PyPI token as an environment secret

While still in the `release` environment settings:

1. Under **Environment secrets**, click **Add secret**
2. Name: `PYPI_API_TOKEN`
3. Value: paste your PyPI token
4. Click **Add secret**

## How the Workflow Works

`publish.yml` triggers when you publish a GitHub Release:

```yaml
on:
  release:
    types: [published]
```

It then:

1. Checks out the code at the release tag
2. Builds the distribution using `hatch build`
3. Uploads to PyPI using the `pypa/gh-action-pypi-publish` action

The workflow runs in the `release` environment, which enforces any protection rules you configured.

## Trusted Publishing (OIDC) — Optional

The workflow already has the correct OIDC permission (`id-token: write`), so you can optionally use [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/) instead of an API token:

1. On PyPI, go to your project → **Settings** → **Publishing**
2. Add a trusted publisher: GitHub Actions, with your repo and workflow filename (`publish.yml`)
3. Remove the `user`/`password` fields from the workflow and remove the `PYPI_API_TOKEN` secret

Trusted publishing is more secure because no token is stored anywhere.

## First Publish

The first time you publish, PyPI will create the project under your account. Make sure the package name in `pyproject.toml` is available on PyPI before attempting the first release.
