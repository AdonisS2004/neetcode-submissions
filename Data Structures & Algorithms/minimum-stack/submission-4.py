class MinStack:

    def __init__(self):
        self.stack = [float('inf')]
        self.min_stack = [float('inf')]
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.current_min:
            self.current_min = val
        self.min_stack.append(self.current_min)

    def pop(self) -> None:
        self.min_stack.pop()
        self.current_min = self.min_stack[-1]
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min
