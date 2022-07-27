class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def clear(self):
        return self.data.clear()

    def length(self):
        return len(self.data)


s = Stack()
s.push(3)
s.push(10)
print(s.length())
print(s.peek())
print(s.pop())
s.clear()
print(s.length())
