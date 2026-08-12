class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = [2**31]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_.append(min(self.min_[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]
