"""
LifeOS Agent Protocol
Stdio JSON-RPC handler for agentic systems.
Now with natural language intent parsing and agentic scenario exploration.
"""

import json
import sys
from lifeos.core import LifeOS
from lifeos.physics import PhysicsEngine
from lifeos.cli import main
from lifeos.agentic import AgenticLifeOS

def handle_request(request: dict) -> dict:
    """Handles a single agent request."""
    action = request.get("action")
    params = request.get("params", {})
    
    try:
        if action == "status":
            life = LifeOS()
            state = life.load_state()
            engine = PhysicsEngine()
            insights = engine.detect_dissonance(state)
            return {
                "status": "success",
                "data": {
                    "state": state.model_dump(),
                    "insights": insights
                }
            }
        
        elif action == "create_branch":
            life = LifeOS()
            branch = life.create_branch(params.get("name"), params.get("modifications", []))
            return {
                "status": "success",
                "data": {
                    "branch_id": branch.id,
                    "path": str(life.branches_dir / branch.id)
                }
            }
        
        elif action == "simulate":
            life = LifeOS()
            branch = life.get_branch(params.get("branch_name"))
            if not branch:
                return {"status": "error", "message": f"Branch not found: {params.get('branch_name')}"}
            
            branch_state_file = life.branches_dir / branch.id / "state.json"
            with open(branch_state_file, 'r') as f:
                state_data = json.load(f)
            from lifeos.core import State
            state = State(**state_data)
            
            engine = PhysicsEngine()
            state = engine.apply_deterministic_rules(state)
            narrative = engine.generate_narrative(state, branch.modifications)
            
            return {
                "status": "success",
                "data": {
                    "narrative": narrative,
                    "state": state.model_dump()
                }
            }
        
        elif action == "adopt":
            life = LifeOS()
            branch = life.get_branch(params.get("branch_name"))
            if not branch:
                return {"status": "error", "message": f"Branch not found: {params.get('branch_name')}"}
            
            branch_state_file = life.branches_dir / branch.id / "state.json"
            with open(branch_state_file, 'r') as f:
                state_data = json.load(f)
            from lifeos.core import State
            life.save_state(State(**state_data))
            life.archive_branch(branch)
            
            return {
                "status": "success",
                "message": f"Adopted branch: {branch.name}"
            }
        
        # === NEW AGENTIC ACTIONS ===
        
        elif action == "explore_scenario":
            """
            Natural language scenario exploration.
            Params: user_input (str), context (dict, optional)
            """
            agent = AgenticLifeOS()
            result = agent.conversational_explore(
                params.get("user_input", ""),
                params.get("context")
            )
            return {
                "status": "success",
                "data": result
            }
        
        elif action == "parse_intent":
            """
            Parse natural language into ontological modifications.
            Params: user_input (str)
            """
            agent = AgenticLifeOS()
            parsed = agent.parser.parse_intent(params.get("user_input", ""))
            return {
                "status": "success",
                "data": parsed
            }
        
        elif action == "compare_branches":
            """
            Compare multiple branches.
            Params: branch_ids (list), metrics (list, optional)
            """
            # Placeholder - would implement comparison logic
            return {
                "status": "success",
                "data": {
                    "message": "Branch comparison not yet implemented",
                    "branch_ids": params.get("branch_ids", [])
                }
            }
        
        elif action == "find_patterns":
            """
            Search for historical patterns.
            Params: query (str), timeframe (str, optional)
            """
            # Placeholder - would implement pattern search
            return {
                "status": "success",
                "data": {
                    "message": "Pattern search not yet implemented",
                    "query": params.get("query", "")
                }
            }
        
        else:
            return {"status": "error", "message": f"Unknown action: {action}"}
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

def run_stdio_protocol():
    """Runs the stdio protocol loop."""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            request = json.loads(line.strip())
            response = handle_request(request)
            print(json.dumps(response), flush=True)
        except json.JSONDecodeError:
            continue
        except Exception as e:
            print(json.dumps({"status": "error", "message": str(e)}), flush=True)

if __name__ == "__main__":
    run_stdio_protocol()
