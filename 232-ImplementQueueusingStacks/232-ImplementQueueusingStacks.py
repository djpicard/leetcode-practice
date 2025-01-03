class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self) -> int:
        if self.st1:
            return self.st1.pop()
        return -1

    def peek(self) -> int:
        return self.st1[-1]

    def empty(self) -> bool:
        return len(self.st1) == 0


# Your MyQueue object will be inst1ntiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()