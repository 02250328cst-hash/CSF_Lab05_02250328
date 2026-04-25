class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack after pushing elements:")
s.display()

print("Top element:", s.peek())

print("Popped element:", s.pop())

print("Stack after popping:")
s.display()