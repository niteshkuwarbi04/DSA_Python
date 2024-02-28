# length of linked list is number of nodes in linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
a = LinkedList()

print(len(a))