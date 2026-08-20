class StackElement:
    def __init__(self, value = None, minimum = None):
        self.value = value
        self.minimum = minimum

class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, value: int) -> None:
        if self.stack:
            node = StackElement(value, min(self.stack[-1].minimum, value))
        else:
            node = StackElement(value, value)
        self.stack.append(node)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()