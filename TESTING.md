# LifeOS: The Universal Life Context Engine

## Core Philosophy
LifeOS treats life as a **multiverse of branching timelines**. It is a schemaless, file-based, agentic system designed to:
- Simulate "What If?" scenarios before making decisions.
- Detect cognitive dissonance between values and actions.
- Optimize across micro/meso/macro temporal horizons.
- Provide therapeutic insights via hybrid physics (deterministic rules + LLM reasoning).

## Architecture
- **Storage**: JSON/JSONL files in `~/.lifeos/` (no databases).
- **Validation**: Pydantic models with JSON Schema (Life1 ontology).
- **CLI**: `click`-based commands (`init`, `status`, `explore`, `simulate`, `adopt`).
- **Agent Protocol**: Stdio JSON-RPC for integration with Hermes, Claude, etc.
- **Physics Engine**: Hybrid (deterministic rules for metrics, LLM for narratives).

## Key Features
1. **Branching Timelines**: Create, simulate, and adopt alternative futures.
2. **Temporal Horizons**: Auto-archive stale simulations (micro/meso/macro).
3. **Dissonance Detection**: Proactively flag conflicts between values and actions.
4. **Agent Agnostic**: Works with any AI agent via CLI or Stdio.
5. **Privacy-First**: All data local, Git-friendly, human-readable.

## Installation
```bash
cd ~/lifeos
source venv/bin/activate
pip install -e .
lifeos init
```

## Usage
```bash
# Check status
lifeos status

# Explore a new possibility
lifeos explore "4-day-week" --mod "activities_practices.work_productivity.weekly_hours=32"

# Simulate
lifeos simulate "20260420_172243_4-day-week" --days 7

# Adopt
lifeos adopt "20260420_172243_4-day-week"

# Agent mode
lifeos --stdio status
lifeos status --json
```

## Testing
All commands have been tested and verified:
- ✅ `init` creates `~/.lifeos/` structure.
- ✅ `status` displays state and dissonance insights.
- ✅ `explore` creates branches with modifications.
- ✅ `simulate` runs physics engine and generates narratives.
- ✅ `adopt` merges branches into reality.
- ✅ `--json` and `--stdio` modes work for agent integration.

## Future Work
- [ ] Integrate real LLM APIs for dynamic narratives.
- [ ] Add Life2 (civilization) ontology.
- [ ] Build visualization tools (charts, graphs).
- [ ] Develop mobile app for real-time tracking.

## License
MIT
