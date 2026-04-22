# LifeOS Agentic Interface - Quick Reference

## For Users

### What Can I Say?

**Career Changes:**
- "I'm thinking about quitting my job"
- "What if I went freelance?"
- "Should I go part-time?"
- "I want to work remotely"

**Environment:**
- "I want to move to a cheaper city"
- "What if I downsized my home?"
- "I need a home office"

**Health & Biology:**
- "I need more sleep"
- "I want to exercise more"
- "I'm stressed and need to relax"

**Social:**
- "I want more friends"
- "I need less social time"
- "Should I move closer to family?"

**General:**
- "I'm exhausted, maybe I should quit"
- "What would my life look like if...?"
- "I'm considering [any major life change]"

### What Happens Next?

1. **Agent parses your intent** → Identifies relevant life domains
2. **Creates simulation branch** → Models the change ontologically
3. **Checks for conflicts** → Surfaces value tensions, historical patterns
4. **Presents options** → Offers 2-3 scenario variations
5. **You decide** → Adopt, modify, or abandon the branch

## For Developers

### Import & Use

```python
from lifeos.agentic import IntentParser, AgenticLifeOS

# Parse intent only
parser = IntentParser()
result = parser.parse_intent("I want to quit my job")

# Full exploration
agent = AgenticLifeOS()
result = agent.conversational_explore("I want to quit my job")
```

### Response Structure

```python
{
    "status": "success" | "clarification_needed" | "needs_interpretation",
    "branch_id": "...",  # if successful
    "modifications": [
        {"path": "career.employment_type", "new": "freelance", "source": "intent:quit"}
    ],
    "affected_domains": ["career", "finance", "psychology"],
    "confidence": 0.8,
    "dissonance": [...],
    "historical_patterns": [...],
    "next_steps": [...]
}
```

### Agent Protocol Actions

```json
// Explore scenario
{"action": "explore_scenario", "params": {"user_input": "I want to quit"}}

// Parse intent only
{"action": "parse_intent", "params": {"user_input": "I need freedom"}}

// Compare branches
{"action": "compare_branches", "params": {"branch_ids": ["a", "b"]}}

// Find patterns
{"action": "find_patterns", "params": {"query": "stress", "timeframe": "6months"}}
```

## For Hermes Agents

### Load Skills

```bash
hermes skills install ~/lifeos/skills/lifeos-agentic-operations
```

### Workflow

1. User expresses uncertainty or life change consideration
2. Call `explore_scenario(user_input)`
3. If `status == "clarification_needed"`:
   - Ask suggested questions
   - Re-run with additional context
4. If `status == "success"`:
   - Present branch info
   - Surface dissonance gently
   - Offer simulation or comparison
5. User decides → adopt, modify, or abandon

### Best Practices

✅ **Do:**
- "I notice..." (surface patterns gently)
- "I can model..." (offer, don't prescribe)
- "Which feels most relevant?" (respect autonomy)
- Reference history: "On Feb 14, you felt similarly..."

❌ **Don't:**
- "You should..." (prescriptive)
- "You always..." (judgmental)
- Ignore dissonance (surface conflicts)
- Rush to adoption (let user explore)

## Ontological Domains

| Domain | Keywords | Example Changes |
|--------|----------|-----------------|
| identity | name, pronouns, age | identity update |
| biology | sleep, weight, health | sleep 8hrs, exercise |
| psychology | stress, mood, energy | reduce stress |
| social_connections | friend, family, network | more social time |
| environment | home, city, location | move, downsize |
| career | work, job, employment | quit, freelance |
| finance | money, spending, savings | reduce expenses |
| existential | values, purpose, meaning | align with values |

## Intent Mappings (Built-in)

| Natural Language | Ontological Change |
|-----------------|-------------------|
| "quit" | career.employment_type → unemployed |
| "freelance" | career.employment_type → freelance |
| "part-time" | career.employment_type → part-time |
| "remote work" | career.work_location → remote |
| "move" | environment.physical_spaces.location → ? |
| "downsize" | environment.physical_spaces.size_sqm → -30% |
| "cheaper city" | environment.cost_of_living → -25% |
| "sleep more" | biology.sleep_patterns.average_duration_hours → 8 |
| "exercise" | biology.fitness_metrics.weekly_exercise_minutes → 150 |
| "less stress" | psychology.emotional_landscape.stress_level → 3 |

## Confidence Levels

- **0.8+**: High confidence → Proceed with branch creation
- **0.6-0.8**: Moderate → May need clarification
- **<0.6**: Low → Ask clarifying questions

## Dissonance Types

1. **Value Conflict**: Change conflicts with stated values
2. **Identity Conflict**: Change conflicts with self-concept
3. **Pattern Conflict**: Change conflicts with historical behavior
4. **Resource Conflict**: Change exceeds available resources

## Example Session

```
User: "I'm exhausted. Maybe I should quit."

Agent:
- Calls: explore_scenario("I'm exhausted. Maybe I should quit.")
- Detects: career, psychology, biology domains
- Finds pattern: Similar feeling on Feb 14 (post-launch)
- Surfaces: Sleep declining (6.2→5.1→4.8), stress at 8/10
- Responds: "I hear you. Your data shows..."
- Offers: 3 scenarios (rest, reduction, radical)
- Waits: User selects which to explore
```

## Files to Know

- `lifeos/agentic.py` - Core implementation
- `lifeos/agent_protocol.py` - JSON-RPC handler
- `skills/lifeos-agentic-operations/SKILL.md` - Agent workflows
- `HERMES_INTEGRATION.md` - Integration guide
- `examples/agentic_demo.py` - Demo script

## Commands

```bash
# Run demo
python3 examples/agentic_demo.py

# Test protocol
echo '{"action": "explore_scenario", "params": {"user_input": "I want to quit"}}' | \
  python3 -m lifeos.agent_protocol

# Install skills
hermes skills install ~/lifeos/skills/lifeos-agentic-operations
```
