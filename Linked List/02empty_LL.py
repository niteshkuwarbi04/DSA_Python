class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):

        # Empty Linked list
        self.head = None
        self.n = 0      # n = Number of nodes in linked list

L = LinkedList()
print(L) 