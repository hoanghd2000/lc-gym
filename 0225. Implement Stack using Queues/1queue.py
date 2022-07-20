class MyStack:

    def __init__(self):
        self.q1 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for i in range(len(self.q1) - 1):
            cur = self.q1.pop(0)
            self.q1.append(cur)
        cur = self.q1.pop(0)
        
        return cur

    def top(self) -> int:
        cur = 0
        for i in range(len(self.q1)):
            cur = self.q1.pop(0)
            self.q1.append(cur)
        return cur
        

    def empty(self) -> bool:
        if self.q1:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()