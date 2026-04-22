> Life/Modern living as a Homo Sapien - as a complete, comprehensive JSON Schema

I'll create a comprehensive JSON Schema representing modern human life. This will be a detailed, structured representation covering all major aspects of contemporary Homo sapien existence.

This comprehensive JSON Schema captures modern human life across **10 major domains**:

1. **Identity** — Legal names, demographics, digital identities, self-concept, personality frameworks
2. **Biology** — Genetics, anatomy, physiology, medical history, sensory systems, reproductive health, longevity markers
3. **Psychology** — Cognitive abilities, emotional landscape, consciousness states, mental models, subjective wellbeing
4. **Social Connections** — Family structures, friendship networks, professional relationships, community belonging, social capital
5. **Environment** — Physical spaces, socioeconomic context, material possessions, environmental exposures, digital environment
6. **Lifecycle** — Developmental stages, life events, daily routines, time perception, mortality awareness
7. **Activities & Practices** — Work, leisure, maintenance tasks, consumption patterns, spiritual practices, learning
8. **Existential Dimensions** — Sources of meaning, values hierarchy, life projects, transcendence connection, moral frameworks
9. **System Interactions** — Governance, economic systems, healthcare, education, digital infrastructure engagement
10. **Metadata** — Schema versioning, privacy controls, data completeness

