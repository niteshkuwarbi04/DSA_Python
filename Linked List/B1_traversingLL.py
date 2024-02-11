class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):

        # Empty Linked list
        self.head = None
        self.n = 0      # n = Number of nodes in linked list

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)      # creating new node
        new_node.next = self.head   # creating connection
        self.head = new_node        # reassign head

        self.n = self.n + 1         # increment n

    # Traverse
    def __str__(self):
        current = self.head     # current = complete node(add+data)
        result = ''

        while current!=None :
            result  = result + str(current.data) + ' -> '
            current = current.next
        
        return result[:-3]      # slicing to avoid last ' -> '

L = LinkedList()
L.insert_head(1) 
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(L) 
