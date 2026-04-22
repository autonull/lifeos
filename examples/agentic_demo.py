#!/usr/bin/env python3
"""
LifeOS Agentic Interface - Example Usage

This script demonstrates how to use the new natural language interface
to explore life scenarios through the LifeOS ontological framework.
"""

import sys
sys.path.insert(0, '/home/bot/lifeos')

from lifeos.agentic import IntentParser, AgenticLifeOS

def demo_intent_parser():
    """Demonstrate natural language intent parsing."""
    print("\n" + "="*60)
    print("INTENT PARSER DEMO")
    print("="*60)
    
    parser = IntentParser()
    
    examples = [
        "I'm thinking about quitting my job to freelance",
        "What if I moved to a cheaper city?",
        "I need more sleep and less stress",
        "Should I go part-time?",
        "I want to exercise more and lose weight"
    ]
    
    for text in examples:
        print(f"\nUser says: \"{text}\"")
        print("-" * 40)
        
        result = parser.parse_intent(text)
        
        print(f"  Detected domains: {', '.join(result['affected_domains'])}")
        print(f"  Intent type: {result['intent_type']}")
        print(f"  Confidence: {result['confidence']:.1%}")
        
        if result['modifications']:
            print(f"  Suggested ontology changes:")
            for mod in result['modifications']:
                print(f"    - {mod['path']} → {mod['new']}")
        
        if result.get('clarification_needed'):
            print(f"  Needs clarification: {result['clarification_needed']}")

def demo_scenario_exploration():
    """Demonstrate full scenario exploration."""
    print("\n" + "="*60)
    print("SCENARIO EXPLORATION DEMO")
    print("="*60)
    
    # Note: This would require actual LifeOS state to be present
    # For demo, we show the structure
    print("\nIn a full implementation, calling:")
    print("  agent = AgenticLifeOS()")
    print("  result = agent.conversational_explore(\"I want to quit my job\")")
    print("\nWould return:")
    print("  - Created branch ID")
    print("  - Ontological modifications")
    print("  - Detected dissonance/conflicts")
    print("  - Historical patterns")
    print("  - Suggested next steps")

if __name__ == "__main__":
    demo_intent_parser()
    demo_scenario_exploration()
    
    print("\n" + "="*60)
    print("AGENT PROTOCOL ACTIONS")
    print("="*60)
    print("""
New JSON-RPC actions available:

1. explore_scenario
   Params: {user_input: "I want to quit my job"}
   Returns: Branch info, modifications, dissonance, next steps

2. parse_intent  
   Params: {user_input: "I want more freedom"}
   Returns: Parsed intent with domains and modifications

3. compare_branches
   Params: {branch_ids: ["branch1", "branch2"]}
   Returns: Comparison across ontological metrics

4. find_patterns
   Params: {query: "stress after product launch", timeframe: "6months"}
   Returns: Historical patterns matching query
""")
