class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)


q = Queue()

q.enqueue('Nishen')
q.enqueue('Ishan')
q.enqueue('Kishan')

print("Customers waiting:")
q.display()

served = q.dequeue()
print("Serving customer:", served)

print("Remaining queue:")
q.display()