from collections import deque

class QueueWithDeque:
    def __init__(self):
        self.queue = deque()  # Initialize an empty deque to act as a queue

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)  # Adds the item to the end of the deque
    
    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.popleft()  # Removes and returns the first item
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)
