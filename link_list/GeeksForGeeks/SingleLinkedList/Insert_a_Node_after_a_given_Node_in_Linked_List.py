# https://www.geeksforgeeks.org/insert-a-node-after-a-given-node-in-linked-list/
# Examples:
# Input: LinkedList = 2 -> 3 -> 4 -> 5, newData = 1, key = 2
# Output: LinkedList = 2 -> 1 -> 3 -> 4 -> 5

# Input: LinkedList = 1 -> 3 -> 5 -> 7, newData = 1, key = 2
# Output: Node not found
# Time Complexity: O(N), where N is the number of nodes in the linked list.
# Auxiliary Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node

def insert_after(head,key,new_data):
    current = head
    while current is not None:
        if current.data == key:
            new_node = Node(new_data)
            temp = current.next
            current.next = new_node
            new_node.next = temp
            return
        current = current.next

    print("Node not found")

def print_list(head):
    current = head
    
    while current is not None:
        print(current.data)
        current = current.next


if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 2 -> 3 -> 5 -> 6
    head = None
    head = insert_at_front(head,6)
    head = insert_at_front(head,5)
    head = insert_at_front(head,3)
    head = insert_at_front(head,2)
    print_list(head)
    print("Original Linked List")

    key = 3
    new_data = 4
    insert_after(head,key,new_data)
    print_list(head)