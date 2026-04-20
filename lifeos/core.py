"""
LifeOS Core Module
Manages the LifeOS engine: State, Branches, Archives, and Physics.
"""

import json
import os
import shutil
import fcntl
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, field_validator
import jsonschema

# --- Schemas (Loaded from files) ---
LIFE1_SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "life1.json"
LIFE2_SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "life2.json"

def load_schema(path: Path) -> dict:
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {}

LIFE1_SCHEMA = load_schema(LIFE1_SCHEMA_PATH)
LIFE2_SCHEMA = load_schema(LIFE2_SCHEMA_PATH)

# --- Pydantic Models ---

class State(BaseModel):
    """Represents a snapshot of life (Life1 Schema)."""
    identity: dict
    biology: dict
    psychology: dict
    social_connections: dict
    environment: dict
    lifecycle: dict
    activities_practices: dict
    existential_dimensions: dict
    metadata: dict = Field(default_factory=lambda: {
        "created_at": datetime.now().isoformat(),
        "last_updated": datetime.now().isoformat(),
        "version": "1.0.0"
    })

    @field_validator('metadata')
    def update_timestamp(cls, v):
        v['last_updated'] = datetime.now().isoformat()
        return v

    def validate(self):
        """Validates against Life1 schema."""
        if LIFE1_SCHEMA:
            jsonschema.validate(self.model_dump(), LIFE1_SCHEMA)

class Branch(BaseModel):
    """Represents a simulation branch."""
    id: str
    name: str
    parent_state: str
    created_at: datetime
    status: str = "active"  # active, archived, adopted
    horizon: str = "meso"  # micro, meso, macro, branch
    modifications: List[Dict[str, Any]] = []
    simulation_log: List[Dict[str, Any]] = []
    narrative: Optional[str] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class LifeOS:
    """The main LifeOS engine."""

    def __init__(self, root_path: Optional[Path] = None):
        self.root = root_path or Path.home() / ".lifeos"
        self.state_file = self.root / "state.json"
        self.history_dir = self.root / "history"
        self.branches_dir = self.root / "branches"
        self.archive_dir = self.root / "archive"
        self.horizons_dir = self.root / "horizons"
        self.insights_dir = self.root / "insights"
        self._ensure_dirs()

    def _ensure_dirs(self):
        """Creates directory structure."""
        for d in [self.history_dir, self.branches_dir, self.archive_dir, self.horizons_dir, self.insights_dir]:
            d.mkdir(parents=True, exist_ok=True)

    def load_state(self) -> State:
        """Loads the current state from state.json."""
        if not self.state_file.exists():
            raise FileNotFoundError("state.json not found. Run 'lifeos init'.")
        with open(self.state_file, 'r') as f:
            data = json.load(f)
        state = State(**data)
        state.validate()
        return state

    def save_state(self, state: State):
        """Saves state atomically with backup."""
        # Backup
        if self.state_file.exists():
            backup = self.history_dir / f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"
            shutil.copy(self.state_file, backup)
        
        # Atomic write
        temp = self.state_file.with_suffix('.tmp')
        with open(temp, 'w') as f:
            json.dump(state.model_dump(), f, indent=2)
        os.rename(temp, self.state_file)
        
        # Log to history
        self._log_to_history(state)

    def _log_to_history(self, state: State):
        """Appends state to history JSONL."""
        log_file = self.history_dir / f"{datetime.now().strftime('%Y-%m-%d')}.jsonl"
        with open(log_file, 'a') as f:
            f.write(json.dumps(state.model_dump()) + '\n')

    def create_branch(self, name: str, modifications: List[Dict[str, Any]] = None) -> Branch:
        """Creates a new simulation branch."""
        state = self.load_state()
        branch_id = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{name.replace(' ', '_')}"
        branch_dir = self.branches_dir / branch_id
        branch_dir.mkdir(parents=True, exist_ok=True)

        # Fork state
        new_state_data = state.model_dump()
        # Apply modifications (simplified path traversal)
        if modifications:
            for mod in modifications:
                path_parts = mod['path'].split('.')
                current = new_state_data
                for part in path_parts[:-1]:
                    current = current[part]
                current[path_parts[-1]] = mod['new']

        # Save branch state
        branch_state = State(**new_state_data)
        branch_state_file = branch_dir / "state.json"
        with open(branch_state_file, 'w') as f:
            json.dump(branch_state.model_dump(), f, indent=2)

        branch = Branch(
            id=branch_id,
            name=name,
            parent_state=str(self.state_file),
            created_at=datetime.now(),
            modifications=modifications or []
        )
        
        # Save branch metadata
        with open(branch_dir / "branch.json", 'w') as f:
            json.dump(branch.model_dump(mode='json'), f, indent=2)

        return branch

    def get_branch(self, name: str) -> Optional[Branch]:
        """Loads a branch by name (partial match)."""
        for branch_dir in self.branches_dir.iterdir():
            if branch_dir.is_dir() and name in branch_dir.name:
                with open(branch_dir / "branch.json", 'r') as f:
                    data = json.load(f)
                return Branch(**data)
        return None

    def archive_branch(self, branch: Branch):
        """Moves a branch to the archive."""
        branch_dir = self.branches_dir / branch.id
        archive_branch_dir = self.archive_dir / "branches" / branch.id
        archive_branch_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(branch_dir), str(archive_branch_dir))
        branch.status = "archived"
        with open(archive_branch_dir / "branch.json", 'w') as f:
            json.dump(branch.model_dump(mode='json'), f, indent=2)

    def run_maintenance(self):
        """Archives stale branches and horizons."""
        now = datetime.now()
        # Check branches
        for branch_dir in self.branches_dir.iterdir():
            if branch_dir.is_dir():
                with open(branch_dir / "branch.json", 'r') as f:
                    data = json.load(f)
                branch = Branch(**data)
                if branch.horizon == "micro" and (now - branch.created_at).days > 2:
                    self.archive_branch(branch)
                elif branch.horizon == "meso" and (now - branch.created_at).days > 30:
                    self.archive_branch(branch)
                elif branch.horizon == "macro" and (now - branch.created_at).days > 365:
                    self.archive_branch(branch)
