# Codecov

The CI workflow runs coverage on every push and pull request, and uploads the results to [Codecov](https://codecov.io). This gives you per-PR coverage diffs, a coverage badge, and trend graphs over time.

## Steps

### 1. Create a Codecov account

Go to [codecov.io](https://codecov.io) and sign in with your GitHub account.

### 2. Add your repository

1. In the Codecov dashboard, click **+ Add new repository**
2. Find and select your repository
3. Copy the **Repository Upload Token** shown on the setup page

### 3. Add the secret to GitHub

1. Go to your GitHub repository → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `CODECOV_TOKEN`
4. Value: paste the token from Codecov
5. Click **Add secret**

That's it. The next CI run will upload coverage automatically.

## How the Workflow Uses It

In `ci.yml`, after running tests with coverage, the workflow uploads the report:

```yaml
- name: Upload coverage reports to Codecov
  uses: codecov/codecov-action@v5
  env:
    CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
```

## Coverage Badge

Your generated `README.md` already includes a Codecov badge. Once you've completed setup and the first CI run has uploaded a report, the badge will show your current coverage percentage.

## Running Coverage Locally

```bash
hatch run test:cov
```

This generates both a JSON report (used by the CI upload) and a text report printed to the terminal.
