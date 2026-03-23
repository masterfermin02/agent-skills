---
name: unit-testing
description: "Write, review, and improve unit tests using best practices. Framework-agnostic — applies to any language or test framework (xUnit, Jest, PHPUnit, Pest, JUnit, etc.). Use when writing new unit tests, reviewing existing tests for quality, refactoring fragile or brittle tests, choosing between mocks/stubs/fakes/spies, naming tests, structuring test files, identifying anti-patterns, generating test doubles, or applying patterns like AAA, Object Mother, Builder, or Assert Object. Also triggers on phrases like generate tests for this code, my tests are brittle, tests keep breaking, how do I mock this, what is the difference between mock and stub, write a test for, add tests to, test coverage, unit test this, improve my tests, tests are hard to maintain."
---

# Unit Testing Skill

## Installation

```bash
# via skills.sh
npx skillsadd masterfermin02/agent-skills --skill unit-testing

# via ClaWHub
npx clawhub@latest install masterfermin02/agent-skills/unit-testing

# manual
git clone https://github.com/masterfermin02/agent-skills.git
cp -r agent-skills/unit-testing ~/.openclaw/skills/
```

Framework-agnostic unit testing best practices. Apply these patterns regardless of language or test runner.

## Core Principles

1. **Test behavior, not implementation** — tests should survive internal refactoring
2. **One behavior per test** — not one method per test
3. **AAA structure** — Arrange / Act / Assert, always
4. **Prefer fakes and spies over mocks** — less coupling to mocking frameworks
5. **Name tests as readable sentences** — a non-developer should understand the scenario

## Workflow

### Writing New Tests

1. Identify the **unit of behavior** (a business scenario, not a method)
2. Name the test using `Subject_Scenario_ExpectedBehavior` pattern
3. Structure with AAA — keep each section minimal
4. Use Object Mother or Builder for test data setup
5. Assert on observable behavior only — never internal state via reflection

### Reviewing Existing Tests

Check for these anti-patterns (see `references/anti-patterns.md`):
- Tests that verify `Times.Once` on mocks instead of outcomes
- Test names with "Test", "Should", "Assert", "Verify"
- Multiple Act phases in one test
- Getters added only for testing
- Logic in test constructors / shared mutable state

### Choosing Test Doubles

| Double | Use when |
|--------|----------|
| Fake | Replacing infrastructure (DB, email, queue) — working but simple impl |
| Stub | Controlling return values for the SUT |
| Spy | Verifying side effects (what was sent, stored, emitted) |
| Mock | Last resort — when Fake/Spy would be too complex |
| Dummy | Satisfying required params that are never used |

**Default:** Prefer Fake + Spy. Use Mock only when a handwritten double would be complex.

### Test Naming

Pattern: `Subject_Scenario_ExpectedBehavior`

```
✅ Deactivating_AnActiveSubscription_Succeeds
✅ Creating_WithTooShortPassword_IsInvalid
✅ PlacingOrder_WithNoItems_Fails

❌ TestDeactivateSubscription
❌ ShouldThrowWhenPasswordTooShort
❌ DeactivateSubscription_SetsStatusToInactive
```

Rules:
- No technical terms (Test, Assert, Should, Verify)
- Present tense or readable active language
- Underscores over camelCase for readability
- Name the SUT variable `sut`

## Key Patterns

### AAA Pattern
```
// Arrange — set up SUT and dependencies
// Act — single method call on sut
// Assert — verify outcome (return value, state, or interaction)
```
Never multiple Act-Assert cycles in one test — split them.

### Object Mother
Static factory for pre-configured test objects. Eliminates setup duplication.
See `references/patterns.md` for full examples.

### Builder Pattern
Fluent builder for complex test objects with many optional fields.
See `references/patterns.md` for full examples.

### Assert Object / Custom Assertions
Encapsulate complex assertions into reusable methods.
See `references/patterns.md` for full examples.

### Humble Object
When a class mixes logic with infrastructure (I/O, UI, HTTP), extract the logic into a pure testable class. The "humble object" is the thin infrastructure wrapper.

### Functional Architecture
Separate pure logic (unit tested) from side effects (integration tested).
Pure functions → unit tests. Orchestration → integration tests.

## What NOT to Test

- Simple properties / DTOs with no logic
- Constant-returning methods
- Code where the test description is "calls method and returns what I set"
- Private methods directly — test through public behavior

## Reference Files

- `references/patterns.md` — Object Mother, Builder, Assert Object examples (multi-language)
- `references/anti-patterns.md` — Common mistakes with before/after examples
- `references/test-doubles.md` — Fake, Stub, Spy, Mock examples (multi-language)
