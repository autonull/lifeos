# Hermes Integration Guide for LifeOS Agentic Interface

## Overview

LifeOS now supports **natural language scenario exploration** through an agentic interface. Instead of requiring users to know exact ontology paths or CLI commands, Hermes can now interpret conversational input and guide users through exploring life changes.

## Quick Start

### For Hermes Agents

Load the `lifeos-agentic-operations` skill and use the new agent protocol actions.

### Example: User Expresses Uncertainty

```
User: "I'm exhausted. Maybe I should just quit my job."

Hermes (using LifeOS agentic protocol):
{
  "action": "explore_scenario",
  "params": {
    "user_input": "I'm exhausted. Maybe I should just quit my job."
  }
}

Response:
{
  "status": "success",
  "data": {
    "status": "clarification_needed",
    "message": "I hear you're considering quitting. Let me understand better...",
    "detected_domains": ["career", "psychology", "biology"],
    "suggested_questions": [
      "Are you feeling burned out from overwork?",
      "Is this about the job itself, or the workload?",
      "Have you considered what you'd do next?"
    ]
  }
}
```

## Available Agent Protocol Actions

### 1. `explore_scenario` (Primary)

Natural language scenario exploration with automatic ontology mapping.

**Request:**
```json
{
  "action": "explore_scenario",
  "params": {
    "user_input": "I'm thinking about going freelance",
    "context": {
      "user_preferences": {
        "risk_tolerance": "moderate",
        "priority": "autonomy"
      }
    }
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "status": "success",
    "branch_id": "freelance-exploration-2026-04-21",
    "branch_name": "freelance-exploration",
    "modifications": [
      {"path": "career.employment_type", "new": "freelance"},
      {"path": "career.work_location", "new": "remote"}
    ],
    "affected_domains": ["career", "finance", "psychology"],
    "dissonance": [
      {
        "type": "value_conflict",
        "description": "You value 'stability' but this increases income volatility",
        "severity": "medium"
      }
    ],
    "historical_patterns": [
      "On Feb 14, you felt similarly after product launch. You took 3 days off and stress dropped from 8→4."
    ],
    "next_steps": [
      "Review the potential conflicts detected",
      "Run simulation to see projected outcomes",
      "Compare with alternative scenarios"
    ]
  }
}
```

### 2. `parse_intent`

Lightweight intent parsing without creating branches.

**Request:**
```json
{
  "action": "parse_intent",
  "params": {
    "user_input": "I want to sleep more and exercise"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "intent_type": "health_improvement",
    "modifications": [
      {"path": "biology.sleep_patterns.average_duration_hours", "new": 8},
      {"path": "biology.fitness_metrics.weekly_exercise_minutes", "new": 150}
    ],
    "affected_domains": ["biology"],
    "confidence": 0.8
  }
}
```

### 3. `compare_branches`

Compare multiple scenario branches.

**Request:**
```json
{
  "action": "compare_branches",
  "params": {
    "branch_ids": ["conservative-change", "moderate-shift", "radical-transformation"]
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "comparison": {
      "metrics": {...},
      "trade_offs": {...}
    }
  }
}
```

### 4. `find_patterns`

Search historical data for relevant patterns.

**Request:**
```json
{
  "action": "find_patterns",
  "params": {
    "query": "stress after product launch",
    "timeframe": "6months"
  }
}
```

## Agent Workflows

### Workflow 1: Career Change Exploration

```
1. User: "I'm thinking about quitting my job"

2. Hermes calls: explore_scenario(user_input)

3. LifeOS responds with:
   - Detected domains: career, psychology, finance
   - Modifications: employment_type → unemployed
   - Dissonance: conflicts with stability value
   - Historical pattern: similar feeling after last crunch

4. Hermes presents to user:
   "I hear you. Before we explore this fully, let me check your history...
   
   You mentioned feeling this way 3 times in the past 6 months,
   each after intense work periods. Last time, taking 3 days off
   helped more than thinking about quitting.
   
   Options I can model for you:
   1. Rest scenario: What if you took a week off instead?
   2. Reduction scenario: What if you went part-time?
   3. Full change: What if you actually quit?
   
   Which feels most relevant?"

5. User selects option → Create corresponding branch

6. Run simulation → Present outcomes → User decides
```

### Workflow 2: Relationship Decision

```
1. User: "My partner wants me to move in together. I don't know."

2. Hermes calls: explore_scenario(user_input)

3. LifeOS detects:
   - Domains: social_connections, environment, psychology
   - Potential dissonance: independence value vs. relationship desire
   - Missing info: user's living situation, past cohabitation experience

4. Hermes responds:
   "This is a big decision. From what you've shared:
   - You value 'independence' highly
   - You currently live alone with a home office
   - You've mentioned feeling 'claustrophobic' in shared spaces
   
   Before I model scenarios, help me understand:
   - What scares you most about moving in together?
   - What excites you about it?
   
   Your answers will help me create accurate scenarios."
```

## Response Status Codes

