# Universal PR Review Rules

These apply to any language/framework.

## 🔴 Blockers (must fix before merge)

### Security
- **SEC-001** Hardcoded secrets — API keys, passwords, tokens in code
- **SEC-002** SQL injection risk — string interpolation in queries
- **SEC-003** XSS risk — unescaped user input rendered to HTML
- **SEC-004** Insecure direct object reference — no authorization check on resource access
- **SEC-005** Sensitive data in logs — passwords, tokens, PII logged

### Correctness
- **COR-001** Null/undefined dereference without guard
- **COR-002** Unhandled promise rejection / missing try-catch on async
- **COR-003** Off-by-one errors in loops/pagination
- **COR-004** Race conditions in concurrent code
- **COR-005** Wrong HTTP method or status code

### Code Quality
- **QUA-001** Dead code committed (commented-out blocks, unused imports/vars)
- **QUA-002** Debug/dev artifacts in production code (`console.log`, `dd()`, `var_dump()`, `print_r()`)
- **QUA-003** `.env`/config values hardcoded instead of using config system

---

## 🟡 Warnings (should fix)

### Design
- **DES-001** Function/method does more than one thing (SRP violation)
- **DES-002** Business logic in controller/route handler — should be in service/action
- **DES-003** Duplicated logic — same code block appears 2+ times (DRY violation)
- **DES-004** Magic numbers/strings — unexplained literals (use constants/enums)
- **DES-005** God class/function — too many responsibilities

### Performance
- **PER-001** N+1 query — loop that executes a query per iteration
- **PER-002** Missing database index on filtered/sorted column
- **PER-003** Loading full dataset into memory when pagination/chunking is needed
- **PER-004** Synchronous operation that should be queued/async

### Testing
- **TST-001** No tests added for new feature/bug fix
- **TST-002** Test added but doesn't assert the important behavior
- **TST-003** Test depends on external service without mocking

### Maintainability
- **MAI-001** Missing or inadequate error message (makes debugging hard)
- **MAI-002** Complex conditional that needs extraction or comment
- **MAI-003** Inconsistent naming with surrounding codebase

---

## ⚪ Suggestions (optional improvements)

- **SUG-001** Early return opportunity (remove unnecessary `else`)
- **SUG-002** Could use a more expressive built-in (map/filter vs manual loop)
- **SUG-003** Typo in variable/function/comment name
- **SUG-004** Missing PHPDoc/JSDoc on public API
- **SUG-005** Test coverage could be expanded

---

## Scope Rules

### What to always check
- Every changed file in the diff
- New dependencies added (composer.json, package.json) — check for known vulnerabilities
- Migration files — check for reversibility (`down()` method)
- Config changes — check for accidental exposure of secrets

### What NOT to flag
- Pre-existing issues outside the diff scope
- Style preferences not covered by project's linter config
- Subjective architecture debates without a clear better option

---

## Severity Guidelines

| Severity | When to use |
|---|---|
| 🔴 Must fix | Security risk, data loss, broken functionality, blocks merge |
| 🟡 Should fix | Technical debt, maintainability, performance, missing tests |
| ⚪ Suggestion | Nice-to-have, minor style, optional improvement |
