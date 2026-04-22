# LifeOS: The Universal Life Context Engine

> **"Life is not a single path, but a multiverse of branching possibilities. LifeOS helps you explore them before you live them."**

## 🌌 Vision & Purpose

LifeOS is a **schemaless, file-based, agentic life optimization system** that treats human life as a "multiverse" of branching possibilities across **comprehensive ontological frameworks** covering individual existence, collective systems, entity relationships, and consumer behavior.

LifeOS enables you to:

- **Simulate "What If?" Scenarios Across Life Domains**: Explore alternative futures affecting identity, biology, psychology, social connections, career, environment, values, and 40+ subdomains before making life-altering decisions.
- **Detect Cross-Domain Cognitive Dissonance**: Proactively identify conflicts between your values and actions, your neurotype and environment, your identity and social roles.
- **Visualize Your Future Self**: See the psychological, physiological, and social impact of your choices across multiple temporal horizons.
- **Model Collective Impact**: Understand how individual choices ripple through communities and systems.
- **Therapeutic Reframing**: Use ontology-guided reasoning to heal dissonance, explore identity transitions, and align actions with purpose.

### Personal Implications
- **Informed Decision-Making**: Reduce regret by simulating outcomes before committing.
- **Self-Awareness**: Gain insight into how your daily habits shape your long-term well-being.
- **Therapeutic Value**: Use the system to reframe negative thought patterns and visualize positive futures.
- **Privacy-First**: All data remains local, ensuring your personal journey stays private.

### Societal Implications
LifeOS is not just a personal tracker; it's a **civilization-scale engine** (via the `life2` ontology) that can:
- Model the impact of individual choices on collective well-being.
- Simulate policy changes at a community or societal level.
- Foster empathy by allowing users to "walk in another's shoes" via simulated timelines.
- Preserve human decision-making as a **human-readable, Git-friendly** artifact for future generations.
- Enable research into human behavior, decision-making, and well-being at scale (with user consent).

---

## 🏗️ Architecture

### Core Principles
1. **No Premature Optimization**: Uses **JSON/JSONL files** instead of databases (SQLite) for:
   - Schemaless flexibility (add fields without migration).
   - Human readability and Git compatibility.
   - Local-first privacy (data stays on your machine).
2. **Hybrid Physics Engine**: Combines:
   - **Deterministic Rules**: For tangible metrics (e.g., sleep < 6h → energy -3).
   - **LLM Reasoning**: For psychological narratives and therapeutic insights (placeholder for future API integration).
3. **Temporal Horizons**:
   - **Micro**: Daily routines (auto-archived after 2 days).
   - **Meso**: Monthly goals (auto-archived after 30 days).
   - **Macro**: Yearly visions (auto-archived after 365 days).
4. **Agent Agnostic**: Works with **any AI agent** (Hermes, Claude, etc.) via:
   - CLI for human interaction.
   - Stdio JSON-RPC protocol for agent integration.

### Directory Structure
```
~/.lifeos/
├── state.json              # Current reality (your "main branch")
├── history/                # Daily snapshots (JSONL)
├── branches/               # Active simulations
│   └── 20260420_172748_remote-work/
│       ├── branch.json     # Metadata (modifications, status)
│       └── state.json      # Simulated state
├── archive/                # Archived branches
├── horizons/               # Temporal horizon data
└── insights/               # Dissonance detection logs
```

### Ontologies (Reference-Only Guides)

LifeOS uses **comprehensive ontological frameworks** downloaded from the official repository. These are **not enforced**—they guide data organization and enable rich cross-domain reasoning. Think of them as overlapping lenses, not separate silos:

**Individual Existence**: Identity, biology, psychology, social connections, environment, lifecycle, activities, values, system interactions, metadata

**Collective Systems**: Demographics, economy, governance, environment, culture, infrastructure, provenance tracking

**Entity Relationships**: Explicit domain mappings with cardinality and cross-references (person → family → career → health → social → culture → finance → legal → technology → spirituality → environment → politics)

**Agent-Centric Modeling**: Multidimensionality, intersectionality, digital-physical hybridity, temporal dynamism, global-local nestedness, neurodiversity paradigms

**Consumer Behavior**: Hierarchical transaction classification for spending analysis

These frameworks **combine freely**—a single life state might draw from all of them simultaneously. A career change simulation could touch identity (self-concept), biology (stress response), social (professional network), finance (income volatility), and consumer behavior (spending patterns) in one branch.

