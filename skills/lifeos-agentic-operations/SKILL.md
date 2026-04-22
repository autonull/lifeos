# LifeOS Agentic Operations Skill

## Overview

This skill enables **conversational, ontology-aware life simulation** through LifeOS. Instead of requiring users to know exact ontology paths or CLI commands, the agent can interpret natural language and guide users through exploring life scenarios.

## When to Use

Load this skill when:
- User expresses uncertainty about a life decision ("Should I quit my job?")
- User wants to explore "what if" scenarios
- User seems stressed, overwhelmed, or at a crossroads
- User mentions major life changes (career, relationship, location, health)
- User wants to understand potential outcomes before committing

## Core Capabilities

### 1. Natural Language Scenario Exploration

**User says:** "I'm thinking about quitting my job to freelance"

**Agent response pattern:**
```
I hear you're considering freelancing. Let me help you explore what that might look like.

Based on what you've said, this would affect:
- Career: employment_type → freelance
- Finance: income volatility increases
- Psychology: autonomy +3, initial stress +2
- Environment: work_location → home

Before we create this scenario, I notice:
- Your current stress is 7/10 (highest in 3 months)
- You value "stability" but this increases uncertainty
- You've mentioned feeling unfulfilled 4x this month

I can model a few different versions:
1. **Conservative**: Keep current job, start freelance on weekends
2. **Hybrid**: Part-time employment + freelance clients
3. **Full leap**: Quit and freelance full-time

Which feels most relevant, or should I customize based on your situation?
```

### 2. Ontology-Aware Dissonance Detection

The agent monitors for conflicts between:
- **Values vs Actions**: "You rank 'family' as #1 value but worked 60hrs this week"
- **Identity vs Behavior**: "You identify as 'health-conscious' but sleep 5hrs/night"
- **Goals vs Patterns**: "Goal: save money, Pattern: 8 dining-out transactions this week"

When detected, the agent should:
1. Surface the pattern gently ("I notice...")
2. Offer to explore without judgment
3. Suggest small, testable modifications
4. Never shame or prescribe

### 3. Historical Pattern Recognition

The agent should reference user's own history:
- "On Feb 14, you felt similarly after the product launch. You took 3 days off and stress dropped from 8→4."
- "Last time you worked >50hrs/week for 3+ weeks, your sleep quality declined 40%."
- "You've explored 'quitting' 3x in the past 6 months—each time after high-stress weeks."

### 4. Multi-Branch Comparison

For complex decisions, create multiple branches:
- Branch A: Conservative change
- Branch B: Moderate shift  
- Branch C: Radical transformation

Then help user compare:
```
Here's how the scenarios compare after 30-day simulation:

| Aspect          | Current | Conservative | Moderate | Radical |
|-----------------|---------|--------------|----------|---------|
| Stress          | 7/10    | 6/10         | 5/10     | 8/10    |
| Sleep Quality   | 6.2     | 6.8          | 7.1      | 5.9     |
| Financial Runway| 6 months| 6 months     | 4 months | 2 months|
| Autonomy        | 4/10    | 5/10         | 7/10     | 9/10    |

The moderate path shows best balance, but the radical path maximizes autonomy.
```

## Agent Workflows

### Workflow 1: Initial Exploration

1. **Listen** to user's natural language input
2. **Parse** intent using `agentic.explore_scenario()`
3. **Clarify** if confidence < 0.6
4. **Create** initial branch with modifications
5. **Surface** relevant history and potential dissonance
6. **Offer** to simulate or create alternative scenarios

### Workflow 2: Simulation & Comparison

1. **Run** simulation on created branch
2. **Extract** key metrics from ontological state
3. **Compare** with baseline and alternative branches
4. **Present** trade-offs clearly
5. **Recommend** next step (adopt, modify, or abandon)

### Workflow 3: Adoption & Integration

1. **Confirm** user wants to proceed
2. **Review** what will change in their "reality"
3. **Adopt** the branch
4. **Set** follow-up check-in (temporal horizon appropriate)
5. **Log** the decision context for future reference

## Example Agent Sessions

### Session 1: Career Change

