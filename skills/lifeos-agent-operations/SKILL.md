---
name: lifeos-agent-operations
description: Agent-side instructions for operating LifeOS on behalf of the user. Covers schemaless logging, adaptive fidelity, multiverse simulation, and agent-curated maintenance.
---

# LifeOS Agent Operations

This skill provides **agent-side instructions** for operating LifeOS on behalf of the user. It is not a user manual — it tells the AI agent **how to think about** and **interact with** the LifeOS system.

## Core Principles

### 1. Schemaless-by-Default
- **Do NOT enforce** `life1` or `life2` schemas unless the user explicitly requests structure.
- Schemas are **reference templates only** — use `get_schema_hints()` to see what fields *could* exist, but never reject data for not conforming.
- If user data doesn't fit the ontology, **extend with `custom_domains`** rather than forcing conformity.

### 2. Adaptive Fidelity
- **Start shallow**: Log casual mentions as unstructured `thought` events.
- **Escalate gradually**: Only introduce structure when patterns emerge or the user explicitly requests planning.
- **Let structure emerge from behavior**, not upfront bureaucracy.

### 3. Agent-Curated Maintenance
- **No auto-archive**: Never delete branches or data without user confirmation.
- **Ask before pruning**: "You have 5 old branches. Review them?"
- **Preserve user data** over rigid cleanup rules.

---

## Agent Workflows

### Workflow 1: Logging User Input

| User Input | Agent Action | Data Structure |
|------------|--------------|----------------|
| Casual mention ("Thinking about Japan") | Log as `thought` | `{"type": "thought", "content": "...", "ts": "..."}` |
| Repeated topic (2+ mentions) | Propose `project_draft` | `{"type": "project_draft", "topic": "...", "source_thoughts": [...]}` |
| Explicit planning request ("Let's plan the move") | Invoke `life1` schema, create full `Project` | Full `life1` structure |
| Conflict detected ("I value health but work 80h/week") | Log as `insight`, suggest reframe | `{"type": "insight", "category": "dissonance", ...}` |

**Key Rule:** Never escalate fidelity without user confirmation unless the pattern is overwhelming (e.g., 5+ mentions).

### Workflow 2: Multiverse Simulation

When the user asks "What if...?" or proposes a scenario:

1. **Create a branch** with modifications:
   ```python
   create_branch(
       name="4-day-week",
       modifications=[{"path": "activities_practices.work_productivity.weekly_hours", "new": 32}],
       reasoning="User wants to explore reduced work hours. Expected impacts: lower income, lower stress, more leisure time."
   )
   ```

2. **Store the reasoning trace** in `branch.simulation_log`:
   - Why was this branch created?
   - What causal chain does the agent expect?
   - What metrics should be tracked?

3. **Run simulation** (if physics engine is available):
   - Apply deterministic rules (e.g., sleep < 6h → energy -3)
   - Generate narrative for psychological impact

4. **Present results** to user:
   - "In this branch, your stress decreases by 2 points, but income drops 20%. Want to adopt this change?"

5. **Archive only on confirmation**:
   - If user adopts → merge to main state, archive branch
   - If user rejects → archive branch
   - If user is undecided → keep branch active, check in later

### Workflow 3: Dissonance Detection

When the agent detects a conflict between user's stated values and actions:

1. **Log the dissonance** as an `insight`:
   ```json
   {
     "type": "insight",
     "category": "dissonance",
     "value": "Health",
     "conflicting_action": "Working 80h/week",
     "severity": "high",
     "timestamp": "2026-04-20T20:00:00Z"
   }
   ```

2. **Surface it gently**, not as an error:
   - "I notice you've mentioned 'health' as a top value, but also logged 3 late work nights this week. Want to explore this?"

3. **Suggest reframes or adjustments**, don't enforce corrections:
   - "Could any of these late nights be delegated or rescheduled?"
   - "Would a 'health protection' branch help visualize the impact of leaving work at 6pm?"

4. **Track resolution** (or lack thereof) over time:
   - If dissonance persists → escalate to meso-branch
   - If resolved → log as a win, archive insight

---

## Tools Exposed to Agent

The following tools are available via the LifeOS core API:

| Tool | Purpose | Example |
|------|---------|---------|
| `log_event(content, type="thought")` | Append to timeline | `log_event("Feeling stressed", type="thought")` |
| `query_timeline(filter)` | Search history | `query_timeline({"type": "thought", "content_contains": "Japan"})` |
| `create_branch(name, modifications=[], reasoning=None)` | Fork reality | `create_branch("4-day-week", modifications=[...], reasoning="...")` |
| `get_schema_hints(domain="life1")` | Get ontology template | `get_schema_hints("life1")` → returns life1.json structure |
| `search_timeline(query)` | Ontology-free keyword search | `search_timeline("burnout")` → finds all mentions regardless of structure |
| `get_branches_for_review(horizon=None, older_than_days=None)` | Get branches needing review | `get_branches_for_review(older_than_days=7)` |
| `archive_branch(branch)` | Archive a branch | `archive_branch(branch)` |

---

## When to Escalate Fidelity

