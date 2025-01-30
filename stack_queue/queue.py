# Queue (FIFO: First-In, First-Out)
# Definition: A structure where the first item added is the first to be removed.

# Use When: Elements need to be processed in the order they arrived.

# Operations:

# Enqueue: Add an item to the end.
# Dequeue: Remove the item from the front.
# Peek: View the front item without removing it.
# Real-World Examples:

# Customer Service Lines: The first customer in line is served first.
# Print Queue: Documents are printed in the order they’re added to the queue.
# Task Scheduling: Tasks are processed in the order they are queued, useful in CPU scheduling.


# FIFo first in first out
# (first)1<-2<-3<-(last)
# insert(enqueue) 4
# (first)1<-2<-3<-4<-(last)
# dequeue will 1(first in first out) 
# (first)2<-3<-4(last)



class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueu(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1

        return temp.value                        

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_queue = Queue(4)
my_queue.enqueu(5)
my_queue.enqueu(6)
my_queue.enqueu(7)
my_queue.print_queue()
print("dequeue:",my_queue.dequeue(),"\n")
my_queue.print_queue()