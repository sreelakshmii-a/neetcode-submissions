class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=float('inf')
        self.minStack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack)==0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1],val))
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if len(self.minStack) != 0:
            self.mini=self.minStack[-1]
    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) == 0:
            return None
        return self.minStack[-1]
