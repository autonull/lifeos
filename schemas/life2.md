Certainly! I will design a comprehensive JSON Schema for Homo Sapiens Civilization Life, integrating standards from Schema.org, PROV-O, OWL-Time, and cultural heritage models. The main contents of the schema are as follows:

- **Schema Overview**: Introduction to the schema's purpose, design principles, and standards used.
- **Core Entity Definitions**: Detailed schemas for Persons, Organizations, Events, and Cultural Artifacts with validation rules.
- **Temporal & Spatial Modeling**: Handling time periods and geographic locations using OWL-Time and GeoJSON.
- **Relationships & Provenance**: Modeling connections and historical context using PROV-O and Schema.org properties.
- **Validation & Examples**: Implementation examples and validation rules with sample JSON data.

-------

# Comprehensive JSON Schema for Homo Sapiens Civilization Life

## 1 Schema Overview & Design Principles

This **JSON Schema** provides a structured framework for modeling the complex facets of **Homo sapiens civilization**, encompassing individuals, organizations, events, cultural artifacts, and their interrelationships across time and space. The schema integrates multiple established standards to create a **semantic, interoperable, and extensible** model suitable for research, cultural heritage applications, and historical analysis.

### 1.1 Design Philosophy

The schema is built upon these **core design principles**:

- **Interoperability**: Integrates Schema.org, PROV-O, OWL-Time, and CIDOC CRM standards for maximum compatibility with existing systems
- **Semantic Precision**: Uses defined vocabularies and ontologies to ensure unambiguous data interpretation
- **Temporal Awareness**: Incorporates comprehensive time modeling for historical events and periods
- **Provenance Tracking**: Supports the documentation of data origins and historical attribution
- **Extensibility**: Allows domain-specific customization without breaking core functionality
- **Validation-Focused**: Includes strict constraints for data quality and consistency

### 1.2 Standards Integration

The schema synthesizes several **critical standards**:

| Standard | Primary Contribution | Implementation |
| :--- | :--- | :--- |
| **Schema.org** | Core entity definitions (Person, Organization, Event, Place) | Direct type usage with property extensions |
| **PROV-O** | Provenance and attribution modeling | Entity-Activity-Agent relationships |
| **OWL-Time** | Temporal modeling and time descriptions | Time entities and duration specifications |
| **CIDOC CRM** | Cultural heritage specific relationships | Property mappings and extensions |
| **JSON-LD** | Linked Data context and semantics | Context definitions for semantic interpretation |

## 2 Core Entity Definitions

### 2.1 Person Schema

