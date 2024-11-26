class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def is_empyt(self):
        return not (self.stack1 or self.stack2)

    def size(self):
        return len(self.stack1) + len(self.stack2)


queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued:", queue.dequeue())  # Output: Dequeued: 1
queue.enqueue(4)
print("Dequeued:", queue.dequeue())  # Output: Dequeued: 2
print("Dequeued:", queue.dequeue())  # Output: Dequeued: 3
print("Dequeued:", queue.dequeue())  # Output: Dequeued: 4

