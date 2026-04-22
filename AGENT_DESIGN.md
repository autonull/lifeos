# LifeOS Agentic Interface Design

## The Problem: CLI-First is Agent-Hostile

Current LifeOS expects agents to:
1. Know exact ontology paths (`biology.sleep_patterns.average_duration_hours`)
2. Manually construct modification objects
3. Understand the entire ontological structure
4. Parse CLI output or basic JSON-RPC

This is like expecting a human to speak SQL instead of English.

## Solution: Conversational Agentic Layer

### 1. Natural Language Intent Parsing

**User says:** "I'm thinking about quitting my job to freelance. What would that look like?"

**LifeOS should:**
- Map "quitting job to freelance" → ontological changes:
  - `career.employment_type`: "employee" → "freelance"
  - `career.sector`: "private" → "self-employed"
  - `finance.income_volatility`: "low" → "high"
  - `psychology.autonomy`: +3
  - `psychology.stress_level`: +2 (initially)
  - `activities_practices.work_productivity.weekly_hours`: variable
  - `environment.work_location`: "office" → "home"
- Surface relevant history: "Last time you had high stress, your sleep quality dropped 40%"
- Generate comparison scenarios
- Detect dissonance: "You value 'stability' but this increases income volatility"

### 2. Ontology-Aware Semantic Search

Instead of keyword search, use ontological relationships:

```python
# Current: dumb string search
search_timeline("stress")

# Better: ontology-aware traversal
# "Show me times when high work hours led to poor sleep"
search_timeline(
  condition="activities_practices.work_productivity.weekly_hours > 50",
  correlate="biology.sleep_patterns.quality_score",
  timeframe="last_6_months"
)
```

### 3. Dissonance Detection as Proactive Agent

Current: User must run `lifeos status` to see dissonance

Better: Agent continuously monitors and surfaces insights:

```python
# Agent-initiated conversation
Agent: "I notice you've logged 'exhausted' 4 days in a row. Your sleep quality is down to 5.2/10. 
        Your calendar shows 3 late nights this week. Want to explore what happens if you decline Thursday's meeting?"
```

### 4. Scenario Generation (Not Just Modification)

Current: User must specify exact modifications

Better: Agent generates scenarios from intent:

```python
# User: "What if I moved to a cheaper city?"
Agent generates scenario exploring:
  - environment.cost_of_living_index: -30%
  - finance.housing_cost: -40%
  - social_connections.proximity: "dispersed" (from friends/family)
  - psychology.belonging: -2 (initially)
  - career.remote_work_compatibility: required
  - environment.climate, walkability, air_quality, etc.
```

### 5. Cross-Domain Reasoning

Current: Each domain is siloed

Better: Agent understands cascading effects:

```python
# Rule: neurotype × environment × sleep → stress
if state.identity.neurotype == "ADHD" and 
   state.environment.sensory_input == "high" and 
   state.biology.sleep_patterns.duration < 7:
   
   # Agent suggests: 
   "People with ADHD often struggle with stress when sleep-deprived in high-stimulus environments.
    Your data shows this pattern 3x this month. Consider:
    - Noise-canceling headphones (environment modification)
    - Earlier wind-down routine (biology modification)
    - Declining Thursday's crowded event (social modification)"
```

### 6. Temporal Horizon Awareness

Current: Manual horizon specification

Better: Agent understands temporal context:

```python
# Micro (daily): "You're tired today. Skip the gym?"
# Meso (monthly): "You've worked 60hr weeks for 3 weeks. Burnout risk: high"
# Macro (yearly): "Your 'creativity' value ranks #1, but you've spent 0 hours on creative pursuits this year"
```

### 7. Agent-to-Agent Protocols

Current: Basic stdio JSON-RPC

Better: Rich agent protocols:

```json
{
  "action": "explore_intent",
  "intent": "career_change",
  "natural_language": "What if I quit to freelance?",
  "context": {
    "user_values": ["autonomy", "creativity", "stability"],
    "current_state_summary": {...},
    "relevant_history": [...]
  },
  "expected_response": {
    "ontology_changes": [...],
    "affected_domains": ["career", "finance", "psychology", "social_connections"],
    "potential_dissonance": ["stability vs autonomy"],
    "historical_patterns": [...],
    "suggested_scenarios": [
      {"name": "conservative-freelance", "changes": [...]},
      {"name": "full-leap", "changes": [...]}
    ]
  }
}
```

## Implementation Plan

### Phase 1: Intent Parser
- Map natural language to ontological paths
- Handle synonyms, colloquialisms, incomplete specifications
- Generate clarification questions when ambiguous

### Phase 2: Ontology Navigator
- Build graph of ontological relationships
- Enable cross-domain queries
- Surface related concepts automatically

### Phase 3: Proactive Agent
- Continuous monitoring with smart thresholds
- Contextual timing for interventions
- Personalized insight generation

### Phase 4: Scenario Engine
- Generate complete scenarios from minimal input
- Auto-surface relevant historical patterns
- Multi-branch comparison

### Phase 5: Conversational Memory
- Remember past explorations
- Reference previous decisions
- Build narrative continuity

## Example Conversational Flow

```
User: "I'm exhausted. Maybe I should just quit."

Agent: "I hear you. Let me check your recent patterns...

Your sleep quality has been declining (6.2 → 5.1 → 4.8) over the past week.
You've worked 55+ hours each week since April 1st.
Your stress level is at 8/10, highest in 3 months.

Before we explore 'quitting', I notice:
- You said something similar on Feb 14th (after the product launch crunch)
- That week, you took 3 days off and your stress dropped to 4/10
- You didn't actually want to quit—you wanted rest

Options I can help you explore:
1. **Rest scenario**: What if you took a week off instead of quitting?
2. **Reduction scenario**: What if you went part-time (30hr weeks)?
3. **Radical change**: What if you actually did quit? (Let's model this fully)

Which feels most relevant right now?"

User: "Honestly? Option 3. But let's also look at option 2."

Agent: "Great. I'll create two branches:
- 'partial-reduction': 30hr weeks, same company
- 'freelance-future': full quit, freelance consulting

I'll pull in your actual spending data (from buy.js ontology) to model financial runway.
I'll also check your social support network—your data shows strong colleague relationships,
which might be affected by leaving.

Give me 10 seconds to build these scenarios..."
````

## Key Insight

The ontologies aren't just data structures—they're the **vocabulary** the agent uses to understand human life. The agent should be fluent in this vocabulary, translating between human intent and ontological precision automatically.

Current LifeOS: Human must learn ontology paths
Better LifeOS: Ontology learns human intent
