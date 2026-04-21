"""
LifeOS Core Module
Manages the LifeOS engine: State, Branches, Archives, and Physics.
Schemaless-by-default: schemas are suggestions, not enforced constraints.
"""

import json
import os
import shutil
import fcntl
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, field_validator

# --- Schemas (Loaded as reference templates, not validation rules) ---
LIFE1_SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "life1.json"
LIFE2_SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "life2.json"

def load_schema(path: Path) -> dict:
    """Loads a schema file as a reference template."""
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {}

# Load schemas as reference only - no validation enforcement
LIFE1_SCHEMA = load_schema(LIFE1_SCHEMA_PATH)
LIFE2_SCHEMA = load_schema(LIFE2_SCHEMA_PATH)

# --- Pydantic Models ---

class State(BaseModel):
    """Represents a snapshot of life.
    
    Schemaless design: accepts any valid JSON structure.
    life1/life2 schemas are reference templates only.
    Custom domains can be added dynamically.
    """
    # Core fields from life1 ontology (optional, for backward compatibility)
    identity: Optional[dict] = None
    biology: Optional[dict] = None
    psychology: Optional[dict] = None
    social_connections: Optional[dict] = None
    environment: Optional[dict] = None
    lifecycle: Optional[dict] = None
    activities_practices: Optional[dict] = None
    existential_dimensions: Optional[dict] = None
    
    # Dynamic extension point for custom ontologies
    custom_domains: Optional[dict] = None
    
    # Catch-all for any other fields (schemaless flexibility)
    metadata: dict = Field(default_factory=lambda: {
        "created_at": datetime.now().isoformat(),
        "last_updated": datetime.now().isoformat(),
        "version": "1.1.0"  # Updated to reflect schemaless design
    })

    @field_validator('metadata')
    def update_timestamp(cls, v):
        v['last_updated'] = datetime.now().isoformat()
        return v

    def get_schema_hints(self, domain: str = "life1") -> dict:
        """Returns schema hints for a given domain.
        
        This is a suggestion tool for the Agent, not a validation rule.
        The Agent can choose to follow these hints or ignore them.
        
        Args:
            domain: 'life1' for individual ontology, 'life2' for civilization
        
        Returns:
            Dictionary containing the schema structure as a reference template
        """
        if domain == "life1":
            return LIFE1_SCHEMA
        elif domain == "life2":
            return LIFE2_SCHEMA
        else:
            return {}

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
        # No validation - schemaless design
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

    def create_branch(self, name: str, modifications: List[Dict[str, Any]] = None, reasoning: str = None) -> Branch:
        """Creates a new simulation branch with optional reasoning trace.
        
        Args:
            name: Branch name
            modifications: List of modification operations
            reasoning: Human-readable explanation of why these modifications were made
        """
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
        
        # Add reasoning trace if provided
        if reasoning:
            branch.simulation_log.append({
                "type": "reasoning",
                "content": reasoning,
                "timestamp": datetime.now().isoformat()
            })

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

    def get_branches_for_review(self, horizon: str = None, older_than_days: int = None) -> List[Branch]:
        """Returns branches that need Agent review for archival decisions.
        
        This replaces the auto-archive maintenance with Agent-curated review.
        
        Args:
            horizon: Filter by horizon type (micro, meso, macro)
            older_than_days: Only return branches older than this many days
        
        Returns:
            List of branches for the Agent to review
        """
        now = datetime.now()
        review_candidates = []
        
        for branch_dir in self.branches_dir.iterdir():
            if not branch_dir.is_dir():
                continue
                
            branch_file = branch_dir / "branch.json"
            if not branch_file.exists():
                continue
                
            with open(branch_file, 'r') as f:
                data = json.load(f)
            
            branch = Branch(**data)
            
            # Apply filters
            if horizon and branch.horizon != horizon:
                continue
                
            if older_than_days:
                age_days = (now - branch.created_at).days
                if age_days < older_than_days:
                    continue
            
            review_candidates.append(branch)
        
        return review_candidates

    def search_timeline(self, query: str, horizon: str = "all") -> List[Dict[str, Any]]:
        """Searches timeline history for relevant entries.
        
        This is an ontology-free search that works across all data structures.
        It uses simple keyword matching (can be enhanced with embeddings later).
        
        Args:
            query: Search query string
            horizon: Time horizon filter (micro, meso, macro, all)
        
        Returns:
            List of matching entries with context
        """
        results = []
        query_lower = query.lower()
        
        # Search in history files
        if self.history_dir.exists():
            for history_file in self.history_dir.glob("*.jsonl"):
                with open(history_file, 'r') as f:
                    for line in f:
                        try:
                            entry = json.loads(line.strip())
                            # Simple keyword search in string values
                            entry_str = json.dumps(entry).lower()
                            if query_lower in entry_str:
                                results.append({
                                    "source": str(history_file),
                                    "entry": entry,
                                    "type": "history"
                                })
                        except json.JSONDecodeError:
                            continue
        
        # Search in active branches
        for branch_dir in self.branches_dir.iterdir():
            if not branch_dir.is_dir():
                continue
            
            state_file = branch_dir / "state.json"
            if state_file.exists():
                with open(state_file, 'r') as f:
                    try:
                        state_data = json.load(f)
                        state_str = json.dumps(state_data).lower()
                        if query_lower in state_str:
                            results.append({
                                "source": str(state_file),
                                "entry": state_data,
                                "type": "branch_state",
                                "branch_id": branch_dir.name
                            })
                    except json.JSONDecodeError:
                        continue
        
        return results
