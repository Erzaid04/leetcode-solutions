class MinStack:

    def __init__(self):
        self.st = []
        self.ms = []

    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.ms:
            self.ms.append(value)
        else:
            self.ms.append(min(value,self.ms[-1]))


    def pop(self) -> None:
        if not self.st:
            return -1
        
        self.ms.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.ms[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()