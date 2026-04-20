"""
LifeOS Physics Engine
Hybrid engine: Deterministic rules for math, LLM for psychology.
"""

from typing import List, Dict, Any
from lifeos.core import State

class PhysicsEngine:
    """Hybrid physics engine for simulating life changes."""

    def __init__(self):
        self.rules = self._load_rules()

    def _load_rules(self) -> List[Dict[str, Any]]:
        """Deterministic rules for tangible metrics."""
        return [
            {
                "trigger": "activities_practices.work_productivity.weekly_hours",
                "condition": lambda v: v > 45,
                "effects": {
                    "biology.sleep_patterns.quality_score": -2,
                    "psychology.emotional_landscape.stress_level": 8,
                    "social_connections.time_for_friends": -10
                }
            },
            {
                "trigger": "biology.sleep_patterns.average_duration_hours",
                "condition": lambda v: v < 6,
                "effects": {
                    "psychology.emotional_landscape.energy_level": -3,
                    "biology.vital_signs.resting_heart_rate": 5
                }
            }
        ]

    def apply_deterministic_rules(self, state: State) -> State:
        """Applies hard-coded rules to state."""
        data = state.model_dump()
        for rule in self.rules:
            path = rule["trigger"].split(".")
            current = data
            for part in path[:-1]:
                current = current[part]
            value = current[path[-1]]
            
            if rule["condition"](value):
                for effect_path, delta in rule["effects"].items():
                    eff_path = effect_path.split(".")
                    eff_current = data
                    for part in eff_path[:-1]:
                        eff_current = eff_current[part]
                    eff_current[eff_path[-1]] = eff_current.get(eff_path[-1], 0) + delta
        return State(**data)

    def generate_narrative(self, state: State, changes: List[Dict[str, Any]]) -> str:
        """
        Generates a psychological narrative using an LLM prompt.
        In a real implementation, this would call an LLM API.
        Here, we simulate the output.
        """
        # Placeholder for LLM integration
        stress_level = state.psychology.get('emotional_landscape', {}).get('stress_level', 0)
        sleep_hours = state.biology.get('sleep_patterns', {}).get('average_duration_hours', 7)
        work_hours = state.activities_practices.get('work_productivity', {}).get('weekly_hours', 0)
        
        narrative = f"""
Based on the changes: {changes}

Psychological Projection:
- Your stress levels are at {stress_level}/10.
- Your energy levels may shift based on your {sleep_hours}h sleep average.
- Social connections might feel {'strained' if work_hours > 40 else 'balanced'}.

Therapeutic Insight:
This simulation suggests a trade-off between productivity and well-being. 
Consider whether the short-term gain aligns with your long-term purpose.
"""
        return narrative.strip()

    def detect_dissonance(self, state: State) -> List[str]:
        """Detects conflicts between values and actions."""
        insights = []
        values = state.existential_dimensions.get('values_hierarchy', [])
        activities = state.activities_practices.get('work_productivity', {})
        
        health_value = next((v for v in values if 'health' in v.get('value', '').lower()), None)
        if health_value:
            sleep = state.biology.get('sleep_patterns', {}).get('average_duration_hours', 0)
            if sleep and sleep < 7:
                insights.append(f"Dissonance: You value 'Health' but sleep {sleep}h (recommended 7-8h).")
        
        work_hours = activities.get('weekly_hours', 0)
        if work_hours > 45:
            insights.append(f"Dissonance: Work hours ({work_hours}) may conflict with work-life balance.")
        
        return insights
