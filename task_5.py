class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, d):
        n = Node(d)
        n.next = self.head
        self.head = n

    def insert_at_end(self, d):
        n = Node(d)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def delete_node(self, d):
        t = self.head
        if t and t.data == d:
            self.head = t.next
            return
        p = None
        while t and t.data != d:
            p = t
            t = t.next
        if t:
            p.next = t.next

    def search(self, d):
        t = self.head
        while t:
            if t.data == d:
                return "Element found"
            t = t.next
        return "Element not found"

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

print("Linked List:")
l.display()

l.insert_at_beginning(5)
print("After inserting 5 at beginning:")
l.display()

l.delete_node(20)
print("After deleting 20:")
l.display()

print("Search 30:")
print(l.search(30))