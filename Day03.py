class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_at_end(head, data):
    new_node = Node(data)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node


# Creating linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original Linked List:")
print_list(head)

head = insert_at_beginning(head, 5)
print("After inserting at beginning:")
print_list(head)

insert_at_end(head, 40)
print("After inserting at end:")
print_list(head)