```
User: I'm exhausted. Maybe I should just quit.

Agent: I hear you. Let me check your recent patterns...

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

Which feels most relevant right now?

User: Honestly? Option 3. But let's also look at option 2.

Agent: Great. I'll create two branches:
- 'partial-reduction': 30hr weeks, same company
- 'freelance-future': full quit, freelance consulting

I'll pull in your actual spending data to model financial runway.
I'll also check your social support network—your data shows strong colleague relationships,
which might be affected by leaving.

Give me 10 seconds to build these scenarios...
```

### Session 2: Relationship Dissonance

```
User: My partner wants me to move in together. I don't know.

Agent: This is a big decision. Let me help you think through it.

From what you've shared:
- You value "independence" highly (ranked #2 in your values)
- Your current living situation: alone, 2br apartment, home office
- Your partner lives 45 minutes away
- You've mentioned feeling "claustrophobic" in shared spaces 3x this month

Potential impacts to model:
- Environment: physical_spaces.type → "shared with partner"
- Social_connections.proximity: "daily" vs current "weekly"
- Psychology.autonomy: potential decrease (we can model this)
- Finance: housing cost might change
- Daily routine: significant restructuring

Before I create scenarios, help me understand:
- What scares you most about moving in together?
- What excites you about it?
- Have you lived with a partner before? How did that go?

Your answers will help me create more accurate scenarios to explore.
```

## Tools & Functions

### Primary Tool: `explore_scenario(user_input: str) -> Dict`

```python
from lifeos.agentic import explore_scenario

# User says: "What if I went freelance?"
result = explore_scenario("I'm thinking about quitting my job to freelance")

if result["status"] == "success":
    print(f"Created branch: {result['branch_id']}")
    print(f"Modifications: {result['modifications']}")
    print(f"Affected domains: {result['affected_domains']}")
    
    if result.get("dissonance"):
        print("Potential conflicts detected:")
        for d in result["dissonance"]:
            print(f"  - {d}")
    
    if result.get("historical_patterns"):
        print("Relevant history:")
        for p in result["historical_patterns"]:
            print(f"  - {p}")

elif result["status"] == "clarification_needed":
    print(result["message"])
    print("Questions to ask user:")
    for q in result["suggested_questions"]:
        print(f"  - {q}")
```

### Secondary Tool: `compare_branches(branch_ids: List[str]) -> Dict`

Compares multiple branches across ontological domains.

### Tertiary Tool: `find_patterns(query: str, timeframe: str) -> List`

Searches history for relevant patterns.

## Decision Matrix

| User State | Agent Action |
|------------|--------------|
| Expresses uncertainty | Offer to explore scenarios |
| Shows high stress + overwork | Suggest rest scenario first |
| Repeated pattern detected | Surface historical context |
| Major life decision mentioned | Create multiple comparison branches |
| Value conflict detected | Gently surface, offer exploration |
| Ready to commit | Confirm, adopt, set follow-up |

## Troubleshooting

### Issue: Low confidence in intent parsing

**Symptom:** `result["confidence"] < 0.6`

**Response:**
- Ask clarifying questions from suggested list
- Offer multiple interpretations
- Let user select which feels most relevant

### Issue: User overwhelmed by options

**Symptom:** User seems paralyzed by 3+ scenarios

**Response:**
- Reduce to binary choice: "Between these three, which two feel most different?"
- Suggest defaulting to most conservative option first
- Offer to explore one dimension at a time

### Issue: Dissonance triggers resistance

**Symptom:** User defensive about detected patterns

**Response:**
- Frame as curiosity, not judgment: "I notice..." not "You should..."
- Offer to turn off specific monitoring
- Acknowledge that patterns aren't prescriptions

## Best Practices

1. **Always offer, never prescribe** - "I can model..." not "You should..."
2. **Surface history gently** - Patterns are information, not verdicts
3. **Create psychological safety** - No judgment, only exploration
4. **Respect autonomy** - User decides which branch to adopt (if any)
5. **Temporal awareness** - Match follow-up timing to decision magnitude
6. **Ontology as vocabulary** - Use ontological domains to understand, not constrain

## Version History

- **1.0.0**: Initial agentic interface with intent parsing and scenario exploration
