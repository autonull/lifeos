"""
LifeOS CLI
Command-line interface for LifeOS.
Supports --json for agents and --stdio for agent protocol.
"""

import json
import sys
import click
from pathlib import Path
from lifeos.core import LifeOS, State
from lifeos.physics import PhysicsEngine

@click.group()
@click.option('--stdio', is_flag=True, help="Run in stdio protocol mode for agents.")
@click.pass_context
def main(ctx, stdio):
    """LifeOS: Universal Life Context Engine"""
    ctx.ensure_object(dict)
    ctx.obj['stdio'] = stdio
    if stdio:
        click.echo("LifeOS Agent Mode: Ready", err=True)

@main.command()
@click.pass_context
def init(ctx):
    """Initialize the LifeOS directory structure."""
    root = Path.home() / ".lifeos"
    if root.exists():
        click.echo("LifeOS already initialized at ~/.lifeos")
        return
    
    # Create directories
    for d in ["history", "branches", "archive", "horizons", "insights"]:
        (root / d).mkdir(parents=True, exist_ok=True)
    
    # Create default state.json
    default_state = {
        "identity": {"names": {"preferred_name": "User"}, "self_concept": {"values": [], "beliefs": {}}},
        "biology": {
            "sleep_patterns": {"average_duration_hours": 7.0, "quality_score": 7},
            "vital_signs": {},
            "fitness_metrics": {}
        },
        "psychology": {
            "emotional_landscape": {"baseline_mood": "neutral", "stress_level": 5, "energy_level": 5},
            "cognitive_abilities": {}
        },
        "social_connections": {"family_created": {}, "friendship_network": {}, "professional_network": {}},
        "environment": {"physical_spaces": {}, "digital_environment": {}},
        "lifecycle": {"routines": {}, "life_events": []},
        "activities_practices": {"work_productivity": {"weekly_hours": 40.0}, "leisure_recreation": {}},
        "existential_dimensions": {"values_hierarchy": [], "purpose_statement": ""},
        "metadata": {"created_at": "now", "last_updated": "now", "version": "1.0.0"}
    }
    
    with open(root / "state.json", 'w') as f:
        json.dump(default_state, f, indent=2)
    
    click.echo("✅ LifeOS initialized at ~/.lifeos")
    click.echo("   Run 'lifeos status' to view your state.")

@main.command()
@click.option('--json', 'json_output', is_flag=True, help="Output as JSON for agents.")
@click.pass_context
def status(ctx, json_output):
    """Show current state and active opportunities."""
    try:
        life = LifeOS()
        state = life.load_state()
        engine = PhysicsEngine()
        
        # Detect dissonance
        insights = engine.detect_dissonance(state)
        
        if json_output:
            output = {
                "state": state.model_dump(),
                "insights": insights,
                "opportunities": []
            }
            # Add opportunities logic here
            click.echo(json.dumps(output, indent=2))
        else:
            click.echo("\n📊 LIFE STATUS")
            click.echo(f"Name: {state.identity.get('names', {}).get('preferred_name', 'Unknown')}")
            sleep_hours = state.biology.get('sleep_patterns', {}).get('average_duration_hours', 'N/A')
            quality = state.biology.get('sleep_patterns', {}).get('quality_score', 'N/A')
            click.echo(f"Sleep: {sleep_hours}h (Quality: {quality})")
            stress = state.psychology.get('emotional_landscape', {}).get('stress_level', 'N/A')
            click.echo(f"Stress: {stress}")
            if insights:
                click.echo("\n⚠️  Dissonance Detected:")
                for i in insights:
                    click.echo(f"   - {i}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

@main.command()
@click.argument('name')
@click.option('--mod', 'modifications', multiple=True, help="Modifications (e.g., 'path=value')")
@click.pass_context
def explore(ctx, name, modifications):
    """Explore a new possibility (create a branch)."""
    try:
        life = LifeOS()
        mods = []
        for mod in modifications:
            if '=' in mod:
                path, value = mod.split('=', 1)
                # Try to convert to number
                try:
                    value = float(value)
                except:
                    pass
                mods.append({"path": path, "new": value})
        
        branch = life.create_branch(name, mods)
        click.echo(f"✅ Created branch: {branch.id}")
        click.echo(f"   Path: {life.branches_dir / branch.id}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

@main.command()
@click.argument('branch_name')
@click.option('--days', default=30, help="Days to simulate.")
@click.option('--json', 'json_output', is_flag=True, help="Output as JSON.")
@click.pass_context
def simulate(ctx, branch_name, days, json_output):
    """Simulate a branch."""
    try:
        life = LifeOS()
        branch = life.get_branch(branch_name)
        if not branch:
            click.echo(f"Branch not found: {branch_name}", err=True)
            return
        
        # Load branch state
        branch_state_file = life.branches_dir / branch.id / "state.json"
        with open(branch_state_file, 'r') as f:
            state_data = json.load(f)
        state = State(**state_data)
        
        engine = PhysicsEngine()
        state = engine.apply_deterministic_rules(state)
        narrative = engine.generate_narrative(state, branch.modifications)
        
        if json_output:
            output = {
                "branch": branch.id,
                "narrative": narrative,
                "state": state.model_dump()
            }
            click.echo(json.dumps(output, indent=2))
        else:
            click.echo(f"\n🔮 Simulation: {branch.name}")
            click.echo(narrative)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

@main.command()
@click.argument('branch_name')
@click.pass_context
def adopt(ctx, branch_name):
    """Adopt a branch (merge into reality)."""
    try:
        life = LifeOS()
        branch = life.get_branch(branch_name)
        if not branch:
            click.echo(f"Branch not found: {branch_name}", err=True)
            return
        
        # Load branch state
        branch_state_file = life.branches_dir / branch.id / "state.json"
        with open(branch_state_file, 'r') as f:
            state_data = json.load(f)
        
        # Save as current state
        life.save_state(State(**state_data))
        
        # Archive branch
        life.archive_branch(branch)
        
        click.echo(f"✅ Adopted branch: {branch.name}")
        click.echo("   Reality updated.")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

if __name__ == '__main__':
    main()
