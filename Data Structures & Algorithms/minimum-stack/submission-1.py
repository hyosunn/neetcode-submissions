class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minList:
            val = min(val, self.minList[-1])
        else:
            pass

        self.minList.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minList.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minList[-1]
        
