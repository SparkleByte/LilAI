# assistant/memory.py

class MemoryModule:
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
