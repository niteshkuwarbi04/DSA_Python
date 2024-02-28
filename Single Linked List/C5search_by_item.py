
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
    def traverse(self):
        current = self.head     # current = complete node(add+data)
        result = ''

        while current!=None :
            result  = result + str(current.data) + ' -> '
            current = current.next
        
        return result[:-3]      # slicing to avoid last ' -> '
    
    def append(self, value):

        new_node = Node(value)

        if self.head == None:       # if list is empty
            self.head = new_node
            self.n = self.n + 1
            return

        current = self.head

        while current.next!=None:
            current = current.next
        
        # you are now at the lastnode
        current.next = new_node
        self.n = self.n + 1

    # inserting in the middle/after an element
    def insert_after(self,after,value):

        new_node = Node(value)

        current = self.head

        while current!= None:
            if current.data == after:
                break
            current = current.next

        if current != None:  
            new_node.next = current.next
            current.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):

        if self.head == None:
            return 'Empty LinkedList'
        
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):      # will delete from tail

        if self.head == None:       # for empty LL
            print('LinkedList is already empty.')

        current = self.head

        if current.next == None:        # for LL having only 1 item
            return self.delete_head()

        while current.next.next != None:        # main logic 
            current = current.next

        # current -> 2nd last node
        current.next = None
        self.n = self.n - 1

    def remove(self,value):

        if self.head == None:
            print('LinkedList is empty')

        if self.head.data == value:     # checks whether it is the 1st item to be removed 
            return self.delete_head()

        current = self.head

        while current.next != None:
            if current.next.data == value:
                break
            current = current.next
        
        if current.next == None:        
            print('Not found')

        else:
            current.next = current.next.next

    def searchByItem(self,item):

        current = self.head
        pos = 0

        while current != None:
            if current.data == item:
                return pos
            current = current.next
            pos = pos + 1

        return 'Item not found'

L = LinkedList()

L.insert_head(1) 
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(L.traverse())

print(L.searchByItem(4))
