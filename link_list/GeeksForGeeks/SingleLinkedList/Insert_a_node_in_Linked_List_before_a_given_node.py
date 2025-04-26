# https://www.geeksforgeeks.org/insert-a-node-in-linked-list-before-a-given-node/
# Input: head: 1 -> 2 -> 3 -> 4 -> 5 , newData = 6, key = 2
# Output: 1 -> 6 -> 2 -> 3 -> 4 -> 5 
# Explanation: After inserting node with value 6 before (key = 2) of the linked list, the resultant linked list will be: 1 -> 6 -> 2 -> 3 -> 4 -> 5 


# Input: head: 1 -> 3 -> 2, newData = 9, key = 1
# Output: 9 -> 1 -> 3 -> 2
# Explanation: After inserting node with value 9 before (key = 1) of the linked list, the resultant linked list will be: 9 -> 1 -> 3 -> 2

# Time Complexity: O(n), where n is the number of nodes in the list.
# Auxiliary Space: O(n)

class Node:
    def __init__(self, new_node):
        self.data = new_node
        self.next = None

def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node

def insert_before(head,key,new_value):
    current = head

    if current.data == key:
        new_node = Node(new_value)
        new_node.next = head
        return new_node
    
    while current.next.data is not None:
        if current.next.data == key:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node
            break
        current = current.next

    return head    



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

    head = insert_before(head, 6, 0)

    print_list(head)