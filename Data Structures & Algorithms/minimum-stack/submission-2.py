class MinStack:

    def __init__(self):
        self.minimum = 2**31-1
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minimum:
            self.minimum = val
        self.minimums.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()
        if self.minimums:
            self.minimum = self.minimums[-1]
        else:
            self.minimum = 2**31-1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
