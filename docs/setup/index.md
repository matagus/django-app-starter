# Post-Generation Setup

After running `copier copy`, your app directory is ready — but a few one-time steps are needed to fully activate the GitHub Actions workflows.

## What Works Out of the Box

These workflows require **no configuration** and will work as soon as you push to GitHub:

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| **CI** | Push / PR to `main` | Runs tests across Python 3.10–3.14 × Django 5.x–6.x |
| **Labels** | Push to `main` (`.github/**` changed) | Syncs GitHub labels from `.github/labels.toml` |
| **Release draft** | Push a `v*` tag | Creates a draft GitHub release with auto-generated notes |

## What Needs Setup

These require a one-time manual configuration:

- [ ] **[GitHub Pages](github-pages.md)** — Enable in repo settings so your docs site is deployed
- [ ] **[Codecov](codecov.md)** — Add `CODECOV_TOKEN` secret so coverage reports are uploaded
- [ ] **[PyPI Publishing](pypi-publishing.md)** — Create a `release` environment and add `PYPI_API_TOKEN` secret

Complete these steps in order — GitHub Pages is the quickest and has no external dependencies.

## After Setup

Once everything is configured, your workflow will be:

1. Push code → CI runs tests and uploads coverage
2. Push code → Docs are rebuilt and deployed
3. Tag a release → Draft release is created automatically
4. Publish the draft → Package is built and uploaded to PyPI

See the [Release Process](../release-process.md) for a complete walkthrough.
