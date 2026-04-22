# Changelog

All notable changes to LifeOS will be documented in this file.

## [Unreleased]

### Added - Agentic Interface (2026-04-21)

#### New Modules
- **`lifeos/agentic.py`**: Core agentic interface with natural language intent parsing
  - `IntentParser` class for domain detection and intent mapping
  - `AgenticLifeOS` class for conversational scenario exploration
  - Pre-built mappings for 10+ common life change intents
  - 8 ontological domain keyword detectors

- **`skills/lifeos-agentic-operations/SKILL.md`**: Hermes skill for agentic operations
  - Complete workflows for career, relationship, and health scenarios
  - Decision matrix for different user states
  - Best practices for psychological safety
  - Example agent-user sessions

#### New Agent Protocol Actions
- **`explore_scenario`**: Natural language scenario exploration
  - Input: `{"user_input": "I'm thinking about quitting my job"}`
  - Output: Branch info, modifications, dissonance, next steps
  
- **`parse_intent`**: Lightweight intent parsing without branch creation
  - Input: `{"user_input": "I need more freedom"}`
  - Output: Parsed intent with domains and modifications

- **`compare_branches`**: Compare multiple scenario branches (placeholder)
  - Input: `{"branch_ids": ["branch1", "branch2"]}`
  - Output: Comparison metrics and trade-offs

- **`find_patterns`**: Search historical patterns (placeholder)
  - Input: `{"query": "stress after launch", "timeframe": "6months"}`
  - Output: Matching historical patterns

#### Documentation
- **`HERMES_INTEGRATION.md`**: Complete integration guide for Hermes agents
  - Protocol action documentation
  - Example workflows and sessions
  - Error handling patterns
  - Best practices for agent behavior

- **`IMPLEMENTATION_SUMMARY.md`**: Implementation overview
  - What's new and why
  - Core capabilities explained
  - Example user journeys (before/after)
  - Testing instructions

- **`QUICK_REFERENCE.md`**: Quick reference card
  - User-facing examples
  - Developer API reference
  - Ontological domain cheat sheet
  - Common intent mappings

- **`examples/agentic_demo.py`**: Demo script
  - Intent parser demonstration
  - Scenario exploration examples

#### Updated Documentation
- **`README.md`**: Added agentic interface section
  - New skill installation instructions
  - Protocol actions table
  - Link to integration guide

- **`VISION.md`**: Removed versioned ontology references
  - Emphasized blended conceptual frameworks
  - Aligned with agentic-first philosophy

- **`schemas/README.md`**: Ontology documentation
  - 5 ontological frameworks documented
  - Usage philosophy clarified

### Changed
- **`lifeos/agent_protocol.py`**: Enhanced with agentic actions
  - Added `AgenticLifeOS` import
  - Implemented 4 new protocol actions
  - Maintains backward compatibility

### Philosophy
- **Ontologies as vocabulary, not constraints**: Reference-only guides that blend freely
- **Agent as primary user**: Natural language interface over CLI
- **Psychological safety**: No judgment, only exploration
- **Schemaless-by-default**: JSON storage, no enforcement

### Technical Details
- **No breaking changes**: All existing CLI and protocol actions continue to work
- **No new dependencies**: Uses existing LifeOS core modules
- **Python 3.x**: Compatible with current LifeOS requirements
- **Backward compatible**: Existing integrations unaffected

### Future Work (Not Yet Implemented)
- [ ] Full `compare_branches` implementation with ontological metrics
- [ ] Full `find_patterns` implementation with temporal filtering
- [ ] Enhanced dissonance detection with multi-domain conflict resolution
- [ ] LLM-generated natural language narratives for scenarios
- [ ] Multi-branch visualization and comparison UI
- [ ] Probabilistic outcome modeling
- [ ] External data integration (calendar, finances, health trackers)

---

## [Previous Versions]

### [1.0.0] - Initial Release
- Core LifeOS functionality
- CLI interface
- Basic agent protocol (status, create_branch, simulate, adopt)
- Physics engine with dissonance detection
- Branch/simulation architecture
- Ontology schemas (life1-4, buy.js)

---

## Version Numbering

LifeOS uses semantic versioning: `MAJOR.MINOR.PATCH`
- **MAJOR**: Breaking changes to core architecture or data model
- **MINOR**: New features, backward-compatible additions
- **PATCH**: Bug fixes and documentation updates

The agentic interface is a MINOR release (new feature, backward-compatible).
