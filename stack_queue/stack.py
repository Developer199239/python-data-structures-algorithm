# Stack (LIFO: Last-In, First-Out)
# Definition: A structure where the last item added is the first to be removed.

# Use When: The most recent element needs to be processed first.

# Operations:

# Push: Add an item to the top.
# Pop: Remove the item from the top.
# Peek: View the top item without removing it.
# Real-World Examples:

# Browser Back Button: Tracks pages visited, so pressing "back" returns to the most recent page first.
# Undo in Text Editors: Reverses the most recent action taken, like typing or deleting.
# Call Stack in Programming: Functions are stored in the call stack, where the last function called is the first one completed.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#
#LIFO=> Last in frist out
# (top)1->2->3->(bottom)
# Insert 10 
# (top)10->1->2->3->(bottom)
# pop 
# (top)1->2->3->(bottom)

class Stack:
    def __init__(self, value):        
        new_node = Node(value)
        self.top = new_node
        self.height = 1


    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


    #
    # 1->None
    #          top->3->23->7->None
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value            


    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
print("stack items")
my_stack.print_stack()
print('\n')

print("Pop item for stack")
print(my_stack.pop(),'\n')