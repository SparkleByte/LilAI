# assistant/planner.py

class Planner:
    """Class generates plans and step breakdowns for user input.""" 
    def __init__(self):
        self.tasks = []
        self.current_plan = []
    def add_task(self, task):
        """defines add task function"""
        self.tasks.append({"task": task, "completed": False})
    def complete_task(self, index):
        """defines complete task function"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
    def get_tasks(self, show_all=True):
        """defines get tasks function"""
        if show_all:
            return self.tasks
        return [t for t in self.tasks if not t["completed"]]
    def create_plan(self, user_input):
        """Function breaks input into actionable steps."""
        # Placeholder parsing - I'll improve this later
        steps = user_input.lower().split(" and ")
        self.current_plan = [step.strip() for step in steps if step]
        return self.current_plan
    def get_next_step(self):
        """Function returns the next step in the plan."""
        if self.current_plan:
            return self.current_plan.pop(0)
        return None
