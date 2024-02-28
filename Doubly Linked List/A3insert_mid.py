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
    
    def insert_head(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return
        
        else:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node
        self.n = self.n + 1

    def insert_last(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            current.next.prev = current
        self.n = self.n + 1

    def insert_mid(self,after,value):
        new_node = Node(value)
        current = self.head

        while current != None:
            if current.data == after:
                break
            current = current.next
        
        if current != None:   
            new_node.prev = current
            new_node.data = value
            new_node.next = current.next
            current.next = new_node
            new_node.next.prev = new_node
            self.n = self.n + 1
        else:
            print('Item not found')

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            if current.next:
                print("<-> ", end='')
            current = current.next

        print()

DLL = DoublyLinkedList()

print(DLL.__len__())

DLL.insert_head(20)
DLL.insert_head(30)
DLL.insert_head(40)
DLL.insert_last(60)
DLL.insert_last(70)

DLL.display()

DLL.insert_mid(20, 10)
DLL.display()