**See `schemas/README.md` for complete documentation.**

### Hermes Agent Integration

LifeOS includes **Hermes Agent skills** in the `skills/` directory for deep integration:

- **`lifeos-agent-operations`** (Required): Agent-side instructions for operating LifeOS on behalf of the user. Covers schemaless logging, adaptive fidelity, multiverse simulation, and agent-curated maintenance.
- **`lifeos-agentic-operations`** (New): Enables natural language scenario exploration. Instead of requiring exact ontology paths, users can say "I'm thinking about quitting my job" and the agent maps this to ontological changes automatically.

**To install the skills:**
```bash
# Automated installer (recommended)
./scripts/install_skills.sh

# Or manual copy
cp -r ~/lifeos/skills/lifeos-agent-operations ~/.hermes/skills/productivity/
cp -r ~/lifeos/skills/lifeos-agentic-operations ~/.hermes/skills/productivity/

# Or use Hermes CLI
hermes skills install ~/lifeos/skills/lifeos-agent-operations
hermes skills install ~/lifeos/skills/lifeos-agentic-operations
```

**New Agentic Protocol Actions:**

LifeOS now exposes natural language actions via the agent protocol:

| Action | Description | Example |
|--------|-------------|---------|
| `explore_scenario` | Create branch from natural language | `{"user_input": "I want to quit my job"}` |
| `parse_intent` | Parse intent without creating branch | `{"user_input": "I need more freedom"}` |
| `compare_branches` | Compare multiple scenarios | `{"branch_ids": ["a", "b"]}` |
| `find_patterns` | Search historical patterns | `{"query": "stress after launch"}` |

See [`HERMES_INTEGRATION.md`](HERMES_INTEGRATION.md) for complete documentation.


## 💬 Agentic Interface: Talk to Your Life

LifeOS shines when used through an AI agent like Hermes. Instead of learning CLI syntax or ontology paths, you can simply talk about what's on your mind:

```bash
# Through Hermes Agent (natural language)
hermes lifeos "I'm feeling stuck in my job and wondering what else I could do"
hermes lifeos "What would my life look like if I moved to a quieter place?"
hermes lifeos "I want more time for creative projects but I'm worried about money"
hermes lifeos "Should I take that job offer or stay where I am?"
hermes lifeos "Let's explore what happens if I prioritize my health more"
```

The agent will:
1. **Listen** to your casual description
2. **Map** your words to relevant life domains (career, psychology, finance, etc.)
3. **Explore** by creating simulated branches
4. **Surface** insights: patterns, tensions, and opportunities
5. **Guide** you through options with thoughtful questions
6. **Help** you decide what to try next—all while keeping your data private

### Example Agent Interaction
```
You: "I've been thinking about quitting my job to freelance"
Agent: "I hear you're considering freelancing. Let me understand what that might look like...
        
Based on what you've said, this would affect:
• Career: employment_type → freelance  
• Finance: income volatility increases  
• Psychology: autonomy +3, initial stress +2  
• Environment: work_location → remote

I notice:
• Your current stress is 7/10 (highest in 3 months)  
• You've mentioned feeling unfulfilled 4x this month  
• On Feb 14, you felt similarly after a big project launch

Options I can model for you:
1. **Conservative**: Keep job, start freelance on weekends  
2. **Hybrid**: Part-time employment + freelance clients  
3. **Radical**: Quit and freelance full-time

Which feels most relevant to explore right now?"
```

This transforms LifeOS from a tool you operate into a **thinking partner** that helps you explore possibilities, see patterns, and make more aligned decisions—all through natural conversation.


---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9+
- `pip` or `venv`

### Quick Start
```bash
# Clone or copy the LifeOS package to your system
cd ~/lifeos

# Install the package
source venv/bin/activate # If using venv
pip install -e .

# Initialize your LifeOS instance
lifeos init

# (Optional) Install Hermes Agent skills for deep integration
./scripts/install_skills.sh
```

### Verify Installation
```bash
lifeos status
```

---

## 🛠️ Usage Guide

### 1. Check Your Current State
```bash
lifeos status
```
**Output**:
```
📊 LIFE STATUS
Name: User
Sleep: 7.0h (Quality: 7)
Stress: 5

⚠️ Dissonance Detected:
 - Work hours (40) may conflict with work-life balance.
```

