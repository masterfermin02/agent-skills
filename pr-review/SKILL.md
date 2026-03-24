---
name: pr-review
description: "Code review GitHub Pull Requests. Use whenever asked to review a PR, check a pull request, audit a diff, or give feedback on a GitHub PR. Triggers on: 'review this PR', 'code review', 'check this PR', 'review pull request', GitHub PR URLs (github.com/.../pull/NNN), or any request to audit code changes. Supports private repos via GitHub token. Delegates to language-specific skills (laravel-best-practices, csharp-best-practices, php-the-right-way) when applicable."
---

## Workflow

### Step 1 — Parse the PR URL
Extract `owner`, `repo`, `pr_number` from the URL:
`https://github.com/{owner}/{repo}/pull/{pr_number}`

### Step 2 — Fetch PR metadata + diff
Use the GitHub API. If a token is available in context or provided by user, use it.

```bash
# PR metadata
curl -s -H "Authorization: Bearer {token}" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"

# Diff
curl -s -H "Authorization: Bearer {token}" \
  -H "Accept: application/vnd.github.v3.diff" \
  "https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
```

If no token provided and repo is private → ask user for a GitHub token.
If repo is public → token optional.

### Step 3 — Identify languages/frameworks
Scan changed files for:
- `.php` + `artisan`/`composer.json` → apply **laravel-best-practices**
- `.php` (no Laravel) → apply **php-the-right-way**
- `.cs` → apply **csharp-best-practices**
- `.ts`/`.tsx` + React → apply Inertia/React rules from laravel-best-practices if in Laravel context
- Any language → apply universal rules below

### Step 4 — Review the diff
Apply rules from **references/universal-rules.md**.
Apply language-specific skill rules if detected.

### Step 5 — Output structured review

Format:
```
## PR Review: {title}
**Author:** {author} | **Files:** {changed_files} | **+{additions}/-{deletions}**

### 🔴 Must fix ({count})
### 🟡 Should fix ({count})
### ⚪ Suggestions ({count})

---
### Finding: {title}
**Severity:** 🔴 / 🟡 / ⚪
**File:** `path/to/file.ext` (line N)
**Issue:** clear description
**Fix:**
\`\`\`diff
- bad code
+ good code
\`\`\`

---
### Summary
Overall verdict: ✅ Approve / 🔄 Request changes / 💬 Comment
```

## Token Storage
If user provides a GitHub token, store it for future use in:
`/home/node/.openclaw/.openclaw/workspace/TOOLS.md` under `### GitHub`

## Rules Reference
See **references/universal-rules.md** for language-agnostic review rules.
