# assistant/planner.py

class Planner:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def get_tasks(self, show_all=True):
        if show_all:
            return self.tasks
        return [t for t in self.tasks if not t["completed"]]