The schema is designed to be **extensible**, **privacy-conscious** (with encryption flags and privacy levels), and **culturally neutral** while capturing the full complexity of 21st-century human existence—from biometric data and epigenetic markers to social media presence and algorithmic exposure.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://homo-sapiens.life/modern-living-schema.json",
  "title": "Modern Homo Sapien Life",
  "description": "A comprehensive schema representing the complete experience of modern human life",
  "type": "object",
  "required": ["identity", "biology", "psychology", "social_connections", "environment", "lifecycle"],
  "properties": {
    "identity": {
      "type": "object",
      "title": "Personal Identity",
      "description": "Core identifiers and self-concept",
      "properties": {
        "names": {
          "type": "object",
          "properties": {
            "legal_name": { "type": "string" },
            "preferred_name": { "type": "string" },
            "nicknames": { "type": "array", "items": { "type": "string" } },
            "cultural_names": { "type": "array", "items": { "type": "string" } }
          }
        },
        "demographics": {
          "type": "object",
          "properties": {
            "birth_date": { "type": "string", "format": "date" },
            "age_years": { "type": "integer", "minimum": 0, "maximum": 125 },
            "sex_at_birth": { "enum": ["male", "female", "intersex"] },
            "gender_identity": { "type": "string" },
            "pronouns": { "type": "array", "items": { "type": "string" } },
            "nationality": { "type": "string" },
            "ethnicity": { "type": "array", "items": { "type": "string" } },
            "languages": { "type": "array", "items": { "type": "string" } },
            "primary_language": { "type": "string" }
          }
        },
        "identifiers": {
          "type": "object",
          "properties": {
            "national_id": { "type": "string" },
            "passport_numbers": { "type": "array", "items": { "type": "string" } },
            "social_security": { "type": "string" },
            "digital_identities": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "platform": { "type": "string" },
                  "username": { "type": "string" },
                  "verified": { "type": "boolean" }
                }
              }
            },
            "biometric_data": {
              "type": "object",
              "properties": {
                "fingerprints": { "type": "boolean" },
                "facial_recognition_template": { "type": "boolean" },
                "dna_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
                "retinal_scan": { "type": "boolean" }
              }
            }
          }
        },
        "self_concept": {
          "type": "object",
          "properties": {
            "values": { "type": "array", "items": { "type": "string" } },
            "beliefs": {
              "type": "object",
              "properties": {
                "religious": { "type": "string" },
                "spiritual": { "type": "string" },
                "philosophical": { "type": "string" },
                "political": { "type": "string" }
              }
            },
            "personality_traits": {
              "type": "object",
              "properties": {
                "big_five": {
                  "type": "object",
                  "properties": {
                    "openness": { "type": "number", "minimum": 0, "maximum": 100 },
                    "conscientiousness": { "type": "number", "minimum": 0, "maximum": 100 },
                    "extraversion": { "type": "number", "minimum": 0, "maximum": 100 },
                    "agreeableness": { "type": "number", "minimum": 0, "maximum": 100 },
                    "neuroticism": { "type": "number", "minimum": 0, "maximum": 100 }
                  }
                },
                "mbti": { "type": "string", "pattern": "^[IE][NS][FT][JP]$" },
                "other_frameworks": { "type": "object" }
              }
            },
            "life_narrative": { "type": "string" },
            "future_aspirations": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },
    "biology": {
      "type": "object",
      "title": "Biological Systems",
      "properties": {
        "genetics": {
          "type": "object",
          "properties": {
            "genome_sequence": { "type": "string" },
            "ancestry_composition": {
              "type": "object",
              "additionalProperties": { "type": "number", "minimum": 0, "maximum": 1 }
            },
            "known_mutations": { "type": "array", "items": { "type": "string" } },
            "epigenetic_markers": { "type": "object" },
            "telomere_length": { "type": "number" }
          }
        },
        "anatomy": {
          "type": "object",
          "properties": {
            "height_cm": { "type": "number", "minimum": 30, "maximum": 300 },
            "weight_kg": { "type": "number", "minimum": 1, "maximum": 600 },
            "body_composition": {
              "type": "object",
              "properties": {
                "fat_percentage": { "type": "number", "minimum": 0, "maximum": 100 },
                "muscle_mass_kg": { "type": "number" },
                "bone_density": { "type": "number" },
                "water_percentage": { "type": "number", "minimum": 0, "maximum": 100 }
              }
            },
            "organ_status": {
              "type": "object",
              "properties": {
                "brain": { "$ref": "#/definitions/organHealth" },
                "heart": { "$ref": "#/definitions/organHealth" },
                "lungs": { "$ref": "#/definitions/organHealth" },
                "liver": { "$ref": "#/definitions/organHealth" },
                "kidneys": { "$ref": "#/definitions/organHealth" },
                "digestive_system": { "$ref": "#/definitions/organHealth" },
                "reproductive_system": { "$ref": "#/definitions/organHealth" },
                "immune_system": { "$ref": "#/definitions/organHealth" },
                "endocrine_system": { "$ref": "#/definitions/organHealth" },
                "nervous_system": { "$ref": "#/definitions/organHealth" },
                "skeletal_system": { "$ref": "#/definitions/organHealth" },
                "muscular_system": { "$ref": "#/definitions/organHealth" },
                "integumentary_system": { "$ref": "#/definitions/organHealth" }
              }
            },
            "prosthetics": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "type": { "type": "string" },
                  "location": { "type": "string" },
                  "neural_interface": { "type": "boolean" },
                  "manufacturer": { "type": "string" }
                }
              }
            }
          }
        },
        "physiology": {
          "type": "object",
          "properties": {
            "vital_signs": {
              "type": "object",
              "properties": {
                "resting_heart_rate": { "type": "integer", "minimum": 30, "maximum": 200 },
                "blood_pressure": {
                  "type": "object",
                  "properties": {
                    "systolic": { "type": "integer", "minimum": 70, "maximum": 250 },
                    "diastolic": { "type": "integer", "minimum": 40, "maximum": 150 }
                  }
                },
                "body_temperature_celsius": { "type": "number", "minimum": 35, "maximum": 42 },
                "respiratory_rate": { "type": "integer", "minimum": 8, "maximum": 40 },
                "oxygen_saturation": { "type": "number", "minimum": 70, "maximum": 100 }
              }
            },
            "metabolic_rate": { "type": "number" },
            "sleep_patterns": {
              "type": "object",
              "properties": {
                "average_duration_hours": { "type": "number", "minimum": 0, "maximum": 24 },
                "quality_score": { "type": "number", "minimum": 0, "maximum": 100 },
                "chronotype": { "enum": ["extreme_early", "moderate_early", "intermediate", "moderate_late", "extreme_late"] },
                "sleep_stages": {
                  "type": "object",
                  "properties": {
                    "deep_percentage": { "type": "number" },
                    "rem_percentage": { "type": "number" },
                    "light_percentage": { "type": "number" }
                  }
                },
                "disorders": { "type": "array", "items": { "type": "string" } }
              }
            },
            "nutritional_status": {
              "type": "object",
              "properties": {
                "dietary_pattern": { "type": "string" },
                "caloric_intake_daily": { "type": "integer" },
                "micronutrient_levels": { "type": "object" },
                "hydration_status": { "type": "string" },
                "gut_microbiome_profile": { "type": "object" }
              }
            },
            "fitness_metrics": {
              "type": "object",
              "properties": {
                "vo2_max": { "type": "number" },
                "flexibility_score": { "type": "number" },
                "strength_metrics": { "type": "object" },
                "endurance_metrics": { "type": "object" },
                "reaction_time_ms": { "type": "number" }
              }
            }
          }
        },
        "medical_history": {
          "type": "object",
          "properties": {
            "conditions": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "diagnosis": { "type": "string" },
                  "icd10_code": { "type": "string" },
                  "onset_date": { "type": "string", "format": "date" },
                  "status": { "enum": ["active", "resolved", "chronic", "in_remission"] },
                  "severity": { "enum": ["mild", "moderate", "severe", "life_threatening"] },
                  "treatments": { "type": "array", "items": { "type": "string" } }
                }
              }
            },
            "medications": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" },
                  "dosage": { "type": "string" },
                  "frequency": { "type": "string" },
                  "purpose": { "type": "string" },
                  "prescribed_since": { "type": "string", "format": "date" }
                }
              }
            },
            "immunizations": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "vaccine": { "type": "string" },
                  "date": { "type": "string", "format": "date" },
                  "booster_dates": { "type": "array", "items": { "type": "string", "format": "date" } }
                }
              }
            },
            "allergies": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "allergen": { "type": "string" },
                  "reaction_type": { "type": "string" },
                  "severity": { "enum": ["mild", "moderate", "severe", "anaphylactic"] }
                }
              }
            },
            "surgical_history": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "procedure": { "type": "string" },
                  "date": { "type": "string", "format": "date" },
                  "surgeon": { "type": "string" },
                  "outcome": { "type": "string" }
                }
              }
            },
            "mental_health": {
              "type": "object",
              "properties": {
                "diagnoses": { "type": "array", "items": { "type": "string" } },
                "therapy_history": { "type": "array", "items": { "type": "string" } },
                "hospitalizations": { "type": "array", "items": { "type": "string" } },
                "crisis_plans": { "type": "boolean" }
              }
            }
          }
        },
        "sensory_systems": {
          "type": "object",
          "properties": {
            "vision": {
              "type": "object",
              "properties": {
                "acuity_left": { "type": "string" },
                "acuity_right": { "type": "string" },
                "color_vision": { "type": "boolean" },
                "corrections": { "type": "array", "items": { "type": "string" } },
                "conditions": { "type": "array", "items": { "type": "string" } }
              }
            },
            "hearing": {
              "type": "object",
              "properties": {
                "threshold_left_db": { "type": "array", "items": { "type": "number" } },
                "threshold_right_db": { "type": "array", "items": { "type": "number" } },
                "aids": { "type": "boolean" },
                "cochlear_implant": { "type": "boolean" }
              }
            },
            "olfaction": {
              "type": "object",
              "properties": {
                "functional": { "type": "boolean" },
                "anosmia_type": { "type": "string" }
              }
            },
            "gustation": {
              "type": "object",
              "properties": {
                "taste_disorders": { "type": "array", "items": { "type": "string" } },
                "preferences": { "type": "array", "items": { "type": "string" } }
              }
            },
            "somatosensation": {
              "type": "object",
              "properties": {
                "pain_threshold": { "type": "number" },
                "temperature_sensitivity": { "type": "string" },
                "tactile_defensiveness": { "type": "boolean" }
              }
            },
            "proprioception": {
              "type": "object",
              "properties": {
                "balance_score": { "type": "number" },
                "coordination_level": { "type": "string" }
              }
            },
            "vestibular": {
              "type": "object",
              "properties": {
                "motion_sickness": { "type": "boolean" },
                "spatial_orientation": { "type": "string" }
              }
            }
          }
        },
        "reproductive_health": {
          "type": "object",
          "properties": {
            "fertility_status": { "type": "string" },
            "contraception": { "type": "string" },
            "pregnancy_history": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "outcome": { "type": "string" },
                  "date": { "type": "string", "format": "date" },
                  "complications": { "type": "array", "items": { "type": "string" } }
                }
              }
            },
            "hormonal_profile": { "type": "object" },
            "sexual_health": {
              "type": "object",
              "properties": {
                "orientation": { "type": "string" },
                "activity_level": { "type": "string" },
                "dysfunctions": { "type": "array", "items": { "type": "string" } },
                "sti_history": { "type": "array", "items": { "type": "string" } }
              }
            }
          }
        },
        "longevity_markers": {
          "type": "object",
          "properties": {
            "biological_age": { "type": "number" },
            "epigenetic_clock": { "type": "string" },
            "inflammation_markers": { "type": "object" },
            "longevity_interventions": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },
    "psychology": {
      "type": "object",
      "title": "Cognitive & Psychological Profile",
      "properties": {
        "cognitive_abilities": {
          "type": "object",
          "properties": {
            "iq_score": { "type": "integer", "minimum": 40, "maximum": 200 },
            "cognitive_domains": {
              "type": "object",
              "properties": {
                "verbal_comprehension": { "type": "number", "minimum": 0, "maximum": 100 },
                "perceptual_reasoning": { "type": "number", "minimum": 0, "maximum": 100 },
                "working_memory": { "type": "number", "minimum": 0, "maximum": 100 },
                "processing_speed": { "type": "number", "minimum": 0, "maximum": 100 },
                "executive_function": { "type": "number", "minimum": 0, "maximum": 100 },
                "emotional_intelligence": { "type": "number", "minimum": 0, "maximum": 100 },
                "creativity_index": { "type": "number", "minimum": 0, "maximum": 100 },
                "wisdom_score": { "type": "number", "minimum": 0, "maximum": 100 }
              }
            },
            "learning_style": { "type": "string" },
            "neurodivergence": {
              "type": "array",
              "items": {
                "enum": ["ADHD", "autism_spectrum", "dyslexia", "dyscalculia", "dyspraxia", "tourette", "giftedness", "none"]
              }
            },
            "memory_profile": {
              "type": "object",
              "properties": {
                "short_term_capacity": { "type": "integer" },
                "long_term_retention": { "type": "string" },
                "prospective_memory": { "type": "string" },
                "autobiographical_density": { "type": "string" }
              }
            }
          }
        },
        "emotional_landscape": {
          "type": "object",
          "properties": {
            "baseline_mood": { "type": "string" },
            "emotional_regulation": { "type": "string", "enum": ["excellent", "good", "moderate", "poor", "dysregulated"] },
            "emotional_granularity": { "type": "string" },
            "common_triggers": { "type": "array", "items": { "type": "string" } },
            "coping_mechanisms": { "type": "array", "items": { "type": "string" } },
            "trauma_history": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "type": { "type": "string" },
                  "age_at_occurrence": { "type": "integer" },
                  "resolved": { "type": "boolean" },
                  "therapeutic_interventions": { "type": "array", "items": { "type": "string" } }
                }
              }
            },
            "attachment_style": { "enum": ["secure", "anxious", "avoidant", "disorganized", "unclassified"] }
          }
        },
        "consciousness_states": {
          "type": "object",
          "properties": {
            "default_mode": { "type": "string" },
            "meditation_practice": {
              "type": "object",
              "properties": {
                "regular": { "type": "boolean" },
                "tradition": { "type": "string" },
                "experience_level": { "type": "string" },
                "altered_states_achieved": { "type": "array", "items": { "type": "string" } }
              }
            },
            "substance_use": {
              "type": "object",
              "properties": {
                "caffeine_daily_mg": { "type": "integer" },
                "alcohol_units_weekly": { "type": "number" },
                "nicotine": { "type": "boolean" },
                "cannabis": { "type": "string" },
                "psychedelics_history": { "type": "array", "items": { "type": "string" } },
                "prescription_psychoactives": { "type": "array", "items": { "type": "string" } },
                "addiction_history": { "type": "array", "items": { "type": "string" } }
              }
            },
            "flow_states": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "activity": { "type": "string" },
                  "frequency": { "type": "string" },
                  "depth_score": { "type": "number" }
                }
              }
            }
          }
        },
        "mental_models": {
          "type": "object",
          "properties": {
            "worldview": { "type": "string" },
            "decision_making_style": { "type": "string" },
            "cognitive_biases": { "type": "array", "items": { "type": "string" } },
            "critical_thinking_level": { "type": "string" },
            "openness_to_experience": { "type": "number" },
            "uncertainty_tolerance": { "type": "string" }
          }
        },
        "subjective_wellbeing": {
          "type": "object",
          "properties": {
            "life_satisfaction_score": { "type": "number", "minimum": 0, "maximum": 10 },
            "happiness_index": { "type": "number", "minimum": 0, "maximum": 10 },
            "meaning_score": { "type": "number", "minimum": 0, "maximum": 10 },
            "flourishing_scale": { "type": "number", "minimum": 0, "maximum": 10 },
            "loneliness_index": { "type": "number", "minimum": 0, "maximum": 10 }
          }
        }
      }
    },
    "social_connections": {
      "type": "object",
      "title": "Social Ecosystem",
      "properties": {
        "family_of_origin": {
          "type": "object",
          "properties": {
            "parents": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "relationship": { "enum": ["biological", "adoptive", "foster", "step", "social"] },
                  "living": { "type": "boolean" },
                  "relationship_quality": { "type": "string" },
                  "contact_frequency": { "type": "string" }
                }
              }
            },
            "siblings": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "relationship_quality": { "type": "string" },
                  "geographic_proximity": { "type": "string" }
                }
              }
            },
            "extended_family": { "type": "array", "items": { "type": "string" } },
            "family_dynamics": { "type": "string" },
            "childhood_adversity_score": { "type": "number", "minimum": 0, "maximum": 10 }
          }
        },
        "family_created": {
          "type": "object",
          "properties": {
            "partners": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "relationship_type": { "enum": ["married", "domestic_partnership", "committed_relationship", "polyamorous", "other"] },
                  "duration_years": { "type": "number" },
                  "cohabiting": { "type": "boolean" },
                  "satisfaction_score": { "type": "number", "minimum": 0, "maximum": 10 }
                }
              }
            },
            "children": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "relationship": { "enum": ["biological", "adopted", "foster", "step", "guardian"] },
                  "age": { "type": "integer" },
                  "custody_arrangement": { "type": "string" }
                }
              }
            },
            "pets": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "species": { "type": "string" },
                  "name": { "type": "string" },
                  "emotional_significance": { "type": "string" }
                }
              }
            }
          }
        },
        "friendship_network": {
          "type": "object",
          "properties": {
            "close_friends": { "type": "integer" },
            "casual_friends": { "type": "integer" },
            "acquaintances": { "type": "integer" },
            "friendship_quality_average": { "type": "number" },
            "social_chemistry_profiles": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "friend_id": { "type": "string" },
                  "shared_interests": { "type": "array", "items": { "type": "string" } },
                  "intimacy_level": { "type": "string" },
                  "conflict_history": { "type": "string" }
                }
              }
            },
            "friendship_durations": {
              "type": "array",
              "items": { "type": "number" }
            }
          }
        },
        "professional_network": {
          "type": "object",
          "properties": {
            "mentors": { "type": "array", "items": { "type": "string" } },
            "mentees": { "type": "array", "items": { "type": "string" } },
            "collaborators": { "type": "array", "items": { "type": "string" } },
            "professional_associations": { "type": "array", "items": { "type": "string" } },
            "network_strength_score": { "type": "number" },
            "weak_ties_count": { "type": "integer" }
          }
        },
        "community_belonging": {
          "type": "object",
          "properties": {
            "neighborhood_connection": { "type": "string" },
            "religious_community": { "type": "string" },
            "hobby_groups": { "type": "array", "items": { "type": "string" } },
            "support_groups": { "type": "array", "items": { "type": "string" } },
            "volunteer_organizations": { "type": "array", "items": { "type": "string" } },
            "online_communities": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "platform": { "type": "string" },
                  "community_name": { "type": "string" },
                  "role": { "type": "string" },
                  "engagement_level": { "type": "string" }
                }
              }
            },
            "sense_of_belonging_score": { "type": "number", "minimum": 0, "maximum": 10 }
          }
        },
        "social_capital": {
          "type": "object",
          "properties": {
            "bonding_capital": { "type": "number" },
            "bridging_capital": { "type": "number" },
            "linking_capital": { "type": "number" },
            "trust_radius": { "type": "string" },
            "reciprocity_expectations": { "type": "string" }
          }
        },
        "communication_patterns": {
          "type": "object",
          "properties": {
            "preferred_channels": { "type": "array", "items": { "type": "string" } },
            "response_latency_average": { "type": "string" },
            "conflict_style": { "type": "string" },
            "assertiveness_level": { "type": "string" },
            "empathy_accuracy": { "type": "number" },
            "social_anxiety_level": { "type": "string" }
          }
        }
      }
    },
    "environment": {
      "type": "object",
      "title": "Living Environment",
      "properties": {
        "physical_spaces": {
          "type": "object",
          "properties": {
            "primary_residence": {
              "type": "object",
              "properties": {
                "type": { "enum": ["house", "apartment", "condo", "mobile_home", "tiny_house", "boat", "van", "other"] },
                "ownership_status": { "enum": ["owned", "mortgaged", "rented", "subsidized", "squatting", "nomadic"] },
                "square_meters": { "type": "number" },
                "location": {
                  "type": "object",
                  "properties": {
                    "country": { "type": "string" },
                    "region": { "type": "string" },
                    "city": { "type": "string" },
                    "neighborhood": { "type": "string" },
                    "coordinates": {
                      "type": "object",
                      "properties": {
                        "latitude": { "type": "number" },
                        "longitude": { "type": "number" }
                      }
                    },
                    "climate_zone": { "type": "string" },
                    "urban_rural": { "enum": ["urban", "suburban", "rural", "remote"] },
                    "walkability_score": { "type": "number", "minimum": 0, "maximum": 100 }
                  }
                },
                "safety_rating": { "type": "number", "minimum": 0, "maximum": 10 },
                "environmental_hazards": { "type": "array", "items": { "type": "string" } },
                "smart_home_integration": { "type": "boolean" },
                "sustainability_features": { "type": "array", "items": { "type": "string" } }
              }
            },
            "secondary_locations": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "type": { "type": "string" },
                  "location": { "type": "string" },
                  "frequency_of_use": { "type": "string" }
                }
              }
            },
            "workspace": {
              "type": "object",
              "properties": {
                "location": { "type": "string" },
                "ergonomics_score": { "type": "number" },
                "commute_duration_minutes": { "type": "number" },
                "remote_work_percentage": { "type": "number", "minimum": 0, "maximum": 100 }
              }
            }
          }
        },
        "socioeconomic_context": {
          "type": "object",
          "properties": {
            "income": {
              "type": "object",
              "properties": {
                "annual_gross": { "type": "number" },
                "currency": { "type": "string" },
                "sources": { "type": "array", "items": { "type": "string" } },
                "stability": { "type": "string" },
                "percentile_nationally": { "type": "number" },
                "percentile_globally": { "type": "number" }
              }
            },
            "wealth": {
              "type": "object",
              "properties": {
                "net_worth": { "type": "number" },
                "assets": {
                  "type": "object",
                  "properties": {
                    "real_estate": { "type": "number" },
                    "investments": { "type": "number" },
                    "retirement": { "type": "number" },
                    "liquid": { "type": "number" },
                    "personal_property": { "type": "number" },
                    "digital_assets": { "type": "number" }
                  }
                },
                "debts": {
                  "type": "object",
                  "properties": {
                    "mortgage": { "type": "number" },
                    "student_loans": { "type": "number" },
                    "consumer_debt": { "type": "number" },
                    "other": { "type": "number" }
                  }
                },
                "generational_wealth": { "type": "string" }
              }
            },
            "education": {
              "type": "object",
              "properties": {
                "highest_degree": { "type": "string" },
                "field_of_study": { "type": "string" },
                "institutions": { "type": "array", "items": { "type": "string" } },
                "student_debt_remaining": { "type": "number" },
                "lifelong_learning": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": { "type": "string" },
                      "topic": { "type": "string" },
                      "year": { "type": "integer" }
                    }
                  }
                }
              }
            },
            "occupation": {
              "type": "object",
              "properties": {
                "current_role": { "type": "string" },
                "industry": { "type": "string" },
                "employment_status": { "enum": ["employed", "self_employed", "unemployed", "student", "retired", "disabled", "caregiver"] },
                "employer": { "type": "string" },
                "years_experience": { "type": "number" },
                "career_satisfaction": { "type": "number", "minimum": 0, "maximum": 10 },
                "work_life_balance": { "type": "string" },
                "job_security": { "type": "string" },
                "meaning_perception": { "type": "string" }
              }
            },
            "social_class": {
              "type": "object",
              "properties": {
                "self_identified": { "type": "string" },
                "objective_indicators": { "type": "object" },
                "class_mobility": { "type": "string" },
                "cultural_capital": { "type": "number" }
              }
            }
          }
        },
        "material_possessions": {
          "type": "object",
          "properties": {
            "transportation": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "type": { "enum": ["car", "motorcycle", "bicycle", "public_transit_pass", "boat", "aircraft", "other"] },
                  "ownership": { "type": "string" },
                  "environmental_impact": { "type": "string" }
                }
              }
            },
            "technology": {
              "type": "object",
              "properties": {
                "smartphones": { "type": "integer" },
                "computers": { "type": "integer" },
                "wearables": { "type": "array", "items": { "type": "string" } },
                "home_automation": { "type": "array", "items": { "type": "string" } },
                "screen_time_daily_hours": { "type": "number" }
              }
            },
            "significant_objects": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "item": { "type": "string" },
                  "sentimental_value": { "type": "boolean" },
                  "monetary_value": { "type": "number" }
                }
              }
            },
            "minimalism_score": { "type": "number", "minimum": 0, "maximum": 100 }
          }
        },
        "environmental_exposure": {
          "type": "object",
          "properties": {
            "air_quality_index": { "type": "number" },
            "water_quality": { "type": "string" },
            "noise_pollution": { "type": "string" },
            "light_pollution": { "type": "string" },
            "green_space_access": { "type": "string" },
            "nature_exposure_weekly_hours": { "type": "number" },
            "toxin_exposures": { "type": "array", "items": { "type": "string" } },
            "radiation_exposure": { "type": "string" }
          }
        },
        "digital_environment": {
          "type": "object",
          "properties": {
            "platform_presence": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "platform": { "type": "string" },
                  "username": { "type": "string" },
                  "activity_level": { "type": "string" },
                  "data_shared": { "type": "array", "items": { "type": "string" } }
                }
              }
            },
            "privacy_settings": { "type": "object" },
            "data_footprint_size_gb": { "type": "number" },
            "algorithmic_exposure": { "type": "array", "items": { "type": "string" } },
            "digital_detox_frequency": { "type": "string" }
          }
        }
      }
    },
    "lifecycle": {
      "type": "object",
      "title": "Life Journey",
      "properties": {
        "developmental_stage": {
          "type": "object",
          "properties": {
            "current_phase": {
              "enum": ["infancy", "early_childhood", "middle_childhood", "adolescence", "emerging_adulthood", "early_adulthood", "middle_adulthood", "late_adulthood", "elderhood", "terminal"]
            },
            "developmental_tasks": { "type": "array", "items": { "type": "string" } },
            "age_normative_expectations": { "type": "array", "items": { "type": "string" } },
            "individual_timing": { "type": "string" }
          }
        },
        "life_events": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "event_type": { "type": "string" },
              "date": { "type": "string", "format": "date" },
              "age_at_event": { "type": "integer" },
              "impact_score": { "type": "number", "minimum": -10, "maximum": 10 },
              "stress_level": { "type": "number", "minimum": 0, "maximum": 100 },
              "resolution_status": { "type": "string" }
            }
          }
        },
        "routines": {
          "type": "object",
          "properties": {
            "daily_structure": {
              "type": "object",
              "properties": {
                "wake_time": { "type": "string" },
                "sleep_time": { "type": "string" },
                "meal_times": { "type": "array", "items": { "type": "string" } },
                "work_hours": { "type": "string" },
                "exercise_timing": { "type": "string" },
                "leisure_blocks": { "type": "array", "items": { "type": "string" } }
              }
            },
            "weekly_patterns": { "type": "object" },
            "seasonal_variations": { "type": "object" },
            "rituals": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" },
                  "frequency": { "type": "string" },
                  "significance": { "type": "string" }
                }
              }
            }
          }
        },
        "time_perception": {
          "type": "object",
          "properties": {
            "pace_of_life": { "type": "string" },
            "time_pressure": { "type": "string" },
            "present_orientation": { "type": "number" },
            "future_orientation": { "type": "number" },
            "past_orientation": { "type": "number" },
            "time_affluence": { "type": "boolean" }
          }
        },
        "mortality_awareness": {
          "type": "object",
          "properties": {
            "death_anxiety_level": { "type": "string" },
            "legacy_concerns": { "type": "array", "items": { "type": "string" } },
            "end_of_life_preferences": {
              "type": "object",
              "properties": {
                "advance_directive": { "type": "boolean" },
                "organ_donation": { "type": "boolean" },
                "preferred_death_location": { "type": "string" },
                "funeral_preferences": { "type": "string" }
              }
            },
            "immortality_projects": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },
    "activities_practices": {
      "type": "object",
      "title": "Daily Life Activities",
      "properties": {
        "work_productivity": {
          "type": "object",
          "properties": {
            "primary_activities": { "type": "array", "items": { "type": "string" } },
            "secondary_activities": { "type": "array", "items": { "type": "string" } },
            "side_projects": { "type": "array", "items": { "type": "string" } },
            "productivity_systems": { "type": "array", "items": { "type": "string" } },
            "procrastination_triggers": { "type": "array", "items": { "type": "string" } },
            "flow_activities": { "type": "array", "items": { "type": "string" } }
          }
        },
        "leisure_recreation": {
          "type": "object",
          "properties": {
            "hobbies": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "activity": { "type": "string" },
                  "skill_level": { "type": "string" },
                  "hours_per_week": { "type": "number" },
                  "social_solo": { "enum": ["social", "solo", "mixed"] }
                }
              }
            },
            "entertainment_consumption": {
              "type": "object",
              "properties": {
                "books_annual": { "type": "integer" },
                "movies_annual": { "type": "integer" },
                "series_streaming_hours_weekly": { "type": "number" },
                "gaming_hours_weekly": { "type": "number" },
                "music_hours_weekly": { "type": "number" },
                "podcast_hours_weekly": { "type": "number" },
                "news_consumption_hours_weekly": { "type": "number" }
              }
            },
            "travel": {
              "type": "object",
              "properties": {
                "countries_visited": { "type": "integer" },
                "travel_style": { "type": "string" },
                "annual_trips": { "type": "integer" },
                "dream_destinations": { "type": "array", "items": { "type": "string" } }
              }
            },
            "creative_practices": { "type": "array", "items": { "type": "string" } },
            "physical_activities": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "activity": { "type": "string" },
                  "frequency": { "type": "string" },
                  "intensity": { "type": "string" }
                }
              }
            }
          }
        },
        "maintenance_tasks": {
          "type": "object",
          "properties": {
            "self_care_routines": { "type": "array", "items": { "type": "string" } },
            "domestic_labor_hours_weekly": { "type": "number" },
            "administrative_burden": { "type": "string" },
            "caregiving_responsibilities": {
              "type": "object",
              "properties": {
                "childcare_hours_weekly": { "type": "number" },
                "eldercare_hours_weekly": { "type": "number" },
                "petcare_hours_weekly": { "type": "number" },
                "emotional_labor_score": { "type": "number" }
              }
            },
            "shopping_patterns": { "type": "object" }
          }
        },
        "consumption_patterns": {
          "type": "object",
          "properties": {
            "diet": {
              "type": "object",
              "properties": {
                "pattern": { "type": "string" },
                "restrictions": { "type": "array", "items": { "type": "string" } },
                "cooking_frequency": { "type": "string" },
                "dining_out_frequency": { "type": "string" },
                "food_budget_monthly": { "type": "number" }
              }
            },
            "consumer_behavior": {
              "type": "object",
              "properties": {
                "shopping_impulse_control": { "type": "string" },
                "brand_loyalty": { "type": "string" },
                "sustainability_priority": { "type": "boolean" },
                "secondhand_usage": { "type": "boolean" },
                "subscription_services": { "type": "array", "items": { "type": "string" } }
              }
            },
            "media_diet": { "type": "object" }
          }
        },
        "spiritual_practices": {
          "type": "object",
          "properties": {
            "formal_religion": {
              "type": "object",
              "properties": {
                "tradition": { "type": "string" },
                "attendance_frequency": { "type": "string" },
                "doctrinal_adherence": { "type": "string" },
                "community_involvement": { "type": "string" }
              }
            },
            "personal_spirituality": {
              "type": "object",
              "properties": {
                "practices": { "type": "array", "items": { "type": "string" } },
                "transcendence_experiences": { "type": "array", "items": { "type": "string" } },
                "meaning_making_system": { "type": "string" }
              }
            },
            "ethical_consumption": { "type": "array", "items": { "type": "string" } }
          }
        },
        "learning_development": {
          "type": "object",
          "properties": {
            "current_learning_goals": { "type": "array", "items": { "type": "string" } },
            "skill_acquisition": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "skill": { "type": "string" },
                  "proficiency": { "type": "string" },
                  "learning_method": { "type": "string" }
                }
              }
            },
            "language_learning": { "type": "array", "items": { "type": "string" } },
            "intellectual_challenges": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },
    "existential_dimensions": {
      "type": "object",
      "title": "Meaning & Purpose",
      "properties": {
        "sources_of_meaning": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "source": { "type": "string" },
              "weight": { "type": "number", "minimum": 0, "maximum": 1 },
              "satisfaction": { "type": "number", "minimum": 0, "maximum": 10 }
            }
          }
        },
        "values_hierarchy": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "value": { "type": "string" },
              "priority_rank": { "type": "integer" },
              "behavior_alignment": { "type": "number", "minimum": 0, "maximum": 10 }
            }
          }
        },
        "purpose_statement": { "type": "string" },
        "life_projects": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "project": { "type": "string" },
              "progress_percentage": { "type": "number" },
              "significance": { "type": "string" }
            }
          }
        },
        "transcendence_connection": {
          "type": "object",
          "properties": {
            "nature_connection": { "type": "number", "minimum": 0, "maximum": 10 },
            "cosmic_perspective": { "type": "number", "minimum": 0, "maximum": 10 },
            "generativity_score": { "type": "number", "minimum": 0, "maximum": 10 },
            "legacy_concern": { "type": "number", "minimum": 0, "maximum": 10 }
          }
        },
        "autonomy_authenticity": {
          "type": "object",
          "properties": {
            "internal_locus_of_control": { "type": "number", "minimum": 0, "maximum": 100 },
            "authenticity_score": { "type": "number", "minimum": 0, "maximum": 10 },
            "self_determination": {
              "type": "object",
              "properties": {
                "autonomy": { "type": "number" },
                "competence": { "type": "number" },
                "relatedness": { "type": "number" }
              }
            }
          }
        },
        "moral_framework": {
          "type": "object",
          "properties": {
            "primary_orientation": { "enum": ["care", "fairness", "loyalty", "authority", "sanctity", "liberty", "utilitarian", "deontological", "virtue_ethics", "existentialist"] },
            "moral_foundations_scores": {
              "type": "object",
              "properties": {
                "care_harm": { "type": "number" },
                "fairness_cheating": { "type": "number" },
                "loyalty_betrayal": { "type": "number" },
                "authority_subversion": { "type": "number" },
                "sanctity_degradation": { "type": "number" },
                "liberty_oppression": { "type": "number" }
              }
            },
            "ethical_dilemmas_stance": { "type": "object" }
          }
        }
      }
    },
    "system_interactions": {
      "type": "object",
      "title": "Institutional & System Engagement",
      "properties": {
        "governance": {
          "type": "object",
          "properties": {
            "citizenship_status": { "type": "string" },
            "voting_behavior": { "type": "string" },
            "political_engagement": { "type": "string" },
            "trust_in_institutions": { "type": "object" },
            "legal_encounters": { "type": "array", "items": { "type": "string" } }
          }
        },
        "economic_systems": {
          "type": "object",
          "properties": {
            "banking_relationships": { "type": "array", "items": { "type": "string" } },
            "credit_score": { "type": "number" },
            "investment_strategy": { "type": "string" },
            "retirement_planning": { "type": "object" },
            "insurance_coverage": { "type": "object" }
          }
        },
        "healthcare_system": {
          "type": "object",
          "properties": {
            "primary_provider": { "type": "string" },
            "insurance_type": { "type": "string" },
            "healthcare_access_score": { "type": "number" },
            "preventive_care_adherence": { "type": "string" },
            "alternative_medicine_usage": { "type": "array", "items": { "type": "string" } }
          }
        },
        "education_system": {
          "type": "object",
          "properties": {
            "educational_debt": { "type": "number" },
            "alumni_networks": { "type": "array", "items": { "type": "string" } },
            "continuing_ed_engagement": { "type": "string" }
          }
        },
        "digital_infrastructure": {
          "type": "object",
          "properties": {
            "internet_access_quality": { "type": "string" },
            "digital_literacy": { "type": "string" },
            "cybersecurity_practices": { "type": "string" },
            "platform_dependencies": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {
        "schema_version": { "type": "string", "default": "1.0.0" },
        "last_updated": { "type": "string", "format": "date-time" },
        "completeness_score": { "type": "number", "minimum": 0, "maximum": 100 },
        "data_sources": { "type": "array", "items": { "type": "string" } },
        "privacy_level": { "enum": ["public", "restricted", "private", "sensitive"] },
        "encryption_status": { "type": "boolean" }
      }
    }
  },
  "definitions": {
    "organHealth": {
      "type": "object",
      "properties": {
        "functionality_percentage": { "type": "number", "minimum": 0, "maximum": 100 },
        "conditions": { "type": "array", "items": { "type": "string" } },
        "last_assessment": { "type": "string", "format": "date" },
        "transplant_history": { "type": "boolean" }
      }
    }
  }
}
```