The **Person schema** extends Schema.org's Person type with additional properties for comprehensive biographical and cultural modeling.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HomoSapiensPerson",
  "description": "A human individual with biological, cultural, and historical attributes",
  "type": "object",
  "allOf": [
    {
      "$ref": "https://schema.org/Person"
    },
    {
      "properties": {
        "@context": {
          "type": "string",
          "default": "https://schema.org",
          "description": "JSON-LD context for semantic interpretation"
        },
        "@type": {
          "type": "string",
          "const": "Person"
        },
        "identifier": {
          "type": "object",
          "description": "System-specific identifiers for this person",
          "properties": {
            "wikidata": {
              "type": "string",
              "pattern": "^Q\\d+$",
              "description": "Wikidata entity identifier"
            },
            "viaf": {
              "type": "string",
              "description": "Virtual International Authority File identifier"
            },
            "orcid": {
              "type": "string",
              "pattern": "^\\d{4}-\\d{4}-\\d{4}-\\d{3}[\\dX]$",
              "description": "Open Researcher and Contributor ID"
            }
          }
        },
        "vitalStatus": {
          "type": "object",
          "description": "Life status information",
          "properties": {
            "status": {
              "type": "string",
              "enum": ["alive", "deceased", "missing", "fictional"],
              "description": "Current life status of the person"
            },
            "birthDate": {
              "type": "string",
              "format": "date",
              "description": "Date of birth in ISO 8601 format"
            },
            "birthPlace": {
              "$ref": "#/definitions/Place",
              "description": "Location where the person was born"
            },
            "deathDate": {
              "type": "string",
              "format": "date",
              "description": "Date of death in ISO 8601 format"
            },
            "deathPlace": {
              "$ref": "#/definitions/Place",
              "description": "Location where the person died"
            },
            "causeOfDeath": {
              "type": "string",
              "description": "Cause of death if known"
            }
          },
          "required": ["status"]
        },
        "biologicalAttributes": {
          "type": "object",
          "description": "Physical and biological characteristics",
          "properties": {
            "sex": {
              "type": "string",
              "enum": ["male", "female", "intersex", "other", "unknown"],
              "description": "Biological sex at birth"
            },
            "height": {
              "type": "object",
              "description": "Physical height measurements",
              "properties": {
                "value": {
                  "type": "number",
                  "minimum": 0
                },
                "unit": {
                  "type": "string",
                  "enum": ["cm", "in", "m"],
                  "default": "cm"
                }
              }
            },
            "geneticData": {
              "type": "object",
              "description": "Genetic information references",
              "properties": {
                "haplogroup": {
                  "type": "string",
                  "description": "Mitochondrial or Y-chromosome haplogroup"
                },
                "ancestryComposition": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "region": {
                        "type": "string",
                        "description": "Geographic region of ancestry"
                      },
                      "percentage": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "culturalAffiliations": {
          "type": "array",
          "description": "Cultural, ethnic, and national affiliations",
          "items": {
            "type": "object",
            "properties": {
              "group": {
                "type": "string",
                "description": "Name of cultural or ethnic group"
              },
              "role": {
                "type": "string",
                "description": "Role or status within the group"
              },
              "period": {
                "$ref": "#/definitions/TimePeriod",
                "description": "Time period of affiliation"
              }
            }
          }
        },
        "relationships": {
          "type": "array",
          "description": "Personal and familial relationships",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": ["parent", "child", "spouse", "sibling", "colleague", "mentor", "student", "friend"],
                "description": "Relationship type"
              },
              "relatedPerson": {
                "$ref": "#/definitions/PersonReference",
                "description": "Reference to related person"
              },
              "startDate": {
                "type": "string",
                "format": "date",
                "description": "When the relationship began"
              },
              "endDate": {
                "type": "string",
                "format": "date",
                "description": "When the relationship ended"
              },
              "sources": {
                "type": "array",
                "items": {
                  "type": "string",
                  "format": "uri"
                },
                "description": "Sources documenting this relationship"
              }
            }
          }
        },
        "occupations": {
          "type": "array",
          "description": "Occupations and roles throughout life",
          "items": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string",
                "description": "Job title or role"
              },
              "organization": {
                "$ref": "#/definitions/OrganizationReference",
                "description": "Employing organization"
              },
              "period": {
                "$ref": "#/definitions/TimePeriod",
                "description": "Time period of occupation"
              },
              "description": {
                "type": "string",
                "description": "Details about the occupation"
              }
            }
          }
        },
        "education": {
          "type": "array",
          "description": "Educational background",
          "items": {
            "type": "object",
            "properties": {
              "institution": {
                "$ref": "#/definitions/OrganizationReference",
                "description": "Educational institution"
              },
              "degree": {
                "type": "string",
                "description": "Degree or certificate obtained"
              },
              "field": {
                "type": "string",
                "description": "Field of study"
              },
              "period": {
                "$ref": "#/definitions/TimePeriod",
                "description": "Time period of education"
              },
              "thesis": {
                "type": "string",
                "description": "Thesis or dissertation title"
              }
            }
          }
        },
        "contributions": {
          "type": "array",
          "description": "Significant contributions and achievements",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": ["discovery", "invention", "artwork", "publication", "politicalMovement", "other"],
                "description": "Type of contribution"
              },
              "title": {
                "type": "string",
                "description": "Title or name of contribution"
              },
              "description": {
                "type": "string",
                "description": "Detailed description of contribution"
              },
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date of contribution"
              },
              "significance": {
                "type": "string",
                "enum": ["local", "regional", "global", "civilization"],
                "description": "Geographic scope of impact"
              },
              "associatedArtifacts": {
                "type": "array",
                "items": {
                  "$ref": "#/definitions/CulturalArtifactReference"
                },
                "description": "Physical or digital artifacts related to contribution"
              }
            }
          }
        },
        "provenance": {
          "$ref": "#/definitions/Provenance",
          "description": "Provenance information about this person's record"
        }
      },
      "required": ["@context", "@type", "name", "vitalStatus"]
    }
  ],
  "definitions": {
    "PersonReference": {
      "type": "object",
      "description": "Reference to a Person entity",
      "properties": {
        "@id": {
          "type": "string",
          "format": "uri",
          "description": "URI reference to the person"
        },
        "name": {
          "type": "string",
          "description": "Name of the person"
        }
      },
      "required": ["@id"]
    },
    "OrganizationReference": {
      "type": "object",
      "description": "Reference to an Organization entity",
      "properties": {
        "@id": {
          "type": "string",
          "format": "uri",
          "description": "URI reference to the organization"
        },
        "name": {
          "type": "string",
          "description": "Name of the organization"
        }
      },
      "required": ["@id"]
    },
    "Place": {
      "type": "object",
      "description": "Geographic location",
      "properties": {
        "@type": {
          "type": "string",
          "const": "Place"
        },
        "name": {
          "type": "string",
          "description": "Name of the place"
        },
        "geo": {
          "type": "object",
          "description": "Geographic coordinates",
          "properties": {
            "latitude": {
              "type": "number",
              "minimum": -90,
              "maximum": 90
            },
            "longitude": {
              "type": "number",
              "minimum": -180,
              "maximum": 180
            }
          },
          "required": ["latitude", "longitude"]
        },
        "address": {
          "type": "string",
          "description": "Human-readable address"
        },
        "administrativeArea": {
          "type": "string",
          "description": "State, province, or region"
        },
        "country": {
          "type": "string",
          "description": "Country name"
        }
      },
      "required": ["@type", "name"]
    },
    "TimePeriod": {
      "type": "object",
      "description": "Time period specification using OWL-Time",
      "properties": {
        "@type": {
          "type": "string",
          "const": "time:TemporalEntity"
        },
        "hasBeginning": {
          "type": "string",
          "format": "date-time",
          "description": "Start date and time in ISO 8601 format"
        },
        "hasEnd": {
          "type": "string",
          "format": "date-time",
          "description": "End date and time in ISO 8601 format"
        },
        "duration": {
          "type": "string",
          "description": "Duration in ISO 8601 duration format (e.g., 'P1Y2M3DT4H5M6S')"
        }
      },
      "required": ["@type"]
    },
    "CulturalArtifactReference": {
      "type": "object",
      "description": "Reference to a Cultural Artifact entity",
      "properties": {
        "@id": {
          "type": "string",
          "format": "uri",
          "description": "URI reference to the artifact"
        },
        "name": {
          "type": "string",
          "description": "Name or identifier of the artifact"
        }
      },
      "required": ["@id"]
    },
    "Provenance": {
      "type": "object",
      "description": "Provenance information following PROV-O",
      "properties": {
        "@type": {
          "type": "string",
          "const": "prov:Entity"
        },
        "wasGeneratedBy": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "@type": {
                "type": "string",
                "const": "prov:Activity"
              },
              "startedAtTime": {
                "type": "string",
                "format": "date-time"
              },
              "endedAtTime": {
                "type": "string",
                "format": "date-time"
              },
              "wasAssociatedWith": {
                "type": "array",
                "items": {
                  "type": "string",
                  "format": "uri"
                }
              }
            }
          }
        },
        "wasAttributedTo": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "URIs of agents who created or contributed to this entity"
        },
        "hadPrimarySource": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "URIs of primary sources for this information"
        }
      }
    }
  }
}
```

### 2.2 Organization Schema

The **Organization schema** models the various collective entities that structure human civilization, from informal groups to complex institutions.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HomoSapiensOrganization",
  "description": "A structured group of people with a common purpose or goal",
  "type": "object",
  "allOf": [
    {
      "$ref": "https://schema.org/Organization"
    },
    {
      "properties": {
        "@context": {
          "type": "string",
          "default": "https://schema.org"
        },
        "@type": {
          "type": "string",
          "const": "Organization"
        },
        "identifier": {
          "type": "object",
          "description": "System-specific identifiers for this organization",
          "properties": {
            "wikidata": {
              "type": "string",
              "pattern": "^Q\\d+$",
              "description": "Wikidata entity identifier"
            },
            "isni": {
              "type": "string",
              "description": "International Standard Name Identifier"
            },
            "grid": {
              "type": "string",
              "description": "Global Research Identifier Database identifier"
            }
          }
        },
        "organizationType": {
          "type": "string",
          "enum": [
            "educational",
            "governmental",
            "commercial",
            "nonprofit",
            "cultural",
            "religious",
            "political",
            "military",
            "scientific",
            "other"
          ],
          "description": "Primary type or purpose of the organization"
        },
        "foundingInfo": {
          "type": "object",
          "description": "Information about the founding of the organization",
          "properties": {
            "date": {
              "type": "string",
              "format": "date",
              "description": "Date of founding"
            },
            "place": {
              "$ref": "homoSapiensPerson.json#/definitions/Place",
              "description": "Location where the organization was founded"
            },
            "founders": {
              "type": "array",
              "items": {
                "$ref": "homoSapiensPerson.json#/definitions/PersonReference"
              },
              "description": "People who founded the organization"
            },
            "charterDocument": {
              "type": "string",
              "format": "uri",
              "description": "URI to founding charter or document"
            }
          }
        },
        "dissolutionInfo": {
          "type": "object",
          "description": "Information about the dissolution of the organization",
          "properties": {
            "date": {
              "type": "string",
              "format": "date",
              "description": "Date of dissolution"
            },
            "reason": {
              "type": "string",
              "description": "Reason for dissolution"
            },
            "successorOrganizations": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/OrganizationReference"
              },
              "description": "Organizations that succeeded this one"
            }
          }
        },
        "governanceStructure": {
          "type": "object",
          "description": "Information about how the organization is governed",
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "hierarchical",
                "collective",
                "democratic",
                "autocratic",
                "tribal",
                "other"
              ],
              "description": "Type of governance structure"
            },
            "leadership": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "string",
                    "description": "Title of leadership position"
                  },
                  "person": {
                    "$ref": "homoSapiensPerson.json#/definitions/PersonReference",
                    "description": "Person holding the position"
                  },
                  "period": {
                    "$ref": "homoSapiensPerson.json#/definitions/TimePeriod",
                    "description": "Time period of leadership"
                  }
                }
              }
            },
            "governingDocuments": {
              "type": "array",
              "items": {
                "type": "string",
                "format": "uri"
              },
              "description": "URIs to constitutions, bylaws, or other governing documents"
            }
          }
        },
        "membership": {
          "type": "object",
          "description": "Information about organization membership",
          "properties": {
            "count": {
              "type": "integer",
              "minimum": 1,
              "description": "Number of members (if known)"
            },
            "categories": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of membership category"
                  },
                  "description": {
                    "type": "string",
                    "description": "Description of membership category"
                  },
                  "rights": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Rights associated with this membership category"
                  }
                }
              }
            },
            "notableMembers": {
              "type": "array",
              "items": {
                "$ref": "homoSapiensPerson.json#/definitions/PersonReference"
              },
              "description": "Notable or historically significant members"
            }
          }
        },
        "activities": {
          "type": "array",
          "description": "Major activities and operations of the organization",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "education",
                  "research",
                  "manufacturing",
                  "trade",
                  "governance",
                  "worship",
                  "military",
                  "culturalPreservation",
                  "other"
                ],
                "description": "Type of activity"
              },
              "description": {
                "type": "string",
                "description": "Detailed description of the activity"
              },
              "period": {
                "$ref": "homoSapiensPerson.json#/definitions/TimePeriod",
                "description": "Time period when the activity was conducted"
              },
              "geographicScope": {
                "type": "string",
                "enum": ["local", "regional", "national", "international", "global"],
                "description": "Geographic scope of the activity"
              }
            }
          }
        },
        "achievements": {
          "type": "array",
          "description": "Significant achievements and contributions of the organization",
          "items": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string",
                "description": "Title of achievement"
              },
              "description": {
                "type": "string",
                "description": "Detailed description of achievement"
              },
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date of achievement"
              },
              "significance": {
                "type": "string",
                "enum": ["local", "regional", "national", "international", "global", "civilization"],
                "description": "Scope of impact"
              },
              "associatedArtifacts": {
                "type": "array",
                "items": {
                  "$ref": "homoSapiensPerson.json#/definitions/CulturalArtifactReference"
                },
                "description": "Physical or digital artifacts related to achievement"
              }
            }
          }
        },
        "subOrganizations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrganizationReference"
          },
          "description": "Departments, subsidiaries, or other sub-organizations"
        },
        "parentOrganization": {
          "$ref": "#/definitions/OrganizationReference",
          "description": "Parent organization if this is a sub-organization"
        },
        "provenance": {
          "$ref": "homoSapiensPerson.json#/definitions/Provenance",
          "description": "Provenance information about this organization's record"
        }
      },
      "required": ["@context", "@type", "name", "organizationType"]
    }
  ],
  "definitions": {
    "OrganizationReference": {
      "type": "object",
      "description": "Reference to an Organization entity",
      "properties": {
        "@id": {
          "type": "string",
          "format": "uri",
          "description": "URI reference to the organization"
        },
        "name": {
          "type": "string",
          "description": "Name of the organization"
        }
      },
      "required": ["@id"]
    }
  }
}
```

