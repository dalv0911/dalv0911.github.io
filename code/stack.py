class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, data):
        n = Node(data)
        if self.top == None:
            self.top = n
        else:
            n.next = self.top
        # Change the added node to top of stack
        self.top = n

    def pop(self):
        if self.top == None:
            raise KeyError('Stack is empty')
        n = self.top
        self.top = self.top.next

        return n.data


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())
