class Stack:
    def __init__(self):
        self.data: list = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self):
        return "[" + ", ".join([f"{self.data[i]}" for i in range(len(self.data)-1, -1, -1)]) + "]"
