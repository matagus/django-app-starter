# Release Process

Releasing a new version involves tagging a commit, letting GitHub Actions create a draft release, then publishing that draft — which triggers the PyPI upload automatically.

## Prerequisites

Before your first release, make sure you've completed:

- [ ] [PyPI Publishing setup](setup/pypi-publishing.md) — `release` environment + `PYPI_API_TOKEN` secret

## Step-by-Step

### 1. Prepare your release

Make sure all changes for this release are merged to `main` and the CI is green.

If you want to update the version explicitly, edit the version in `pyproject.toml`. If you're using Hatch's dynamic versioning from git tags, no manual version bump is needed.

### 2. Tag the commit

Create an annotated tag on the commit you want to release:

```bash
git tag v0.1.0
```

Use [semantic versioning](https://semver.org/): `v<major>.<minor>.<patch>`.

### 3. Push the tag

```bash
git push origin v0.1.0
```

### 4. Wait for the draft release

The `release.yml` workflow triggers on the tag push and creates a **draft** GitHub release. It takes about a minute to complete.

Go to your repository → **Releases** to see the draft.

### 5. Review and edit the draft

GitHub auto-generates release notes from merged pull requests. In the draft:

- Review the auto-generated release notes
- Edit or add any additional context
- Verify the tag and target commit are correct

### 6. Publish the release

Click **Publish release**.

### 7. PyPI upload runs automatically

Publishing the release triggers the `publish.yml` workflow, which:

1. Checks out the code at the release tag
2. Runs `hatch build` to create the distribution files
3. Uploads to PyPI

You can monitor the upload in the **Actions** tab. Once complete, your package will be live at `https://pypi.org/project/<your-package-name>/`.

## Verifying the Release

After publishing, verify:

```bash
pip install <your-package-name>==0.1.0
```

Or check the PyPI page directly.

## Yanking a Release

If you need to yank a broken release from PyPI:

1. Go to your package's PyPI page → **Release history**
2. Click the version → **Options** → **Yank this release**

Yanking prevents new installs but doesn't break existing ones. It does not delete the release from GitHub.
