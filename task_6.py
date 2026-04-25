class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, d):
        n = Node(d)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def count_nodes(self):
        c = 0
        t = self.head
        while t:
            c += 1
            t = t.next
        return c

    def find_middle(self):
        s = f = self.head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s.data

    def reverse_list(self):
        p = None
        c = self.head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        self.head = p

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print("None")


l = LinkedList()

l.insert_at_end(10)
l.insert_at_end(20)
l.insert_at_end(30)
l.insert_at_end(40)

print("Number of nodes:", l.count_nodes())
print("Middle element:", l.find_middle())

l.reverse_list()
print("Reversed list:")
l.display()