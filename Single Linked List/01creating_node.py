# creating individual nodes manually and connecting them to form a linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
a = Node(1)
b = Node(2)
c = Node(3)
# print(c.next)

a.next = b
b.next = c

print(a.next)
