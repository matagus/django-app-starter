# GitHub Actions

The generated app comes with five GitHub Actions workflows. Here's a complete overview.

## Workflow Summary

| Workflow | File | Trigger | Secrets needed |
|----------|------|---------|----------------|
| CI | `ci.yml` | Push/PR to `main`, manual | `CODECOV_TOKEN` |
| Docs | `gh-pages.yml` | Push to `main`, manual | — |
| Labels | `labels.yml` | Push to `main` (`.github/**`), manual | — |
| Release draft | `release.yml` | Push `v*` tag, manual | — |
| Publish to PyPI | `publish.yml` | Release published, manual | `PYPI_API_TOKEN` |

## CI (`ci.yml`)

Runs on every push and pull request to `main`.

Tests your package against a matrix of Python and Django versions:

- **Python**: 3.10, 3.11, 3.12, 3.13, 3.14
- **Django**: 5.0, 5.1, 5.2, 6.0

Incompatible combinations are excluded (e.g. Django 5.0 doesn't support Python 3.13+, Django 6.0 requires Python 3.12+).

After each test run, coverage is uploaded to Codecov. Requires the `CODECOV_TOKEN` secret — see [Codecov setup](setup/codecov.md).

## Docs (`gh-pages.yml`)

Runs on every push to `main`.

Builds your MkDocs documentation and deploys it to the `gh-pages` branch, which serves your GitHub Pages site. Uses `GITHUB_TOKEN` (auto-provided). Requires GitHub Pages to be enabled in your repo settings — see [GitHub Pages setup](setup/github-pages.md).

## Labels (`labels.yml`)

Runs on every push to `main` that changes files under `.github/**`.

Syncs GitHub issue/PR labels from `.github/labels.toml` using the [`labels` CLI](https://github.com/hackebrot/labels). Uses `GITHUB_TOKEN` (auto-provided). No setup required — see [Labels](setup/labels.md).

## Release Draft (`release.yml`)

Runs when you push a tag matching `v*` (e.g. `v1.0.0`).

Creates a **draft** GitHub release with auto-generated release notes based on merged pull requests since the last release. The draft is not published automatically — you review and publish it manually. This is the first step in the [release process](release-process.md).

## Publish to PyPI (`publish.yml`)

Runs when you **publish** a GitHub release (not just create a draft).

Builds your package using `hatch build` and uploads the distribution files to PyPI using the [`pypa/gh-action-pypi-publish`](https://github.com/pypa/gh-action-pypi-publish) action. Runs in the `release` environment. Requires the `PYPI_API_TOKEN` secret — see [PyPI Publishing setup](setup/pypi-publishing.md).

## Release Flow

```
git tag v1.0.0 && git push origin v1.0.0
        │
        ▼
  release.yml runs
  → Draft release created on GitHub
        │
        ▼
  You review and publish the draft
        │
        ▼
  publish.yml runs
  → Package built and uploaded to PyPI
```

See [Release Process](release-process.md) for the full walkthrough.
