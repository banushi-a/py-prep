from collections import deque

class MyStack:

    def __init__(self):
        self.a = deque() #
        self.b = deque() # 
        # can only use .append and .popleft or [0]
        # invariant: the order of the queue a is in order of the stack
        

    def push(self, x: int) -> None:
        self.b.append(x)
        while len(self.a) != 0:
            self.b.append(self.a.popleft())
        self.a = self.b
        self.b = deque()
        

    def pop(self) -> int:
        return self.a.popleft()

    def top(self) -> int:
        return self.a[0]

    def empty(self) -> bool:
        return len(self.a) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()