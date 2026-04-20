"""LifeOS package."""
from .core import LifeOS, State, Branch
from .physics import PhysicsEngine
from .agent_protocol import run_stdio_protocol

__version__ = "0.1.0"
__all__ = ["LifeOS", "State", "Branch", "PhysicsEngine", "run_stdio_protocol"]