### 2.3 Event Schema

The **Event schema** models occurrences of significance to human civilization, from daily activities to historical turning points.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HomoSapiensEvent",
  "description": "An occurrence of significance in human civilization",
  "type": "object",
  "allOf": [
    {
      "$ref": "https://schema.org/Event"
    },
    {
      "properties": {
        "@context": {
          "type": "string",
          "default": "https://schema.org"
        },
        "@type": {
          "type": "string",
          "const": "Event"
        },
        "identifier": {
          "type": "object",
          "description": "System-specific identifiers for this event",
          "properties": {
            "wikidata": {
              "type": "string",
              "pattern": "^Q\\d+$",
              "description": "Wikidata entity identifier"
            },
            "viaf": {
              "type": "string",
              "description": "Virtual International Authority File identifier"
            }
          }
        },
        "eventType": {
          "type": "string",
          "enum": [
            "political",
            "military",
            "cultural",
            "religious",
            "scientific",
            "technological",
            "environmental",
            "social",
            "economic",
            "other"
          ],
          "description": "Primary type or category of the event"
        },
        "eventSubtype": {
          "type": "string",
          "description": "More specific type or subcategory of the event"
        },
        "time": {
          "$ref": "homoSapiensPerson.json#/definitions/TimePeriod",
          "description": "Temporal information about the event"
        },
        "location": {
          "$ref": "homoSapiensPerson.json#/definitions/Place",
          "description": "Location where the event occurred"
        },
        "participants": {
          "type": "array",
          "description": "Participants in the event",
          "items": {
            "type": "object",
            "properties": {
              "agent": {
                "oneOf": [
                  {
                    "$ref": "homoSapiensPerson.json#/definitions/PersonReference"
                  },
                  {
                    "$ref": "homoSapiensOrganization.json#/definitions/OrganizationReference"
                  }
                ],
                "description": "Person or organization participating"
              },
              "role": {
                "type": "string",
                "description": "Role or capacity of participation"
              },
              "significance": {
                "type": "string",
                "enum": ["primary", "secondary", "tertiary", "observer"],
                "description": "Level of participation significance"
              }
            }
          }
        },
        "causes": {
          "type": "array",
          "description": "Causes and precursors to the event",
          "items": {
            "type": "object",
            "properties": {
              "description": {
                "type": "string",
                "description": "Description of the cause"
              },
              "relatedEvents": {
                "type": "array",
                "items": {
                  "type": "string",
                  "format": "uri"
                },
                "description": "URIs to related events that caused this event"
              },
              "certainty": {
                "type": "string",
                "enum": ["certain", "probable", "possible", "disputed"],
                "description": "Level of certainty about this cause"
              }
            }
          }
        },
        "effects": {
          "type": "array",
          "description": "Effects and consequences of the event",
          "items": {
            "type": "object",
            "properties": {
              "description": {
                "type": "string",
                "description": "Description of the effect"
              },
              "relatedEvents": {
                "type": "array",
                "items": {
                  "type": "string",
                  "format": "uri"
                },
                "description": "URIs to events that were effects of this event"
              },
              "immediacy": {
                "type": "string",
                "enum": ["immediate", "short-term", "long-term", "permanent"],
                "description": "Timeframe of the effect"
              },
              "significance": {
                "type": "string",
                "enum": ["minor", "moderate", "major", "civilization-altering"],
                "description": "Magnitude of the effect"
              }
            }
          }
        },
        "narrative": {
          "type": "object",
          "description": "Narrative and interpretive information about the event",
          "properties": {
            "description": {
              "type": "string",
              "description": "Detailed narrative description of the event"
            },
            "interpretations": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "perspective": {
                    "type": "string",
                    "description": "Cultural or scholarly perspective"
                  },
                  "interpretation": {
                    "type": "string",
                    "description": "Interpretation of the event from this perspective"
                  },
                  "source": {
                    "type": "string",
                    "format": "uri",
                    "description": "URI to source of this interpretation"
                  }
                }
              }
            },
            "significance": {
              "type": "object",
              "properties": {
                "assessment": {
                  "type": "string",
                  "enum": ["local", "regional", "national", "international", "global", "civilization"],
                  "description": "Geographic scope of significance"
                },
                "reasoning": {
                  "type": "string",
                  "description": "Explanation of why the event is considered significant"
                },
                "impactAreas": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "enum": [
                      "political",
                      "social",
                      "economic",
                      "cultural",
                      "technological",
                      "environmental",
                      "religious",
                      "other"
                    ]
                  },
                  "description": "Areas of civilization affected by the event"
                }
              }
            }
          }
        },
        "sources": {
          "type": "array",
          "description": "Sources documenting the event",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "primary",
                  "secondary",
                  "archaeological",
                  "oral",
                  "other"
                ],
                "description": "Type of source"
              },
              "citation": {
                "type": "string",
                "description": "Citation information for the source"
              },
              "uri": {
                "type": "string",
                "format": "uri",
                "description": "URI to the source if available online"
              },
              "reliability": {
                "type": "string",
                "enum": ["high", "medium", "low", "uncertain"],
                "description": "Assessment of source reliability"
              }
            }
          }
        },
        "provenance": {
          "$ref": "homoSapiensPerson.json#/definitions/Provenance",
          "description": "Provenance information about this event's record"
        }
      },
      "required": ["@context", "@type", "name", "eventType", "time"]
    }
  ]
}
```

### 2.4 Cultural Artifact Schema

The **Cultural Artifact schema** models physical and digital objects created by humans that hold cultural, historical, or scientific significance.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HomoSapiensCulturalArtifact",
  "description": "An object created by humans with cultural, historical, or scientific significance",
  "type": "object",
  "allOf": [
    {
      "$ref": "https://schema.org/CreativeWork"
    },
    {
      "properties": {
        "@context": {
          "type": "string",
          "default": "https://schema.org"
        },
        "@type": {
          "type": "string",
          "const": "CreativeWork"
        },
        "identifier": {
          "type": "object",
          "description": "System-specific identifiers for this artifact",
          "properties": {
            "wikidata": {
              "type": "string",
              "pattern": "^Q\\d+$",
              "description": "Wikidata entity identifier"
            },
            "viaf": {
              "type": "string",
              "description": "Virtual International Authority File identifier"
            },
            "isbn": {
              "type": "string",
              "pattern": "^(?:ISBN(?:-1[03])?:? )?(?=[0-9X]{10}$|(?=(?:[0-9]+[- ]){3})[- 0-9X]{13}$|97[89][0-9]{10}$|(?=(?:[0-9]+[- ]){4})[- 0-9]{17}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9X]$",
              "description": "International Standard Book Number"
            },
            "doi": {
              "type": "string",
              "pattern": "^10\\.\\d{4,9}/[-._;()/:A-Z0-9]+$",
              "description": "Digital Object Identifier"
            }
          }
        },
        "artifactType": {
          "type": "string",
          "enum": [
            "tool",
            "weapon",
            "artwork",
            "document",
            "architecture",
            "pottery",
            "jewelry",
            "clothing",
            "musicalInstrument",
            "writtenWork",
            "digitalObject",
            "other"
          ],
          "description": "Primary type or category of the artifact"
        },
        "physicalCharacteristics": {
          "type": "object",
          "description": "Physical properties of the artifact",
          "properties": {
            "materials": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Materials from which the artifact is made"
            },
            "dimensions": {
              "type": "object",
              "description": "Physical dimensions of the artifact",
              "properties": {
                "height": {
                  "type": "object",
                  "properties": {
                    "value": {
                      "type": "number",
                      "minimum": 0
                    },
                    "unit": {
                      "type": "string",
                      "enum": ["mm", "cm", "m", "in", "ft"],
                      "default": "cm"
                    }
                  }
                },
                "width": {
                  "type": "object",
                  "properties": {
                    "value": {
                      "type": "number",
                      "minimum": 0
                    },
                    "unit": {
                      "type": "string",
                      "enum": ["mm", "cm", "m", "in", "ft"],
                      "default": "cm"
                    }
                  }
                },
                "depth": {
                  "type": "object",
                  "properties": {
                    "value": {
                      "type": "number",
                      "minimum": 0
                    },
                    "unit": {
                      "type": "string",
                      "enum": ["mm", "cm", "m", "in", "ft"],
                      "default": "cm"
                    }
                  }
                },
                "weight": {
                  "type": "object",
                  "properties": {
                    "value": {
                      "type": "number",
                      "minimum": 0
                    },
                    "unit": {
                      "type": "string",
                      "enum": ["mg", "g", "kg", "oz", "lb"],
                      "default": "g"
                    }
                  }
                }
              }
            },
            "condition": {
              "type": "string",
              "enum": ["excellent", "good", "fair", "poor", "fragmentary", "reconstructed"],
              "description": "Physical condition of the artifact"
            },
            "creationTechnique": {
              "type": "string",
              "description": "Technique used to create the artifact"
            }
          }
        },
        "creation": {
          "type": "object",
          "description": "Information about the creation of the artifact",
          "properties": {
            "date": {
              "type": "string",
              "format": "date",
              "description": "Date or approximate date of creation"
            },
            "place": {
              "$ref": "homoSapiensPerson.json#/definitions/Place",
              "description": "Location where the artifact was created"
            },
            "creators": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "$ref": "homoSapiensPerson.json#/definitions/PersonReference"
                  },
                  {
                    "$ref": "homoSapiensOrganization.json#/definitions/OrganizationReference"
                  }
                ]
              },
              "description": "People or organizations that created the artifact"
            },
            "culture": {
              "type": "string",
              "description": "Cultural context of creation"
            },
            "period": {
              "type": "string",
              "description": "Archaeological or historical period of creation"
            },
            "purpose": {
              "type": "string",
              "description": "Intended purpose of the artifact"
            }
          }
        },
        "discovery": {
          "type": "object",
          "description": "Information about the discovery or excavation of the artifact",
          "properties": {
            "date": {
              "type": "string",
              "format": "date",
              "description": "Date of discovery"
            },
            "place": {
              "$ref": "homoSapiensPerson.json#/definitions/Place",
              "description": "Location where the artifact was discovered"
            },
            "discoverers": {
              "type": "array",
              "items": {
                "$ref": "homoSapiensPerson.json#/definitions/PersonReference"
              },
              "description": "People who discovered the artifact"
            },
            "context": {
              "type": "string",
              "description": "Archaeological or discovery context"
            },
            "excavationDetails": {
              "type": "string",
              "description": "Details about the excavation process"
            }
          }
        },
        "ownership": {
          "type": "array",
          "description": "History of ownership and custody of the artifact",
          "items": {
            "type": "object",
            "properties": {
              "owner": {
                "oneOf": [
                  {
                    "$ref": "homoSapiensPerson.json#/definitions/PersonReference"
                  },
                  {
                    "$ref": "homoSapiensOrganization.json#/definitions/OrganizationReference"
                  }
                ],
                "description": "Current or previous owner"
              },
              "acquisitionMethod": {
                "type": "string",
                "enum": [
                  "purchase",
                  "gift",
                  "excavation",
                  "confiscation",
                  "inheritance",
                  "other"
                ],
                "description": "How the owner acquired the artifact"
              },
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date of acquisition"
              },
              "circumstances": {
                "type": "string",
                "description": "Circumstances of acquisition"
              }
            }
          }
        },
        "currentLocation": {
          "type": "object",
          "description": "Current location and custody of the artifact",
          "properties": {
            "institution": {
              "$ref": "homoSapiensOrganization.json#/definitions/OrganizationReference",
              "description": "Institution currently holding the artifact"
            },
            "location": {
              "$ref": "homoSapiensPerson.json#/definitions/Place",
              "description": "Physical location within the institution"
            },
            "accessionNumber": {
              "type": "string",
              "description": "Accession or catalog number of the artifact"
            },
            "displayStatus": {
              "type": "string",
              "enum": ["onDisplay", "inStorage", "onLoan", "inRestoration", "lost", "destroyed"],
              "description": "Current display status of the artifact"
            }
          }
        },
        "significance": {
          "type": "object",
          "description": "Cultural and historical significance of the artifact",
          "properties": {
            "assessment": {
              "type": "string",
              "enum": ["local", "regional", "national", "international", "global", "civilization"],
              "description": "Geographic scope of significance"
            },
            "reasoning": {
              "type": "string",
              "description": "Explanation of why the artifact is significant"
            },
            "culturalImportance": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Areas of cultural importance"
            },
            "researchValue": {
              "type": "string",
              "enum": ["low", "medium", "high", "exceptional"],
              "description": "Value for scientific research"
            }
          }
        },
        "digitalRepresentations": {
          "type": "array",
          "description": "Digital surrogates or representations of the artifact",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": ["image", "3DModel", "video", "audio", "metadata"],
                "description": "Type of digital representation"
              },
              "uri": {
                "type": "string",
                "format": "uri",
                "description": "URI to the digital representation"
              },
              "format": {
                "type": "string",
                "description": "File format of the digital representation"
              },
              "resolution": {
                "type": "string",
                "description": "Resolution or quality details"
              },
              "creator": {
                "type": "string",
                "description": "Creator of the digital representation"
              },
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date of digital creation"
              }
            }
          }
        },
        "provenance": {
          "$ref": "homoSapiensPerson.json#/definitions/Provenance",
          "description": "Provenance information about this artifact's record"
        }
      },
      "required": ["@context", "@type", "name", "artifactType"]
    }
  ]
}
```

