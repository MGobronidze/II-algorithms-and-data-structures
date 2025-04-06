class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._shift_stacks()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._shift_stacks()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _shift_stacks(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


q = MyQueue()
q.push(1)        # in_stack: [1]
q.push(2)        # in_stack: [1, 2]
q.peek()         # out_stack: [2, 1] → დაბრუნდება 1
q.pop()          # out_stack: [2] → წაიშლება 1
q.empty()        # False