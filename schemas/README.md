# LifeOS Ontology Files

This directory contains the complete ontology files for LifeOS, downloaded from the official repository. These ontologies serve as **references and guides** for data structure - they suggest and guide organization but are **not strictly enforced**.

## Files

### Core Life Ontologies

#### `life1.json` / `life1.md` - Individual Life Ontology
- **Title**: Modern Homo Sapien Life
- **Scope**: Comprehensive schema for individual human existence
- **Domains**: 10 major domains
  - `identity` - Personal identity, demographics, self-concept
  - `biology` - Genetics, anatomy, physiology, medical history
  - `psychology` - Cognitive abilities, emotional landscape, mental models
  - `social_connections` - Family, friendships, professional networks
  - `environment` - Physical spaces, digital environment
  - `lifecycle` - Routines, life events, temporal phases
  - `activities_practices` - Work, leisure, consumption, learning
  - `existential_dimensions` - Values, meaning, purpose
  - `system_interactions` - Governance, economic, healthcare systems
  - `metadata` - Schema versioning, privacy controls
- **Format**: JSON Schema (draft-07)
- **Source**: Extracted from life1.md documentation

#### `life2.json` / `life2.md` - Civilization Ontology
- **Title**: HomoSapiensPerson / Civilization Systems
- **Scope**: Civilization-level systems, policies, collective well-being
- **Standards**: Integrates Schema.org, PROV-O, OWL-Time, CIDOC CRM
- **Key Entities**:
  - Person (with biological, cultural, historical attributes)
  - Organizations
  - Events
  - Cultural Artifacts
  - Temporal & Spatial modeling
  - Provenance tracking
- **Format**: JSON Schema with semantic web standards
- **Source**: Extracted from life2.md documentation

#### `life3.json` - Modern Human Life Ontology (Entity-Relationship Model)
- **Title**: Modern Human Life Ontology
- **Scope**: Entity-relationship model of contemporary human existence
- **Domains** (14 total):
  - identity, family, career, education, health, social, culture
  - finance, legal, technology, spirituality, environment, politics
- **Features**:
  - Explicit entity definitions with attributes
  - Relationship mappings with cardinality
  - Enumerated values for key fields
  - Cross-domain references
- **Format**: Custom JSON ontology (not JSON Schema)
- **Last Updated**: 2026-04-21

#### `life4.json` - Modern Human Life Ontology (Agent-Centric)
- **Title**: Modern Human Life Ontology (MHLO)
- **Scope**: Agent-centric view of human existence
- **Principles**:
  - Multidimensionality
  - Intersectionality
  - Digital-physical hybridity
  - Temporal dynamism
  - Global-local nestedness
- **Core Structure**:
  - `core_agent` - Central human agent with universal properties
  - `domains` - Array of domain definitions with entities and properties
- **Format**: Custom JSON ontology with nested domain structure
- **Last Updated**: 2026-04-21

### Specialized Ontologies

#### `buy.js` - Consumer Spending Ontology
- **Title**: Consumer Spending Ontology
- **Scope**: Complete classification of credit-based transactions in P2P networks
- **Structure**: Hierarchical tree (JavaScript object format)
- **Categories** (examples):
  - 2.1 Sustenance & Nutrition
    - 2.1.1 Food Acquisition (Groceries, Meal Kits, Specialty Foods)
    - 2.1.2 Prepared Consumption (Quick Service, Casual Dining, Fine Dining)
    - 2.1.3 Beverages (Coffee & Tea, Alcohol, Smoothies & Juices)
  - [Additional spending categories...]
- **Format**: JavaScript module (hierarchical tree)
- **Use Case**: Transaction categorization, spending analysis

## Usage Guidelines

### As Reference (Not Enforcement)
These ontologies are **suggestive, not prescriptive**. They:
- ✅ Guide data organization
- ✅ Provide common vocabulary
- ✅ Enable interoperability
- ✅ Suggest relationships between concepts
- ❌ Do NOT enforce rigid validation
- ❌ Do NOT reject data that doesn't conform

### Integration with LifeOS
LifeOS uses these ontologies to:
1. **Guide state structure** - The `state.json` follows life1.json domains
2. **Enable scenario modeling** - Branches can modify any ontology field
3. **Support agent reasoning** - Agents use ontology to understand life domains
4. **Facilitate queries** - Ontology paths enable structured queries

### Example Usage
```python
# Accessing ontology-guided paths
state = {
    "identity": {
        "names": {"preferred_name": "Alice"},
        "self_concept": {"values": ["creativity", "autonomy"]}
    },
    "biology": {
        "sleep_patterns": {"average_duration_hours": 7.5}
    },
    "psychology": {
        "emotional_landscape": {"stress_level": 3}
    }
}

# Modify via LifeOS CLI
# lifeos explore "less-stress" --mod "psychology.emotional_landscape.stress_level=2"
```

## Version History
- **2026-04-21**: Integrated complete ontology set from notention9 repo
  - Added life1.md, life2.md (markdown with embedded JSON schemas)
  - Added life3.json, life4.json (complete ontology files)
  - Added buy.js (consumer spending ontology)
  - Updated life1.json, life2.json with full schemas from markdown

## Source
All ontologies downloaded from:
https://github.com/autonull/notention9/tree/jules-refactor-foreach-325477532658099224/doc/ontology
