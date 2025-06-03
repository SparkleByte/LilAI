# assistant/core.py
from assistant.memory import Memory, MemoryChunk
from assistant.planner import Planner
class Assistant:
    """Class Assistant created"""
    def _init_(self):
        self.memory = Memory()
        self.planner = Planner()
    def handle_input(self, user_input):
        """Defines the input function."""
        chunk = MemoryChunk(content=user_input)
        self.memory.store(chunk)
        return f"Stored: {user_input}"
    def query_memory(self,keyword):
        """defines the query memory function"""
        matches = self.memory.retrieve(keyword)
        return matches
    
   # def run_assistant():
     #   """defines the initial output to user."""
     #   print("✨ LILAI is waking up… How can I assist you today?")
    
    def generate_response(self, user_input):
        """Function to generate responses based on planning logic."""
        plan = self.planner.create_plan(user_input)
       
       # Store the plan as a memory chunk
        chunk = MemoryChunk(content=str(plan), tags=["plan", "generated"])
        self.memory.store(chunk)
    
        # Format response
        response = "Here's what I understand you want to do:\n"
        for idx, step in enumerate(plan, 1):
            response += f"{idx}. {step}\n"
        
        return response