### 2. Explore a New Possibility (Create a Branch)
Simulate a "4-day work week" by reducing weekly hours:
```bash
lifeos explore "4-day-week" --mod "activities_practices.work_productivity.weekly_hours=32"
```
**Output**:
```
✅ Created branch: 20260420_172243_4-day-week
 Path: /home/bot/.lifeos/branches/20260420_172243_4-day-week
```

### 3. Simulate the Branch
Run a simulation to see the psychological and physiological impact:
```bash
lifeos simulate "20260420_172243_4-day-week" --days 7
```
**Output**:
```
🔮 Simulation: 4-day-week
Based on the changes: [{'path': 'activities_practices.work_productivity.weekly_hours', 'new': 32.0}]

Psychological Projection:
- Your stress levels are at 5/10.
- Your energy levels may shift based on your 7.0h sleep average.
- Social connections might feel balanced.

Therapeutic Insight:
This simulation suggests a trade-off between productivity and well-being. 
Consider whether the short-term gain aligns with your long-term purpose.
```

### 4. Adopt the Branch (Merge into Reality)
If the simulation looks good, merge it into your real state:
```bash
lifeos adopt "20260420_172243_4-day-week"
```
**Output**:
```
✅ Adopted branch: 4-day-week
 Reality updated.
```

### 5. View Your History
```bash
cat ~/.lifeos/history/2026-04-20.jsonl
```

### 6. Agent Integration (Stdio Mode)
For use with Hermes, Claude, or any agent:
```bash
lifeos --stdio status
```
**Output**:
```
LifeOS Agent Mode: Ready
📊 LIFE STATUS
Name: User
Sleep: 7.0h (Quality: 7)
Stress: 5
```

### 7. JSON Output for Automation
```bash
lifeos status --json
```
**Output**:
```json
{
  "state": { ... },
  "insights": ["Dissonance: Work hours (40) may conflict with work-life balance."],
  "opportunities": []
}
```
### 8. Advanced: Custom Modifications

You can modify multiple fields in a single branch:
```bash
lifeos explore "balanced-life" \
 --mod "activities_practices.work_productivity.weekly_hours=30" \
 --mod "biology.sleep_patterns.average_duration_hours=8" \
 --mod "psychology.emotional_landscape.stress_level=3"
```

### 9. Ontology-Guided Scenarios

The ontological frameworks enable rich, cross-domain simulations. These frameworks **combine freely**—each scenario below draws from multiple conceptual lenses simultaneously:

**Identity Exploration**:
```bash
# Explore gender transition impacts
# (draws from: identity, biology, psychology, social_connections)
lifeos explore "authentic-self" \
 --mod "identity.names.preferred_name=Alex" \
 --mod "identity.demographics.pronouns=['they/them']" \
 --mod "identity.self_concept.gender_euphoria=8"
```

**Career Change**:
```bash
# Switch from corporate to freelance
# (draws from: career, finance, psychology, environment)
lifeos explore "freelance-life" \
 --mod "career.employment_type=freelance" \
 --mod "career.work_location=remote" \
 --mod "finance.income_volatility=high" \
 --mod "psychology.autonomy=9"
```

**Environment Change**:
```bash
# Move from urban to rural
# (draws from: environment, social_connections, biology)
lifeos explore "rural-exodus" \
 --mod "environment.physical_spaces.type=rural" \
 --mod "environment.air_quality_index=good" \
 --mod "social_connections.proximity=dispersed"
```

**Spending Analysis**:
```bash
# Analyze consumer spending patterns
# (draws from: consumer_behavior, finance, psychology)
lifeos explore "minimalist-budget" \
 --mod "spending.2.1.1_groceries=reduce_30%" \
 --mod "spending.2.1.2_prepared_consumption=eliminate"
```

---

## 🔧 Advanced Configuration

### Customizing the Physics Engine
Edit `lifeos/physics.py` to add your own deterministic rules:
```python
{
  "trigger": "biology.sleep_patterns.average_duration_hours",
  "condition": lambda v: v < 6,
  "effects": {
    "psychology.emotional_landscape.energy_level": -3,
    "biology.vital_signs.resting_heart_rate": 5
  }
}
```

### Extending the Schema
Add new fields to `schemas/life1.json` without breaking existing data. LifeOS is **schemaless** and will ignore unknown fields.

