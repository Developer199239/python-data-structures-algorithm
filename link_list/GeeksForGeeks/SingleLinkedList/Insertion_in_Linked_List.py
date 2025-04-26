class Node:
    def __init__(self, new_node):
        self.data = new_node
        self.next = None

def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node 


def print_list(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next


if __name__ == "__main__":
    head = Node(2)
    head = insert_at_front(head,3)
    print_list(head)