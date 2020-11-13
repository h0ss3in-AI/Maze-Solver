class BaseFrontier:
    def __init__(self):
        self.frontier = []

    def add(self):
        pass

    def remove(self):
        pass

    def is_empty(self):
        return len(self.frontier) == 0

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
