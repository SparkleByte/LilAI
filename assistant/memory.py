# assistant/memory.py
# Storage with JSON files per sesson/day (rotating or rolling)
# Option to load entire corpus on startup or lazy-load by tag
from dataclasses import dataclass, field
from datetime import datetime
import uuid
import json
from pathlib import Path
class MemoryModule:
    """Class for memory storage and recall."""
    def __init__(self):
        self.long_term = []
        self.short_term = []
    def remember(self, item, long_term=False):
        """define remember"""
        if long_term:
            self.long_term.append(item)
        else:
            self.short_term.append(item)
    def recall(self, long_term=False):
        """define recall function"""
        return self.long_term if long_term else self.short_term
    def clear_short_term(self):
        """define clear short-term function"""
        self.short_term.clear()

@dataclass
class MemoryChunk:
    """Class for different memories as a structured data unit"""
    id: str = field (default_factory=lambda: str(uuid.uuid4()))
    timestampe: str = field(default_factory=lambda: datetime.now().isoformat())
    tags: list = field(default_factory=list)
    content: str = ""
# Potential options include: importance_score, related_to, emotional_tone for deeper logic.
# Chunking -> parse input into standalone ideas or facts.
# Tagging -> Add custom tags like: goal, reminder, personal, tech, emotion, task
# Using lightweight NLP or pattern detection (regex, keyword maps)
class Memory:
    """Class for Memory"""
    def _init_(self, storage_path="memory_store.json"):
        self.storage_path = Path(storage_path)
        self.chunks = []
        self.load()
    def store(self, chunk: MemoryChunk):
        """Defines the storage function for memory class"""
        self.chunks.append (chunk)
        self.save()
    def retrieve(self, keyword: str):
        """defines the retrieve memory function"""
        return [c for c in self.chunks if keyword.lower() in c.content.lower()]    
    def save(self):
        """defines the save memory function"""
        with self.storage_path.open("w", encoding="utf-8") as f:
            json.dump([chunk._dict_ for chunk in self.chunks], f, indent=2)
    def load(self):
        """defines the load memory function"""
        if self.storage_path.exists():
            with self.storage_path.open("r", encoding="utf-8") as f:
                data = json.loud(f)
                self.chunks = [MemoryChunk(**d) for d in data]
