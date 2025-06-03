# assistant/core.py
from assistant.memory import Memory, MemoryChunk

class Assistant:
    def _init_(self):
        self.memory = Memory()
    def handle_input(self, user_input):
        chunk = MemoryChunk(content=user_input)
        self.memory.store(chunk)
        return f"Stored: {user_input}"
    def query_memory(self,keyword):
        matches = self.memory.retrieve(keyword)
        return matches
    def run_assistant():
        print("✨ LILAI is waking up… How can I assist you today?")