## 3 Temporal and Spatial Modeling

### 3.1 Temporal Modeling with OWL-Time

The schema incorporates **OWL-Time ontology** concepts for comprehensive temporal modeling of events, periods, and durations.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HomoSapiensTemporalEntity",
  "description": "Temporal entity based on OWL-Time for describing time periods and instants",
  "type": "object",
  "properties": {
    "@context": {
      "type": "string",
      "default": "http://www.w3.org/2006/time#"
    },
    "@type": {
      "type": "string",
      "enum": ["TemporalEntity", "Instant", "Interval"],
      "description": "Type of temporal entity"
    },
    "hasBeginning": {
      "type": "object",
      "description": "Starting point of the temporal entity",
      "properties": {
        "@type": {
          "type": "string",
          "const": "Instant"
        },
        "inXSDDateTime": {
          "type": "string",
          "format": "date-time",
          "description": "DateTime in XSD format"
        },
        "inDateTime": {
          "type": "string",
          "description": "DateTime in any recognizable format"
        },
        "inTimePosition": {
          "type": "object",
          "description": "Time position using a calendar clock system",
          "properties": {
            "hasTRS": {
              "type": "string",
              "description": "Temporal reference system"
            },
            "numericPosition": {
              "type": "number",
              "description": "Numeric position on the time scale"
            }
          }
        }
      }
    },
    "hasEnd": {
      "type": "object",
      "description": "Ending point of the temporal entity",
      "properties": {
        "@type": {
          "type": "string",
          "const": "Instant"
        },
        "inXSDDateTime": {
          "type": "string",
          "format": "date-time",
          "description": "DateTime in XSD format"
        },
        "inDateTime": {
          "type": "string",
          "description": "DateTime in any recognizable format"
        }
      }
    },
    "hasDuration": {
      "type": "object",
      "description": "Duration of the temporal entity",
      "properties": {
        "@type": {
          "type": "string",
          "const": "Duration"
        },
        "xsdDuration": {
          "type": "string",
          "description": "Duration in XSD format (e.g., 'P1Y2M3DT4H5M6S')"
        },
        "months": {
          "type": "number",
          "description": "Duration in months"
        },
        "days": {
          "type": "number",
          "description": "Duration in days"
        },
        "hours": {
          "type": "number",
          "description": "Duration in hours"
        },
        "minutes": {
          "type": "number",
          "description": "Duration in minutes"
        },
        "seconds": {
          "type": "number",
          "description": "Duration in seconds"
        }
      }
    },
    "timeZone": {
      "type": "string",
      "description": "Time zone information"
    },
    "approximate": {
      "type": "boolean",
      "description": "Whether the temporal information is approximate"
    },
    "certainty": {
      "type": "string",
      "enum": ["certain", "probable", "possible", "uncertain"],
      "description": "Level of certainty about the temporal information"
    }
  },
  "required": ["@context", "@type"]
}
```

### 3.2 Geographic Location Modeling

The schema uses **GeoJSON** and **Schema.org Place** concepts for comprehensive spatial modeling.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HomoSapiensLocation",
  "description": "Geographic location with multiple coordinate systems and administrative information",
  "type": "object",
  "allOf": [
    {
      "$ref": "https://schema.org/Place"
    },
    {
      "properties": {
        "@context": {
          "type": "string",
          "default": "https://schema.org"
        },
        "@type": {
          "type": "string",
          "const": "Place"
        },
        "geo": {
          "type": "object",
          "description": "Geographic coordinates",
          "properties": {
            "@type": {
              "type": "string",
              "const": "GeoCoordinates"
            },
            "latitude": {
              "type": "number",
              "minimum": -90,
              "maximum": 90,
              "description": "Latitude in decimal degrees"
            },
            "longitude": {
              "type": "number",
              "minimum": -180,
              "maximum": 180,
              "description": "Longitude in decimal degrees"
            },
            "elevation": {
              "type": "number",
              "description": "Elevation above sea level in meters"
            },
            "coordinateSystem": {
              "type": "string",
              "enum": ["WGS84", "EPSG:4326", "other"],
              "default": "WGS84",
              "description": "Coordinate reference system"
            },
            "accuracy": {
              "type": "number",
              "description": "Accuracy of the coordinates in meters"
            }
          },
          "required": ["latitude", "longitude"]
        },
        "geojson": {
          "type": "object",
          "description": "GeoJSON geometry for more complex spatial representations",
          "properties": {
            "type": {
              "type": "string",
              "enum": ["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon", "GeometryCollection"],
              "description": "GeoJSON geometry type"
            },
            "coordinates": {
              "type": "array",
              "description": "GeoJSON coordinates array"
            }
          },
          "required": ["type", "coordinates"]
        },
        "address": {
          "type": "object",
          "description": "Postal address information",
          "properties": {
            "@type": {
              "type": "string",
              "const": "PostalAddress"
            },
            "streetAddress": {
              "type": "string",
              "description": "Street address"
            },
            "addressLocality": {
              "type": "string",
              "description": "City or locality"
            },
            "addressRegion": {
              "type": "string",
              "description": "State, province, or region"
            },
            "postalCode": {
              "type": "string",
              "description": "Postal or ZIP code"
            },
            "addressCountry": {
              "type": "string",
              "description": "Country name or ISO code"
            }
          }
        },
        "administrativeInfo": {
          "type": "object",
          "description": "Administrative and political information",
          "properties": {
            "country": {
              "type": "string",
              "description": "Sovereign country"
            },
            "countryCode": {
              "type": "string",
              "pattern": "^[A-Z]{2}$",
              "description": "ISO 3166-1 alpha-2 country code"
            },
            "administrativeDivisions": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "level": {
                    "type": "string",
                    "enum": ["first", "second", "third", "fourth"],
                    "description": "Level of administrative division"
                  },
                  "name": {
                    "type": "string",
                    "description": "Name of administrative division"
                  },
                  "code": {
                    "type": "string",
                    "description": "Administrative code"
                  }
                }
              },
              "description": "Administrative divisions containing this place"
            },
            "historicalNames": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Historical name"
                  },
                  "period": {
                    "$ref": "homoSapiensPerson.json#/definitions/TimePeriod",
                    "description": "Time period when this name was used"
                  },
                  "language": {
                    "type": "string",
                    "description": "Language of the name"
                  }
                }
              },
              "description": "Historical names for this location"
            }
          }
        },
        "environmentalContext": {
          "type": "object",
          "description": "Environmental and geographical context",
          "properties": {
            "biome": {
              "type": "string",
              "description": "Biome or ecoregion"
            },
            "climate": {
              "type": "string",
              "description": "Climate classification"
            },
            "terrain": {
              "type": "string",
              "description": "Terrain type"
            },
            "waterFeatures": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Nearby water features (rivers, lakes, oceans)"
            },
            "landmarks": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Notable natural or man-made landmarks"
            }
          }
        }
      },
      "required": ["@context", "@type", "name"]
    }
  ]
}
```

