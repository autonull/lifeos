# LifeOS Skills for Hermes Agent

This directory contains **agent-side skills** that provide deep integration between LifeOS and the Hermes Agent framework.

## Available Skills

### 1. `lifeos-agent-operations` (Required)
**Agent-side instructions** for operating LifeOS on behalf of the user. This skill tells the AI agent **how to think about** and **interact with** the LifeOS system.

**What it provides:**
- Core principles: schemaless-by-default, adaptive fidelity, agent-curated maintenance
- Agent workflows: logging user input, multiverse simulation, dissonance detection
- Tool reference: `log_event()`, `create_branch()`, `search_timeline()`, etc.
- Decision matrix: when to escalate fidelity, when to ask for confirmation
- Troubleshooting: handling schema drift, custom domains, branch maintenance
- Example agent sessions with internal reasoning traces

**When to use:**
- Always load this skill when Hermes is operating LifeOS for the user
- Ensures consistent agent behavior aligned with LifeOS philosophy
- Provides the agent with workflows for adaptive fidelity and schemaless logging

**Not for:** End users looking for installation guides (see main README.md)

---

## Installation

### Option 1: Automated Script (Recommended)
```bash
cd ~/lifeos
./scripts/install_skills.sh
```

### Option 2: Manual Copy
```bash
# Copy agent operations skill (required)
cp -r ~/lifeos/skills/lifeos-agent-operations ~/.hermes/skills/productivity/
```

### Option 3: Symlink for Development
```bash
ln -s ~/lifeos/skills/lifeos-agent-operations ~/.hermes/skills/productivity/lifeos-agent-operations
```

---

## Usage

Once installed, the skill will be automatically loaded when Hermes interacts with LifeOS. You can also explicitly preload it:

```bash
# Preload the skill
hermes -s lifeos-agent-operations

# Or in an interactive session
/skill lifeos-agent-operations
```

---

## For Skill Developers

### Structure
Each skill directory contains:
- `SKILL.md` - The main skill definition with instructions and workflows
- (Optional) `references/` - Additional reference documentation
- (Optional) `templates/` - Templates for common tasks
- (Optional) `scripts/` - Helper scripts

### Philosophy
LifeOS skills follow these principles:
1. **Agent-first**: Skills are written for the AI agent, not the end user
2. **Schemaless**: Embrace flexibility; don't enforce rigid structures
3. **Adaptive fidelity**: Start shallow, escalate structure only when needed
4. **User-curated**: Ask before deleting or archiving user data

### Contributing
When adding new features to LifeOS:
1. Does the agent need new workflows? → Update `lifeos-agent-operations`
2. Are there new tools exposed? → Add to the tools reference section
3. Are there common pitfalls? → Add to troubleshooting
4. Does the ontology evolve? → Document schema drift handling

---

## Version Compatibility

| LifeOS Version | Skill Version | Notes |
|----------------|---------------|-------|
| 1.1.0+ | 1.0.0 | Schemaless design, agent-curated maintenance |
| 1.0.0 | 0.9.0 | Original schema-enforcing version |

---

## License

These skills are part of the LifeOS project and follow the same license.
