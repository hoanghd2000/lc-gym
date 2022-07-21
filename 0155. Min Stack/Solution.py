class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.smallest_stack:
            cur_smallest = self.smallest_stack[-1]
            if val < cur_smallest:
                self.smallest_stack.append(val)
            else:
                self.smallest_stack.append(cur_smallest)
        else:
            self.smallest_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.smallest_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()