## 4 Relationships and Provenance Modeling

### 4.1 PROV-O Provenance Implementation

The schema incorporates **PROV-O ontology** for comprehensive provenance tracking and attribution.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HomoSapiensProvenance",
  "description": "Provenance information based on PROV-O for tracking entity origins and history",
  "type": "object",
  "properties": {
    "@context": {
      "type": "string",
      "default": "http://www.w3.org/ns/prov#"
    },
    "@type": {
      "type": "string",
      "const": "Entity"
    },
    "wasGeneratedBy": {
      "type": "array",
      "description": "Activities that generated this entity",
      "items": {
        "type": "object",
        "properties": {
          "@type": {
            "type": "string",
            "const": "Activity"
          },
          "@id": {
            "type": "string",
            "format": "uri",
            "description": "URI identifying the activity"
          },
          "startedAtTime": {
            "type": "string",
            "format": "date-time",
            "description": "Time when the activity started"
          },
          "endedAtTime": {
            "type": "string",
            "format": "date-time",
            "description": "Time when the activity ended"
          },
          "wasAssociatedWith": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "@type": {
                  "type": "string",
                  "const": "Agent"
                },
                "@id": {
                  "type": "string",
                  "format": "uri",
                  "description": "URI identifying the agent"
                },
                "role": {
                  "type": "string",
                  "description": "Role of the agent in the activity"
                }
              }
            },
            "description": "Agents associated with the activity"
          },
          "used": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "uri"
            },
            "description": "Entities used by the activity"
          }
        }
      }
    },
    "wasDerivedFrom": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      },
      "description": "URIs of entities from which this entity was derived"
    },
    "wasAttributedTo": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "@type": {
            "type": "string",
            "const": "Agent"
          },
          "@id": {
            "type": "string",
            "format": "uri",
            "description": "URI identifying the agent"
          },
          "role": {
            "type": "string",
            "description": "Role of the agent in creating this entity"
          }
        }
      },
      "description": "Agents to whom this entity is attributed"
    },
    "hadPrimarySource": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      },
      "description": "URIs of primary sources for this entity"
    },
    "alternates": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      },
      "description": "URIs of alternate versions of this entity"
    },
    "specializationOf": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      },
      "description": "URIs of more general entities of which this is a specialization"
    },
    "generatedAtTime": {
      "type": "string",
      "format": "date-time",
      "description": "Time when this entity was generated"
    },
    "invalidatedAtTime": {
      "type": "string",
      "format": "date-time",
      "description": "Time when this entity was invalidated"
    },
    "validFromTime": {
      "type": "string",
      "format": "date-time",
      "description": "Start time of entity validity"
    },
    "validToTime": {
      "type": "string",
      "format": "date-time",
      "description": "End time of entity validity"
    }
  },
  "required": ["@context", "@type"]
}
```

### 4.2 Cultural Heritage Relationships (CIDOC CRM)

The schema includes **CIDOC CRM** properties for specialized cultural heritage relationships.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HomoSapiensCulturalHeritageRelations",
  "description": "Specialized relationships for cultural heritage entities based on CIDOC CRM",
  "type": "object",
  "properties": {
    "crmProperties": {
      "type": "object",
      "description": "CIDOC CRM properties for cultural heritage relationships",
      "properties": {
        "P22_transferred_title_to": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "Transfer of title of ownership"
        },
        "P24_transferred_title_of": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "Object whose title was transferred"
        },
        "P31_has_modified": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "Objects that have been modified"
        },
        "P43_has_dimension": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": ["height", "width", "depth", "weight", "diameter", "length"],
                "description": "Type of dimension"
              },
              "value": {
                "type": "number",
                "description": "Numerical value of dimension"
              },
              "unit": {
                "type": "string",
                "description": "Unit of measurement"
              }
            }
          },
          "description": "Dimensions of the object"
        },
        "P44_has_condition": {
          "type": "string",
          "enum": ["excellent", "good", "fair", "poor", "fragmentary", "reconstructed"],
          "description": "Condition of the object"
        },
        "P62_depicts": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "Entities depicted by this object"
        },
        "P67_refers_to": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "Entities referred to by this object"
        },
        "P86_falls_within": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "Larger containing entity (place, collection, etc.)"
        },
        "P108i_was_produced_by": {
          "type": "string",
          "format": "uri",
          "description": "Production event that created this object"
        },
        "P130_shows_features_of": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri"
          },
          "description": "Similar objects that this object resembles"
        }
      }
    }
  }
}
```

