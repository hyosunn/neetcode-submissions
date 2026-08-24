class MinStack:

    def __init__(self):
        self.stack = []
        self.minTrack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minTrack:
            self.minTrack.append(min(val, self.minTrack[-1]))
        else:
            pass
            self.minTrack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minTrack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    
    def getMin(self) -> int:
        return self.minTrack[-1]




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
        
