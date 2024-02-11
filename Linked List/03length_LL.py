# length of linked list is number of nodes in linked list

class LinkedList:
    def __init__(self):

        # Empty Linked list
        self.head = None
        self.n = 0      # n = Number of nodes in linked list

    def __len__(self):
        return self.n

L = LinkedList()
print(len(L)) 