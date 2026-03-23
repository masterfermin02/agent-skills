# Agent Skills

Custom OpenClaw agent skills built by [@masterfermin02](https://github.com/masterfermin02).

## Available Skills

| Skill | Description |
|-------|-------------|
| [unit-testing](./unit-testing/) | Framework-agnostic unit testing best practices (AAA, Object Mother, Builder, test doubles, anti-patterns) |
| [csharp-unit-testing](./csharp-unit-testing/) | C#-specific unit testing with xUnit, Moq, and FluentAssertions |

---

## Installation

### Option 1 — Install via skills.sh

```bash
npx skillsadd masterfermin02/agent-skills
```

### Option 2 — Install via ClaWHub

```bash
npx clawhub@latest install masterfermin02/agent-skills
```

### Option 3 — Install a single skill

```bash
# Install only the unit-testing skill
npx skillsadd masterfermin02/agent-skills --skill unit-testing

# Install only the C# skill
npx skillsadd masterfermin02/agent-skills --skill csharp-unit-testing
```

### Option 4 — Manual install

Clone the repo and copy the skill folder into your agent's skills directory:

```bash
git clone https://github.com/masterfermin02/agent-skills.git
cp -r agent-skills/unit-testing ~/.openclaw/skills/
```

---

## Structure

Each skill follows the [AgentSkills spec](https://openclaw.ai):

```
skill-name/
├── SKILL.md              — trigger description + workflow instructions
└── references/           — detailed reference material loaded on demand
    ├── patterns.md
    ├── anti-patterns.md
    └── test-doubles.md
```

---

## Contributing

Found a bug or want to improve a skill? PRs welcome.