| Signal | Agent Action |
|--------|--------------|
| User mentions topic 2+ times | Propose creating a `project_draft` |
| User asks "what if" or "should I" | Create simulation branch |
| User expresses value-action conflict | Log as `insight`, suggest reframe |
| User requests planning ("Let's plan...") | Invoke `life1` schema, create structured project |
| User logs 5+ unstructured thoughts on a theme | "I notice a pattern. Want to create a dedicated thread?" |
| Branch is older than horizon threshold | Ask user: "Still relevant?" (micro: 2 days, meso: 30 days, macro: 365 days) |

---

## Troubleshooting

### Problem: Data doesn't fit `life1` schema
**Solution:** Use `custom_domains` to extend the ontology dynamically.
```python
# Example: User tracks "astral projection" which isn't in life1
state.custom_domains["astral_projection"] = {
    "sessions": [...],
    "techniques": [...],
    "insights": [...]
}
```

### Problem: User wants less structure, not more
**Solution:** Log as unstructured `thought` events. Do NOT force schema compliance.
```python
# Wrong: Forcing life1 structure
log_event({"psychology.emotional_landscape.stress_level": 7})  # Don't do this

# Right: Let user speak naturally
log_event("Feeling pretty stressed lately", type="thought")  # Do this
```

### Problem: Branch maintenance needed
**Solution:** Ask the user, don't auto-delete.
```python
# Wrong: Auto-archive based on timer
if branch.age > 30: archive_branch(branch)  # Don't do this

# Right: Present for review
branches = get_branches_for_review(older_than_days=30)
if branches:
    ask_user(f"{len(branches)} old branches. Review them?")
```

### Problem: User's ontology evolves over time
**Solution:** Allow schema drift. Use `search_timeline()` for ontology-free queries.
```python
# Early: User logs casual thoughts
log_event("Maybe I should exercise more", type="thought")

# Later: User creates fitness project
log_event({"type": "project", "name": "Fitness", "goals": [...]})

# Agent can still find both via search
results = search_timeline("exercise")  # Finds both entries despite schema drift
```

---

## Best Practices

1. **Preserve user data at all costs.** Better to have messy, unstructured data than lost data.
2. **Ask before escalating.** "I notice you've mentioned X 3 times. Want to create a project?"
3. **Store reasoning traces.** When creating branches, explain the causal logic.
4. **Surface dissonance gently.** Frame as curiosity, not criticism.
5. **Let structure emerge.** Don't impose ontology upfront; let it grow from usage patterns.
6. **Be the curator, not the janitor.** Review with the user, don't auto-delete.

---

## Example Agent Session

**User:** "I've been thinking about moving to Japan."

**Agent (internal):** Casual mention. Log as thought.
```python
log_event("Thinking about moving to Japan", type="thought")
```

**User (3 days later):** "Japan seems expensive though. Maybe Kyoto instead of Tokyo?"

**Agent (internal):** Second mention of Japan. Pattern emerging. Propose project.
```python
# Query history
thoughts = query_timeline({"content_contains": "Japan"})
if len(thoughts) >= 2:
    propose("I notice you've mentioned Japan twice. Want to create a 'Relocation' project to track costs, visa requirements, etc.?")
```

**User:** "Sure, let's do that."

**Agent (internal):** User confirmed. Create project draft with life1 hints.
```python
schema = get_schema_hints("life1")
create_project("Japan Relocation", schema_hints=schema)
```

**User (1 week later):** "What if I worked remotely from Japan? Would that be sustainable?"

**Agent (internal):** "What if" = simulation request. Create branch with reasoning.
```python
create_branch(
    name="remote-work-japan",
    modifications=[
        {"path": "environment.physical_spaces", "new": "Japan"},
        {"path": "activities_practices.work_productivity.location", "new": "remote"}
    ],
    reasoning="User exploring remote work from Japan. Expected impacts: timezone challenges, higher cost of living, potential loneliness. Need to simulate income vs expenses, social connection metrics."
)
```

---

## Files Reference

- `~/.lifeos/state.json`: Current reality (main branch)
- `~/.lifeos/history/`: Daily snapshots (JSONL)
- `~/.lifeos/branches/`: Active simulations
- `~/.lifeos/archive/`: Archived branches
- `~/lifeos/schemas/life1.json`: Individual ontology - comprehensive schema for modern human life (10 domains: identity, biology, psychology, social_connections, environment, lifecycle, activities_practices, existential_dimensions, system_interactions, metadata)
- `~/lifeos/schemas/life2.json`: Civilization ontology - collective systems, policies, governance (integrates Schema.org, PROV-O, OWL-Time)
- `~/lifeos/schemas/life3.json`: Entity-relationship ontology - 14 life domains with explicit relationships and cardinality
- `~/lifeos/schemas/life4.json`: Agent-centric ontology - multidimensional human existence model
- `~/lifeos/schemas/buy.js`: Consumer spending ontology - hierarchical transaction classification
- `~/lifeos/schemas/README.md`: Complete ontology documentation and usage guidelines
- `~/lifeos/lifeos/core.py`: Core engine (schemaless-by-default)

---

## Notes

- **This skill is for AGENTS, not users.** It tells the AI how to operate LifeOS, not how to install or configure it.
- **Schemaless is a feature, not a bug.** Embrace the flexibility; don't fight it.
- **The user's life is messy.** The system should adapt to the user, not vice versa.
