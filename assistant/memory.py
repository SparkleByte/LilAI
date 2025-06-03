# assistant/memory.py
import json
from pathlib import Path
from dataclasses import dataclass, field
from datetime import datetime
import uuid
class MemoryModule:
    """Class for memory storage and recall."""

    def __init__(self):
        self.long_term = []
        self.short_term = []

    def remember(self, item, long_term=False):
        if long_term:
            self.long_term.append(item)
        else:
            self.short_term.append(item)

    def recall(self, long_term=False):
        return self.long_term if long_term else self.short_term

    def clear_short_term(self):
        self.short_term.clear()

@dataclass
class MemoryChunk:
    """Class for different memories"""

    id: str = field (default_factory=lambda: str(uuid.uuid4()))
    timestampe: str = field(default_factory=lambda: datetime.now().isoformat())
    tags: list = field(default_factory=list)
    content: str = ""

class Memory:

    def _init_(self, storage_path = "memory_store.json"):
        self.storage_path = Path(storage_path)
        self.chunks = []
        self.load()

    def store(self, chunk: MemoryChunk):
        self.chunks.append (chunk)
        self.save()

    def retrieve(self, keyword: str):
        return [c for c in self.chunks if keyword.lower() in c.content.lower()]    
    def save(self):
        with self.storage_path.open("w", encoding="utf-8") as f:
            json.dump([chunk._dict_ for chunk in self.chunks], f, indent=2)
    def load(self):
        if self.storage_path.exists():
            with self.storage_path.open("r", encoding="utf-8") as f:
                data = json.loud(f)
                self.chunks = [MemoryChunk(**d) for d in data]
