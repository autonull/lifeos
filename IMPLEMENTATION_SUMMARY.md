# LifeOS Agentic Interface - Implementation Summary

## What's New

LifeOS has been transformed from a **CLI-first tool** requiring exact ontology paths into an **agent-native conversational system** that accepts natural language and automatically maps user intents to ontological changes.

## Key Files Created/Modified

### New Files

1. **`lifeos/agentic.py`** (12.6 KB)
   - `IntentParser` class: Maps natural language to ontological domains
   - `AgenticLifeOS` class: Full conversational scenario exploration
   - Domain keyword detection for 8 ontological categories
   - Pre-built intent mappings for common life changes

2. **`skills/lifeos-agentic-operations/SKILL.md`** (9.5 KB)
   - Complete workflow documentation for Hermes agents
   - Example sessions with career change, relationship decisions
   - Decision matrix for different user states
   - Best practices for psychological safety

3. **`HERMES_INTEGRATION.md`** (10.7 KB)
   - Complete integration guide for Hermes
   - JSON-RPC protocol documentation
   - Example workflows and response formats
   - Error handling patterns

4. **`examples/agentic_demo.py`** (2.9 KB)
   - Demonstration script for intent parsing
   - Usage examples for developers

5. **`schemas/README.md`** (created earlier)
   - Documentation for 5 ontological frameworks
   - Usage guidelines and philosophy

### Modified Files

1. **`lifeos/agent_protocol.py`**
   - Added 4 new actions: `explore_scenario`, `parse_intent`, `compare_branches`, `find_patterns`
   - Imported `AgenticLifeOS` from new agentic module
   - Maintains backward compatibility with existing actions

2. **`README.md`**
   - Added agentic operations skill documentation
   - Protocol actions table
   - Installation instructions for new skill

3. **`VISION.md`** (earlier)
   - Updated to remove versioned ontology references
   - Emphasized blended conceptual frameworks

## Core Capabilities

### 1. Natural Language Intent Parsing

```python
from lifeos.agentic import IntentParser

parser = IntentParser()
result = parser.parse_intent("I'm thinking about quitting my job to freelance")

# Returns:
# {
#   "intent_type": "quit",
#   "affected_domains": ["career", "finance", "psychology"],
#   "modifications": [
#     {"path": "career.employment_type", "new": "freelance"},
#     {"path": "career.sector", "new": "self-employed"}
#   ],
#   "confidence": 0.8
# }
```

### 2. Conversational Scenario Exploration

```python
from lifeos.agentic import AgenticLifeOS

agent = AgenticLifeOS()
result = agent.conversational_explore("I'm exhausted. Maybe I should quit.")

# Returns:
# {
#   "status": "clarification_needed" | "success" | "needs_interpretation",
#   "branch_id": "...",  # if successful
#   "modifications": [...],
#   "dissonance": [...],
#   "historical_patterns": [...],
#   "suggested_questions": [...]  # if clarification needed
# }
```

### 3. Agent Protocol Actions

New JSON-RPC actions for Hermes integration:

| Action | Purpose | Example Input |
|--------|---------|---------------|
| `explore_scenario` | Full natural language exploration | `{"user_input": "I want to quit"}` |
| `parse_intent` | Lightweight intent parsing | `{"user_input": "I need sleep"}` |
| `compare_branches` | Compare scenario outcomes | `{"branch_ids": ["a", "b"]}` |
| `find_patterns` | Search historical data | `{"query": "stress after launch"}` |

## Ontological Domain Detection

The system detects 8 ontological domains from natural language:

1. **identity**: name, pronouns, age, nationality
2. **biology**: sleep, weight, health, fitness, exercise, diet
3. **psychology**: stress, mood, energy, anxiety, autonomy
4. **social_connections**: friends, family, relationships, network
5. **environment**: home, city, location, office, remote, space
6. **career**: work, job, employment, salary, income, company
7. **finance**: money, spending, savings, debt, budget, expenses
8. **existential_dimensions**: values, purpose, meaning, beliefs

## Pre-Built Intent Mappings

The system includes mappings for common life changes:

- **Career**: quit, freelance, part-time, remote work, career change
- **Environment**: move, downsize, cheaper city
- **Biology**: sleep more, exercise, lose weight
- **Psychology**: less stress, more autonomy
- **Social**: more friends, less social

Each mapping automatically translates to specific ontological paths.

