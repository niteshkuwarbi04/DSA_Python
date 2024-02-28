class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
DLL = DoublyLinkedList()

print(DLL.__len__())