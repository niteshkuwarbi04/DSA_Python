# Program to reverse a linked list containing integer data

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        self.n = self.n + 1

    def traverse(self):
        current = self.head

        result = ''
        while current!=None :
            result  = result + str(current.data) + ' -> '
            current = current.next
        
        return result[:-3]

    def reverse(self):
        prev_node = None
        curr_node = self.head

        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
        
        self.head = prev_node

L = LinkedList()

L.insert_head(6)
L.insert_head(7)
L.insert_head(8)
L.insert_head(9)

print(L.traverse())

L.reverse()

print(L.traverse())