## 5 Validation and Implementation Examples

### 5.1 Sample Person Implementation

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Leonardo da Vinci",
  "givenName": "Leonardo",
  "familyName": "da Vinci",
  "additionalName": "di ser Piero",
  "birthDate": "1452-04-15",
  "birthPlace": {
    "@type": "Place",
    "name": "Vinci",
    "address": {
      "addressLocality": "Vinci",
      "addressRegion": "Tuscany",
      "addressCountry": "Italy"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 43.7833,
      "longitude": 10.9333
    }
  },
  "deathDate": "1519-05-02",
  "deathPlace": {
    "@type": "Place",
    "name": "Clos Lucé",
    "address": {
      "addressLocality": "Amboise",
      "addressRegion": "Centre-Val de Loire",
      "addressCountry": "France"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 47.4133,
      "longitude": 0.9833
    }
  },
  "gender": "Male",
  "vitalStatus": {
    "status": "deceased",
    "birthDate": "1452-04-15",
    "birthPlace": {
      "@type": "Place",
      "name": "Vinci",
      "address": {
        "addressLocality": "Vinci",
        "addressRegion": "Tuscany",
        "addressCountry": "Italy"
      }
    },
    "deathDate": "1519-05-02",
    "deathPlace": {
      "@type": "Place",
      "name": "Clos Lucé",
      "address": {
        "addressLocality": "Amboise",
        "addressRegion": "Centre-Val de Loire",
        "addressCountry": "France"
      }
    },
    "causeOfDeath": "natural causes"
  },
  "occupations": [
    {
      "title": "Painter",
      "period": {
        "@type": "time:TemporalEntity",
        "hasBeginning": {
          "@type": "time:Instant",
          "inXSDDateTime": "1472-01-01T00:00:00Z"
        },
        "hasEnd": {
          "@type": "time:Instant",
          "inXSDDateTime": "1519-05-02T00:00:00Z"
        }
      }
    },
    {
      "title": "Engineer",
      "period": {
        "@type": "time:TemporalEntity",
        "hasBeginning": {
          "@type": "time:Instant",
          "inXSDDateTime": "1482-01-01T00:00:00Z"
        },
        "hasEnd": {
          "@type": "time:Instant",
          "inXSDDateTime": "1519-05-02T00:00:00Z"
        }
      }
    }
  ],
  "contributions": [
    {
      "type": "artwork",
      "title": "Mona Lisa",
      "description": "Portrait of Lisa Gherardini",
      "date": "1503-1506",
      "significance": "civilization",
      "associatedArtifacts": [
        {
          "@id": "http://data.europeana.eu/item/2048047/Athena_Plus_ProvidedCHO_Institut_national_d_histoire_de_l_art_5092",
          "name": "Mona Lisa"
        }
      ]
    }
  ],
  "identifier": {
    "wikidata": "Q762",
    "viaf": "24604287"
  },
  "provenance": {
    "@context": "http://www.w3.org/ns/prov#",
    "@type": "Entity",
    "wasGeneratedBy": [
      {
        "@type": "Activity",
        "startedAtTime": "2023-01-01T00:00:00Z",
        "endedAtTime": "2023-01-01T00:00:00Z",
        "wasAssociatedWith": [
          {
            "@type": "Agent",
            "@id": "http://example.org/agents/123",
            "role": "curator"
          }
        ]
      }
    ],
    "wasAttributedTo": [
      {
        "@type": "Agent",
        "@id": "http://example.org/agents/456",
        "role": "researcher"
      }
    ],
    "hadPrimarySource": [
      "https://www.wikidata.org/wiki/Q762",
      "https://viaf.org/viaf/24604287/"
    ]
  }
}
```

### 5.2 Sample Event Implementation

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "French Revolution",
  "eventType": "political",
  "eventSubtype": "revolution",
  "time": {
    "@type": "time:TemporalEntity",
    "hasBeginning": {
      "@type": "time:Instant",
      "inXSDDateTime": "1789-05-05T00:00:00Z"
    },
    "hasEnd": {
      "@type": "time:Instant",
      "inXSDDateTime": "1799-11-09T00:00:00Z"
    },
    "hasDuration": {
      "@type": "Duration",
      "xsdDuration": "P10Y6M4D"
    }
  },
  "location": {
    "@type": "Place",
    "name": "France",
    "address": {
      "addressCountry": "France"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 46.2276,
      "longitude": 2.2137
    }
  },
  "participants": [
    {
      "agent": {
        "@id": "http://example.org/people/robespierre",
        "name": "Maximilien Robespierre"
      },
      "role": "revolutionary leader",
      "significance": "primary"
    },
    {
      "agent": {
        "@id": "http://example.org/organizations/national_assembly",
        "name": "National Assembly"
      },
      "role": "governmental body",
      "significance": "primary"
    }
  ],
  "causes": [
    {
      "description": "Financial crisis due to war debts",
      "certainty": "certain"
    },
    {
      "description": "Social inequality between estates",
      "certainty": "certain"
    },
    {
      "description": "Enlightenment ideas promoting liberty and equality",
      "certainty": "probable"
    }
  ],
  "effects": [
    {
      "description": "End of the monarchy in France",
      "immediacy": "immediate",
      "significance": "civilization-altering"
    },
    {
      "description": "Rise of Napoleon Bonaparte",
      "immediacy": "long-term",
      "significance": "major"
    },
    {
      "description": "Spread of revolutionary ideas across Europe",
      "immediacy": "long-term",
      "significance": "civilization-altering"
    }
  ],
  "narrative": {
    "description": "A period of far-reaching social and political upheaval in France that lasted from 1789 until 1799, and resulted in the end of the French monarchy, the rise of Napoleon Bonaparte, and the fundamental restructuring of French society.",
    "significance": {
      "assessment": "civilization",
      "reasoning": "The French Revolution had a profound impact on world history, leading to the spread of democratic ideals and nationalism, and influencing political developments around the globe for centuries.",
      "impactAreas": [
        "political",
        "social",
        "economic",
        "cultural"
      ]
    }
  },
  "sources": [
    {
      "type": "secondary",
      "citation": "Schama, Simon. Citizens: A Chronicle of the French Revolution. Vintage, 1990.",
      "reliability": "high"
    },
    {
      "type": "primary",
      "citation": "Déclaration des droits de l'homme et du citoyen (1789)",
      "uri": "https://www.conseil-constitutionnel.fr/le-bloc-constitutionnel/textes-integrables/declaration-des-droits-de-l-homme-et-du-citoyen-de-1789",
      "reliability": "certain"
    }
  ],
  "identifier": {
    "wikidata": "Q8364"
  },
  "provenance": {
    "@context": "http://www.w3.org/ns/prov#",
    "@type": "Entity",
    "wasGeneratedBy": [
      {
        "@type": "Activity",
        "startedAtTime": "2023-06-15T00:00:00Z",
        "endedAtTime": "2023-06-15T00:00:00Z",
        "wasAssociatedWith": [
          {
            "@type": "Agent",
            "@id": "http://example.org/agents/789",
            "role": "historian"
          }
        ]
      }
    ],
    "hadPrimarySource": [
      "https://www.wikidata.org/wiki/Q8364"
    ]
  }
}
```

