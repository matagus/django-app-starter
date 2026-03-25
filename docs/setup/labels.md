# GitHub Labels

The generated app includes a `labels.yml` workflow that automatically synchronises your GitHub repository labels from a config file. No manual setup is required.

## How It Works

The workflow triggers on any push to `main` that touches files under `.github/**`:

```yaml
on:
  push:
    branches:
      - main
    paths:
      - ".github/**"
```

It uses the [`labels` CLI](https://github.com/hackebrot/labels) to sync the labels defined in `.github/labels.toml` to your GitHub repository. The `GITHUB_TOKEN` used for authentication is provided automatically — you don't need to configure any secrets.

## Customising Labels

Labels are defined in `.github/labels.toml`. Each label has a name, color, and optional description:

```toml
[[labels]]
name = "bug"
color = "d73a4a"
description = "Something isn't working"

[[labels]]
name = "enhancement"
color = "a2eeef"
description = "New feature or request"
```

To add, remove, or rename labels:

1. Edit `.github/labels.toml`
2. Commit and push to `main`
3. The `labels.yml` workflow runs automatically and syncs the changes

!!! note
    Labels that exist on GitHub but are not in `labels.toml` are **not deleted** automatically. The `sync` command only creates or updates labels defined in the file.

## Manual Trigger

To apply label changes without making another commit, you can trigger the workflow manually from the **Actions** tab:

1. Go to **Actions** → **Sync Github labels**
2. Click **Run workflow** → **Run workflow**

Wait — the current `labels.yml` workflow doesn't include `workflow_dispatch`. To add manual triggering, add this to the `on:` block in `.github/workflows/labels.yml`:

```yaml
on:
  workflow_dispatch:
  push:
    ...
```
