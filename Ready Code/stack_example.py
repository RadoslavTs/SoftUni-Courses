class StackExample:
    def __init__(self):
        self.stack = []

    def push_value(self, value):
        self.stack.append(value)

    def pop_value(self, value):
        return self.stack.pop(value)

    def last_value(self):
        return self.stack[-1]


stack = StackExample()