### 5.3 Validation Rules and Constraints

The schema includes these **validation rules** to ensure data quality:

| Rule Type | Description | Example |
| :--- | :--- | :--- |
| **Format Validation** | Ensures data matches specified formats | Dates must be ISO 8601 compliant |
| **Value Constraints** | Limits values to predefined enumerations | Gender must be from allowed values |
| **Range Validation** | Ensures numerical values within ranges | Latitude must be between -90 and 90 |
| **URI Validation** | Validates URI format and structure | Identifiers must be valid URIs |
| **Conditional Requirements** | Makes fields required based on conditions | Death place required if status is deceased |
| **Pattern Matching** | Enforces specific string patterns | Wikidata IDs must match Q\d+ pattern |

<details>
<summary>🔧 Validation Implementation Example (JavaScript)</summary>

```javascript
const Ajv = require("ajv");
const ajv = new Ajv({ allErrors: true });
const personSchema = require("./homoSapiensPerson.json");
const validate = ajv.compile(personSchema);

const validPerson = {
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Leonardo da Vinci",
  "givenName": "Leonardo",
  "familyName": "da Vinci",
  "vitalStatus": {
    "status": "deceased",
    "birthDate": "1452-04-15",
    "deathDate": "1519-05-02"
  }
};

const invalidPerson = {
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Leonardo da Vinci",
  "vitalStatus": {
    "status": "deceased",
    "birthDate": "1452-04-15",
    "deathDate": "invalid-date" // Invalid date format
  }
};

console.log("Valid person:", validate(validPerson)); // true
console.log("Invalid person errors:", validate.errors); // Array of validation errors
```

