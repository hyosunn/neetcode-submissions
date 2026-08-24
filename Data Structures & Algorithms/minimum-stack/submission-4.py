class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]




""" OPTIMAL O(1) Time SOLUTION: Using Prefix Min Stack:
        - Essentially, create another stack that keeps track of last recorded minimum

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
"""
        
