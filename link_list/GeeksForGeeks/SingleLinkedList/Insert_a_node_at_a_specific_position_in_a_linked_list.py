# https://www.geeksforgeeks.org/insert-a-node-at-a-specific-position-in-a-linked-list/
# Input: 3->5->8->10, data = 2, pos = 2
# Output: 3->2->5->8->10

# Input: 3->5->8->10, data = 11, pos = 5
# Output: 3->5->8->10->11

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Auxiliary Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node

def insert_pos(head,pos,new_value):
    if pos < 1:
        print("Invalid position")
        return head
    
    current = head
    count = 1
    while current is not None and count < pos - 1:
        current = current.next
        count += 1

    new_node = Node(new_value)
    new_node.next = current.next
    current.next = new_node



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

    pos = 3
    new_data = 4
    insert_pos(head,pos,new_data)
    print_list(head)