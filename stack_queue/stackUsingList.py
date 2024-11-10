# LIFO=>Last in first out

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print("stack after pushes: ",stack)

top_element = stack.pop()
print("Popped element:", top_element)
print("Stack after pop:", stack)

if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

if stack:  # Check if stack is not empty
    top_element = stack[-1]
    print("Top element:", top_element)    