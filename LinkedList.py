class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        # O(n)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
        # O(n)
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp                        

    def prepend(self, value):
        # O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True        

    def pop_first(self):
        # O(1)
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        # O(n)
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        # O(n)
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index, new_item):
        # O(n)
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.prepend(new_item)
        if index == self.length:
            return self.append(new_item)

        new_node = Node(new_item)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1                

        return True

    def remove(self, index):
        # O(n)
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1

        return temp


    # https://www.youtube.com/watch?v=D7y_hoT_YZI
    def reverse(self):
        # O(n)
        pre_node = None
        current = self.head
        next_node = current.next

        self.tail = current

        while current:
            next_node = current.next
            current.next = pre_node
            pre_node = current
            current = next_node

        self.head = pre_node
        return True    





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()

print('\npop from linked list')
my_linked_list.pop()
my_linked_list.print_list()

print('\nprepend')
my_linked_list.prepend(3)
my_linked_list.prepend(4)
my_linked_list.print_list()

print('\nPop first')
my_linked_list.pop_first()
my_linked_list.print_list()

print('\nGet')
get_node = my_linked_list.get(1)
print(get_node.value)

print('\nSet Value')
my_linked_list.set_value(0,20)
my_linked_list.print_list()

print('\nInsert')
my_linked_list.print_list()
print('After insert')
my_linked_list.insert(1,5)
my_linked_list.print_list()

print('\nRemove')
my_linked_list.remove(1)
my_linked_list.print_list()

print('\nReverse')
my_linked_list.reverse()
my_linked_list.print_list()