### Temporal Horizon Settings
Adjust archival thresholds in `lifeos/core.py` (default: micro=2 days, meso=30 days, macro=365 days).

### Life2 (Civilization) Integration
Future versions will allow you to:
- Simulate the impact of individual choices on societal metrics.
- Model policy changes (e.g., "What if we reduced work hours for everyone?").
- Explore collective well-being scenarios.

---

## 🧪 Testing & Verification

### Run All Commands
```bash
# Initialize
lifeos init

# Create a branch
lifeos explore "test-branch" --mod "activities_practices.work_productivity.weekly_hours=25"

# Simulate
lifeos simulate "test-branch" --days 3

# Adopt
lifeos adopt "test-branch"

# Verify state
lifeos status
```

### Verify JSON Output
```bash
lifeos status --json | jq .
```

---

## 🛡️ Privacy & Security

- **Local-First**: All data resides in `~/.lifeos/`. No cloud sync.
- **Git-Ignore**: Add `~/.lifeos/` to your `.gitignore` to prevent accidental leaks.
- **Encryption**: Future versions will support end-to-end encryption for sensitive data.
- **Data Ownership**: You own your data. It's stored in human-readable JSON, not locked in a proprietary database.

---

## 🌱 Roadmap

### Phase 1 (Current)
- ✅ Core CLI (`init`, `status`, `explore`, `simulate`, `adopt`)
- ✅ File-based storage with atomic writes
- ✅ Hybrid physics engine (deterministic + LLM placeholder)
- ✅ Agent integration (Stdio JSON-RPC)
- ✅ Comprehensive ontological frameworks for cross-domain reasoning
- ✅ Ontology-guided scenario exploration

### Phase 2 (Next)
- [ ] **LLM Integration**: Connect to real LLM APIs for dynamic narrative generation using ontological context
- [ ] **Ontology-Aware Physics**: Rules that span multiple domains (e.g., neurotype × environment × sleep → stress)
- [ ] **Identity Exploration Tools**: Specialized branches for gender, career, environment transitions
- [ ] **Dissonance Detection 2.0**: Cross-domain conflict detection using ontological relationships
- [ ] **Visualization**: Generate charts/graphs from history data mapped to ontological domains
- [ ] **Mobile App**: Sync with iOS/Android for real-time tracking
- [ ] **Advanced Physics**: Compound effects, network effects, ontology-guided rule generation

### Phase 3 (Vision)
- [ ] **Multiverse Explorer**: Interactive UI to browse all branches.
- [ ] **Collaborative Timelines**: Share branches with friends/therapists.
- [ ] **Predictive Analytics**: Forecast long-term outcomes based on historical data.
- [ ] **Global Simulation**: Model societal impacts of collective behavior changes.
- [ ] **Therapeutic Integrations**: Partner with mental health professionals to validate therapeutic value.

---

## 🤝 Contributing

LifeOS is open-source and welcomes contributions!
- **Report Bugs**: Open an issue on GitHub.
- **Suggest Features**: Propose new physics rules or ontologies.
- **Submit PRs**: Fix bugs, add features, or improve documentation.
- **Research Collaboration**: If you're a researcher interested in using LifeOS for studies, reach out!

### How to Contribute
1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Write tests.
5. Submit a pull request.

---

## 📜 License

MIT License. See `LICENSE` for details.

---

## 🙏 Acknowledgments

- **Hermes Agent**: For the CLI and agent protocol framework.
- **Pydantic**: For data validation.
- **Click**: For CLI development.
- **The User**: For the vision of a "life as a multiverse" philosophy.
- **Open Source Community**: For the tools and libraries that make this possible.

---

## 📚 Further Reading

- **LifeOS Philosophy**: Read the full vision in `VISION.md` (coming soon).
- **Life1 Ontology**: See `schemas/life1.json` for the individual schema.
- **Life2 Ontology**: See `schemas/life2.json` for the civilization schema.
- **Physics Engine**: Read `lifeos/physics.py` to understand the rule system.

---

> **"The best way to predict the future is to simulate it."**  
> — LifeOS Philosophy

---

## 📞 Support

- **Documentation**: This README.
- **Issues**: Open an issue on GitHub.
- **Discussions**: Join the community discussions.
- **Email**: [Your Contact Info]

---

**LifeOS is a work in progress. Your feedback and contributions are welcome!**
