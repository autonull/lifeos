"""
LifeOS Agentic Interface
Natural language intent parsing and ontology-aware reasoning for conversational AI.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from difflib import SequenceMatcher
from lifeos.core import LifeOS, State

# Ontological path mappings (natural language → ontology paths)
INTENT_MAPPINGS = {
    # Career changes
    "quit": {"career.employment_type": "unemployed", "career.sector": None},
    "freelance": {"career.employment_type": "freelance", "career.sector": "self-employed"},
    "part-time": {"career.employment_type": "part-time"},
    "remote work": {"career.work_location": "remote"},
    "career change": {"career.title": None, "career.industry": None},
    
    # Environment changes
    "move": {"environment.physical_spaces.location": None},  # Requires clarification
    "downsize": {"environment.physical_spaces.size_sqm": -30},  # Percentage reduction
    "cheaper city": {"environment.cost_of_living": -25},
    
    # Biology/Health
    "sleep more": {"biology.sleep_patterns.average_duration_hours": 8},
    "exercise": {"biology.fitness_metrics.weekly_exercise_minutes": 150},
    "lose weight": {"biology.body_composition.weight_kg": -10},  # Placeholder logic
    
    # Psychology
    "less stress": {"psychology.emotional_landscape.stress_level": 3},
    "more autonomy": {"psychology.autonomy_score": 8},
    
    # Social
    "more friends": {"social_connections.network_size": 20},  # Simplified
    "less social": {"social_connections.weekly_social_hours": -5},
}

# Ontology domain keywords
DOMAIN_KEYWORDS = {
    "identity": ["name", "identity", "pronouns", "gender", "age", "nationality"],
    "biology": ["sleep", "weight", "height", "health", "fitness", "exercise", "diet", "blood", "heart"],
    "psychology": ["stress", "mood", "energy", "anxiety", "depression", "autonomy", "satisfaction"],
    "social_connections": ["friend", "family", "colleague", "network", "relationship", "social"],
    "environment": ["home", "city", "location", "office", "remote", "space", "noise", "climate"],
    "career": ["work", "job", "career", "employment", "salary", "income", "boss", "company"],
    "finance": ["money", "spending", "savings", "debt", "budget", "expense", "financial"],
    "existential_dimensions": ["value", "purpose", "meaning", "belief", "spiritual", "philosophy"],
}


class IntentParser:
    """Parses natural language into ontological modifications."""
    
    def __init__(self):
        self.intent_mappings = INTENT_MAPPINGS
        self.domain_keywords = DOMAIN_KEYWORDS
    
    def detect_domains(self, text: str) -> List[str]:
        """Detect which ontological domains are relevant to the input."""
        text_lower = text.lower()
        relevant_domains = []
        
        for domain, keywords in self.domain_keywords.items():
            if any(kw in text_lower for kw in keywords):
                relevant_domains.append(domain)
        
        return relevant_domains if relevant_domains else ["general"]
    
    def parse_intent(self, text: str) -> Dict[str, Any]:
        """
        Parse natural language intent into structured ontological changes.
        
        Args:
            text: User's natural language input
            
        Returns:
            Dictionary with:
            - intent_type: Category of change
            - modifications: List of ontology path → value changes
            - affected_domains: Which domains are impacted
            - confidence: How certain we are about the interpretation
            - clarification_needed: What questions to ask
        """
        text_lower = text.lower()
        
        # Detect relevant domains
        affected_domains = self.detect_domains(text)
        
        # Try to match known intent patterns
        modifications = []
        intent_type = "custom"
        confidence = 0.5
        clarification_needed = []
        
        # Check for known intent patterns
        for intent_key, ont_changes in self.intent_mappings.items():
            if intent_key in text_lower:
                # Map to ontology paths
                for path, value in ont_changes.items():
                    modifications.append({
                        "path": path,
                        "new": value,
                        "source": f"intent:{intent_key}"
                    })
                intent_type = intent_key
                confidence = 0.8
                break
        
        # Extract numerical values from text
        numbers = re.findall(r'(\d+(?:\.\d+)?)', text)
        if numbers and modifications:
            # Apply first number to first modification if it's None (needs value)
            for i, mod in enumerate(modifications):
                if mod["new"] is None and i < len(numbers):
                    try:
                        mod["new"] = float(numbers[i])
                    except:
                        pass
        
        # Detect uncertainty or questions
        if any(q in text for q in ["what if", "maybe", "should i", "wondering"]):
            intent_type = "exploratory"
            confidence = 0.7
        
        return {
            "intent_type": intent_type,
            "modifications": modifications,
            "affected_domains": affected_domains,
            "confidence": confidence,
            "clarification_needed": clarification_needed,
            "raw_input": text
        }


class AgenticLifeOS:
    """
    Agentic wrapper around LifeOS with natural language interface.
    """
    
    def __init__(self, root_path: Optional[Path] = None):
        self.life = LifeOS(root_path)
        self.parser = IntentParser()
        self.schema_cache = {}
    
    def get_schema_template(self, domain: str = "life1") -> Dict:
        """Load and cache schema template for a domain."""
        if domain not in self.schema_cache:
            schema_path = Path(__file__).parent.parent / "schemas" / f"{domain}.json"
            if schema_path.exists():
                with open(schema_path, 'r') as f:
                    self.schema_cache[domain] = json.load(f)
            else:
                self.schema_cache[domain] = {}
        return self.schema_cache[domain]
    
    def conversational_explore(self, user_input: str, context: Dict = None) -> Dict:
        """
        Explore a scenario from natural language input.
        
        Args:
            user_input: Natural language description of desired change
            context: Optional context (user preferences, history, etc.)
            
        Returns:
            Rich response with branches created, insights, and follow-ups
        """
        # Parse intent
        parsed = self.parser.parse_intent(user_input)
        
        # If low confidence, generate clarification questions
        if parsed["confidence"] < 0.6:
            return {
                "status": "clarification_needed",
                "message": "I want to make sure I understand. Can you tell me more about what you're looking to change?",
                "detected_domains": parsed["affected_domains"],
                "interpretation": parsed,
                "suggested_questions": self._generate_clarification_questions(parsed)
            }
        
        # If no modifications detected, try to infer from context
        if not parsed["modifications"]:
            return {
                "status": "needs_interpretation",
                "message": "I'm not sure which specific changes you're considering. Here are some possibilities based on what you said...",
                "suggested_scenarios": self._generate_suggested_scenarios(parsed)
            }
        
        # Create branch with parsed modifications
        branch_name = self._sanitize_branch_name(user_input)
        branch = self.life.create_branch(
            name=branch_name,
            modifications=parsed["modifications"],
            reasoning=user_input
        )
        
        # Load branch state for analysis
        branch_state = self._load_branch_state(branch.id)
        
        # Detect potential dissonance
        dissonance = self._detect_dissonance(branch_state, parsed)
        
        # Find relevant history
        history_patterns = self._find_relevant_patterns(parsed)
        
        return {
            "status": "success",
            "branch_id": branch.id,
            "branch_name": branch_name,
            "modifications": parsed["modifications"],
            "affected_domains": parsed["affected_domains"],
            "dissonance": dissonance,
            "historical_patterns": history_patterns,
            "next_steps": self._suggest_next_steps(parsed, dissonance)
        }
    
    def _generate_clarification_questions(self, parsed: Dict) -> List[str]:
        """Generate clarification questions based on parsed intent."""
        questions = []
        domains = parsed.get("affected_domains", [])
        
        if "career" in domains:
            questions.append("Are you thinking about changing jobs, reducing hours, or changing industries?")
        if "environment" in domains:
            questions.append("Are you considering moving, changing your living situation, or modifying your workspace?")
        if "social_connections" in domains:
            questions.append("Are you looking to expand your social circle, strengthen existing relationships, or create more boundaries?")
        if "biology" in domains:
            questions.append("Are you focused on sleep, exercise, diet, or something else related to your physical health?")
        
        return questions if questions else ["Can you give me more specifics about what you'd like to explore?"]
    
    def _generate_suggested_scenarios(self, parsed: Dict) -> List[Dict]:
        """Generate suggested scenarios based on intent."""
        # Placeholder - would use more sophisticated inference
        return [
            {"name": "Conservative Change", "description": "Small, reversible modifications"},
            {"name": "Moderate Shift", "description": "Noticeable changes with safety nets"},
            {"name": "Radical Transformation", "description": "Complete lifestyle overhaul"}
        ]
    
    def _sanitize_branch_name(self, text: str) -> str:
        """Convert text to safe branch name."""
        # Remove special chars, truncate
        safe = re.sub(r'[^\w\s-]', '', text)
        safe = re.sub(r'[\s_]+', '-', safe)
        return safe[:50].lower().strip('-')
    
    def _load_branch_state(self, branch_id: str) -> Dict:
        """Load state from a branch."""
        branch_dir = self.life.branches_dir / branch_id
        state_file = branch_dir / "state.json"
        if state_file.exists():
            with open(state_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _detect_dissonance(self, state: Dict, parsed: Dict) -> List[Dict]:
        """Detect potential value conflicts or concerning patterns."""
        dissonance = []
        
        # Example: Check if changes conflict with stated values
        # This would be more sophisticated with full ontology integration
        return dissonance
    
    def _find_relevant_patterns(self, parsed: Dict) -> List[Dict]:
        """Find historical patterns relevant to this exploration."""
        # Placeholder - would search history for similar scenarios
        return []
    
    def _suggest_next_steps(self, parsed: Dict, dissonance: List) -> List[str]:
        """Suggest next actions based on the exploration."""
        suggestions = []
        
        if dissonance:
            suggestions.append("Review the potential conflicts detected")
        
        suggestions.extend([
            "Run simulation to see projected outcomes",
            "Compare with alternative scenarios",
            "Review historical patterns for similar changes"
        ])
        
        return suggestions


# Convenience function for agents
def explore_scenario(user_input: str, context: Dict = None) -> Dict:
    """
    Quick function for agents to explore a scenario.
    
    Usage:
        result = explore_scenario("I'm thinking about going freelance")
        if result["status"] == "success":
            print(f"Created branch: {result['branch_id']}")
        elif result["status"] == "clarification_needed":
            print(result["message"])
            print("Questions:", result["suggested_questions"])
    """
    agent = AgenticLifeOS()
    return agent.conversational_explore(user_input, context)