| Status | Meaning | Hermes Action |
|--------|---------|---------------|
| `success` | Branch created, ready for simulation | Present outcomes, offer next steps |
| `clarification_needed` | Low confidence in intent | Ask suggested questions |
| `needs_interpretation` | No clear modifications detected | Offer suggested scenarios |
| `error` | Something went wrong | Display error, suggest retry |

## Best Practices for Hermes

### 1. Always Offer, Never Prescribe

❌ "You should take the moderate path."
✅ "The moderate path shows the best balance. Would you like to explore it further?"

### 2. Surface History Gently

❌ "You always say this when stressed."
✅ "I notice you felt similarly on Feb 14th. That week, rest helped more than quitting thoughts."

### 3. Create Psychological Safety

❌ "This conflicts with your values."
✅ "I notice a potential tension between this change and what you've said matters to you. Want to explore?"

### 4. Respect Autonomy

❌ "You're not ready for this change."
✅ "Here are three scenarios with different levels of change. Which feels most relevant?"

### 5. Use Ontology as Vocabulary, Not Constraint

❌ "That's not a valid ontological path."
✅ "Based on what you've said, I can model changes to your career, environment, and psychology domains."

## Error Handling

### Low Confidence Parsing

If `confidence < 0.6`:
1. Acknowledge uncertainty
2. Ask 1-2 clarifying questions from `suggested_questions`
3. Re-parse with additional context

### Dissonance Detected

If `dissonance` array is non-empty:
1. Present gently: "I notice..."
2. Frame as information, not judgment
3. Offer to explore implications
4. Let user decide how to proceed

### Missing Context

If critical info is missing:
1. Identify what's needed
2. Ask specific, targeted questions
3. Re-run exploration with new context

## Integration with Existing LifeOS Features

### Combined with Simulation

```
1. explore_scenario() → creates branch
2. simulate() → runs temporal projection
3. Present narrative + metrics to user
4. User decides: adopt, modify, or abandon
```

### Combined with Dissonance Detection

```
1. explore_scenario() → detects value conflicts
2. Surface conflicts to user
3. Offer to create modified scenario that resolves conflict
4. Compare original vs. modified
```

### Combined with History

```
1. explore_scenario() → finds relevant patterns
2. Present: "Last time you felt this way..."
3. Offer to try what worked (or avoid what didn't)
4. Create branch incorporating historical learning
```

## Example Hermes Session

```
User: I'm exhausted. Maybe I should just quit.

Hermes: I hear you. Let me check your recent patterns...

[Calls: explore_scenario("I'm exhausted. Maybe I should just quit.")]

Your sleep quality has been declining (6.2 → 5.1 → 4.8) over the past week.
You've worked 55+ hours each week since April 1st.
Your stress level is at 8/10, highest in 3 months.

I also notice:
- You said something similar on Feb 14th (after product launch)
- That week, you took 3 days off and stress dropped to 4/10
- You didn't actually quit—you needed rest

Options I can model:
1. **Rest scenario**: What if you took a week off instead of quitting?
2. **Reduction scenario**: What if you went part-time (30hr weeks)?
3. **Radical change**: What if you actually did quit?

Which feels most relevant right now?

User: Honestly? Option 3. But let's also look at option 2.

Hermes: Great. I'll create two branches:
- 'partial-reduction': 30hr weeks, same company
- 'freelance-future': full quit, freelance consulting

I'll pull in your actual spending data to model financial runway.
I'll also check your social support network—your data shows strong
colleague relationships, which might be affected by leaving.

Give me 10 seconds to build these scenarios...

[Calls: explore_scenario for each option]

Here's what I've modeled:

**Partial Reduction (30hrs/week):**
- Income: -40%
- Stress: projected 8→5
- Sleep: projected 5.1→6.8
- Maintains colleague relationships

**Freelance Future:**
- Income: -60% initially, variable
- Stress: projected 8→6 (after 3-month adjustment)
- Autonomy: 4→9
- Loses daily colleague interaction

Both scenarios include your actual spending data and 6-month runway.
Would you like to simulate either further, or compare them side-by-side?
```

## Testing the Integration

### Manual Test

```bash
cd /home/bot/lifeos
python3 examples/agentic_demo.py
```

### Agent Protocol Test

```bash
# Send JSON-RPC request
echo '{"action": "explore_scenario", "params": {"user_input": "I want to quit"}}' | \
  python3 -m lifeos.agent_protocol
```

## Future Enhancements

- [ ] Multi-branch comparison visualization
- [ ] Temporal horizon configuration per scenario
- [ ] Integration with external data (calendar, finances)
- [ ] Collaborative scenarios (multi-user)
- [ ] Probabilistic outcome modeling
- [ ] Natural language narrative generation

## Support

For issues or questions about the agentic interface:
1. Check `/home/bot/lifeos/AGENTIC_INTERFACE.md` for design rationale
2. Review `/home/bot/lifeos/lifeos/agentic.py` for implementation
3. Load `lifeos-agentic-operations` skill for detailed workflows
