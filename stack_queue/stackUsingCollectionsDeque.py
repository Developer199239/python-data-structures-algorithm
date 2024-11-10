# LIFO=>Last in first out

# In Python, the collections.deque (double-ended queue) is a data structure from the collections module. It’s optimized for fast appends and pops from both ends of the queue, making it ideal for implementing a stack or queue.

# What is collections.deque
# deque is a generalization of stacks and queues.
# It allows appending and popping from both ends in constant time.
# It's more efficient than a Python list for inserting and deleting elements from the front of the collection.

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)
    
    def pop(self):
        """Remove and return the item from the top of the stack."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()
    
    def peek(self):
        """Return the item on the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
    
    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack size:", stack.size())  # Output: Stack size: 3
print("Top item:", stack.peek())    # Output: Top item: 30

print("Popped item:", stack.pop())  # Output: Popped item: 30
print("Popped item:", stack.pop())  # Output: Popped item: 20

print("Stack is empty:", stack.is_empty())  # Output: Stack is empty: False
print("Popped item:", stack.pop())          # Output: Popped item: 10
print("Stack is empty:", stack.is_empty())  # Output: Stack is empty: True