</details>

## 6 Conclusion and Future Extensions

This comprehensive JSON Schema for **Homo Sapiens Civilization Life** provides a robust foundation for modeling the complex entities and relationships that constitute human civilization. By integrating **Schema.org**, **PROV-O**, **OWL-Time**, and **CIDOC CRM** standards, the schema offers semantic richness and interoperability with existing systems.

### 6.1 Key Strengths

- **Semantic Interoperability**: Leverages established vocabularies for seamless data exchange
- **Temporal Precision**: Comprehensive time modeling for accurate historical representation
- **Provenance Tracking**: Complete lineage documentation for all entities
- **Extensibility**: Modular design allows domain-specific customization
- **Validation-Focused**: Strict constraints ensure data quality and consistency

### 6.2 Potential Extensions

Future developments could enhance the schema with:

1. **Machine Learning Integration**: Add properties for AI-generated insights and predictions
2. **Blockchain Provenance**: Incorporate immutable provenance tracking through blockchain technology
3. **3D Spatial Modeling**: Extend spatial capabilities for detailed 3D environment representation
4. **Multimedia Support**: Enhanced support for complex multimedia objects and VR/AR experiences
5. **Real-time Updates**: Incorporate capabilities for streaming and real-time data updates
6. **Privacy Controls**: Add schema properties for handling sensitive personal information

### 6.3 Implementation Considerations

When implementing this schema, consider these **best practices**:

- **Use JSON-LD Contexts**: Always include appropriate `@context` declarations for semantic interpretation
- **Validate Early and Often**: Implement validation at data entry points to prevent invalid data
- **Document Extensions**: Clearly document any custom extensions or modifications
- **Maintain Provenance**: Always include provenance information for all entities
- **Use Identifiers Consistently**: Establish and maintain consistent identifier schemes across all entities
- **Plan for Evolution**: Design systems to accommodate schema evolution without breaking existing data

This schema provides a solid foundation for the digital representation of human civilization, supporting research, education, cultural heritage preservation, and historical analysis in the digital age.