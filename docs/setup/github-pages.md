# GitHub Pages

The generated app includes a `gh-pages.yml` workflow that builds your MkDocs documentation and deploys it to GitHub Pages on every push to `main`. You just need to enable GitHub Pages in your repo settings once.

## Steps

### 1. Push your app to GitHub

Make sure your generated app is pushed to a GitHub repository before proceeding.

### 2. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in the left sidebar under "Code and automation")
3. Under **Source**, select **Deploy from a branch**
4. Under **Branch**, select `gh-pages` and leave the folder as `/ (root)`
5. Click **Save**

!!! note
    The `gh-pages` branch is created automatically the first time the `gh-pages.yml` workflow runs. If it hasn't run yet, trigger it manually from the **Actions** tab.

### 3. Trigger the first deploy (if needed)

If you haven't pushed to `main` yet since setting up the repo:

1. Go to **Actions** → **Publish docs via GitHub Pages**
2. Click **Run workflow** → **Run workflow**

### 4. Find your docs URL

After the workflow completes, your docs will be live at:

```
https://<your-github-username>.github.io/<your-repo-name>/
```

GitHub also shows this URL in **Settings → Pages** once the first deployment succeeds.

## How the Workflow Works

The `gh-pages.yml` workflow sets up Python, installs the docs dependencies from `pyproject.toml`, and deploys using MkDocs' built-in `gh-deploy` command:

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: "3.x"

- name: Install docs dependencies
  run: pip install ".[docs]"

- name: Deploy docs
  run: mkdocs gh-deploy --force
```

No secret setup is needed — the `permissions: contents: write` block grants the workflow permission to push to the `gh-pages` branch. Dependencies come from the `[project.optional-dependencies] docs` section in `pyproject.toml`.

## Customising the Docs

Edit `mkdocs.yml` and the files under `docs/` to add pages, change the theme, or update navigation. See the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/) for configuration options.
