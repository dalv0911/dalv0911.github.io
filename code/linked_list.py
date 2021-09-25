class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data

# Singly Linked List


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        end = Node(data)
        if self.head == None:
            self.head = end
            return

        # Traveling through linked list to find trail of list
        n = self.head
        while n.next != None:
            n = n.next
        n.next = end

    def remove(self, data):
        n = self.head
        prev = self.head
        while n.next != None:
            if n.data == data:
                prev.next = n.next
                return
            else:
                prev = n
                n = n.next
        raise KeyError('Data not found')

    def show(self):
        n = self.head
        while n != None:
            print(n.data)
            n = n.next


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)

l.show()

print('Remove 3')
l.remove(3)

l.show()