## Dissonance Detection

The agentic layer integrates with LifeOS PhysicsEngine to detect:

- **Value conflicts**: Proposed change vs. stated values
- **Identity conflicts**: Change vs. self-concept
- **Pattern conflicts**: Change vs. historical behavior
- **Resource conflicts**: Change vs. available resources (time, money, energy)

## Historical Pattern Recognition

The system searches for and surfaces:

- Similar emotional states in the past
- Previous instances of considering similar changes
- Outcomes of past decisions
- Seasonal or contextual patterns

## Example User Journey

### Before (CLI-First)

```
User: "I want to explore quitting my job"
Agent: "Please specify the exact ontology path, e.g., career.employment_type"
User: "career.employment_type"
Agent: "What value should I set?"
User: "unemployed"
Agent: "Branch created: branch_123"
```

### After (Agentic)

```
User: "I'm thinking about quitting my job"
Agent: "I hear you. Let me understand what you're looking to change...
        
Based on what you've said, this would affect:
- Career: employment_type → unemployed
- Finance: income volatility increases
- Psychology: autonomy +3, initial stress +2

I notice:
- Your current stress is 7/10 (highest in 3 months)
- You've mentioned feeling unfulfilled 4x this month
- On Feb 14, you felt similarly after product launch

Options I can model:
1. Conservative: Keep job, start freelance on weekends
2. Hybrid: Part-time + freelance clients
3. Radical: Quit and freelance full-time

Which feels most relevant?"
```

## Integration with Hermes

### Skill Loading

Hermes agents should load:
- `lifeos-agent-operations`: Core operations
- `lifeos-agentic-operations`: Natural language interface

### Usage Pattern

```python
# In Hermes agent
from lifeos.agentic import explore_scenario

result = explore_scenario("I want to quit my job")

if result["status"] == "clarification_needed":
    # Ask user clarifying questions
    print(result["message"])
    for q in result["suggested_questions"]:
        print(f"  - {q}")
elif result["status"] == "success":
    # Present branch info and next steps
    print(f"Created branch: {result['branch_id']}")
    print(f"Modifications: {result['modifications']}")
    if result.get("dissonance"):
        print("Potential conflicts:")
        for d in result["dissonance"]:
            print(f"  - {d}")
```

## Design Philosophy

### Ontology as Vocabulary, Not Constraint

- Ontologies are **conceptual lenses**, not enforced schemas
- They guide structure but never reject non-conforming data
- Multiple ontologies blend freely in a single scenario

### Agent as Primary User

- System designed for **AI agent interaction**, not direct human CLI use
- Natural language is the primary interface
- CLI remains for debugging and advanced users

### Psychological Safety

- No judgment, only exploration
- Patterns are information, not verdicts
- Always offer, never prescribe
- Surface history gently

### Schemaless-by-Default

- JSON/JSONL storage, no database
- Ontologies are reference only
- Git-friendly, human-readable
- Local-first privacy

## Testing

Run the demo:
```bash
cd /home/bot/lifeos
python3 examples/agentic_demo.py
```

Test agent protocol:
```bash
echo '{"action": "explore_scenario", "params": {"user_input": "I want to quit"}}' | \
  python3 -m lifeos.agent_protocol
```

## Next Steps / Future Work

1. **Implement `compare_branches`**: Full comparison logic across ontological metrics
2. **Implement `find_patterns`**: Historical pattern search with temporal filtering
3. **Enhance dissonance detection**: Deeper integration with PhysicsEngine
4. **Natural language narratives**: LLM-generated scenario descriptions
5. **Multi-branch visualization**: Side-by-side scenario comparison UI
6. **Probabilistic modeling**: Outcome probabilities, not just deterministic rules
7. **External data integration**: Calendar, finances, health trackers

## Dependencies

- Python 3.x
- LifeOS core (`lifeos.core.LifeOS`, `lifeos.physics.PhysicsEngine`)
- No additional external dependencies

## Backward Compatibility

- All existing CLI commands continue to work
- Existing agent protocol actions unchanged
- New actions are additive
- Schema files remain reference-only

## Documentation

- `HERMES_INTEGRATION.md`: Complete integration guide
- `AGENTIC_INTERFACE.md`: Original design document
- `skills/lifeos-agentic-operations/SKILL.md`: Agent workflows
- `README.md`: Updated with agentic features
- `examples/agentic_demo.py`: Usage examples
