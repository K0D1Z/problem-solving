class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum_arr = []
        
    def push(self, value: int) -> None:
        if not self.stack:
            self.minimum_arr.append(value)
        elif self.minimum_arr[-1] >= value:
            self.minimum_arr.append(value)
        self.stack.append(value)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.minimum_arr[-1]:
                self.minimum_arr.pop()
            self.stack.pop()
         
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minimum_arr:
            return self.minimum_arr[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()