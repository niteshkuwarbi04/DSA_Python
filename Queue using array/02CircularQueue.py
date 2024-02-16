import ctypes

class Queue:
    def __init__(self):
        self.arr = self.__make__array(5)
        for i in range(0,5):
            self.arr[i] = 0
        self.front = -1
        self.rear = -1

    def inqueue(self,item):
        if (self.front == 0 and self.rear ==4) or (self.front == self.rear + 1):
            print(f'Queue is full')
        else:
            if self.rear == 4:
                self.rear = 0
            else:
                self.rear = self.rear + 1
                self.arr[self.rear] = item
                if self.front == -1:
                    self.front = 0
                
    def dequeue(self):
        if self.front == -1:
            print(f'Queue is empty')
        else:
            x = self.arr[self.front]
            self.arr[self.front] = 0

            if self.front == 4:
                self.front = 0
            else:
                self.front = self.front + 1

            if self.rear == self.front:
                self.front = self.rear = -1

            print(f'Deleted item is: {x}')

    def display(self):
        if self.front >-1:
            for i in range(0, 5):
                print(self.arr[i], end=" ")
        print("\n")

    def __make__array(self,capacity):
        # this code creates a ctype array(static, fixed, referential) with size capacity
        return (capacity*ctypes.py_object)()
    
q = Queue()

while(True):

    q.display()

    ans = int(input('Enter any following operations: \n 1. Insert(from rear) \n 2. Delete(from front) \n 3. Exit \n'))

    if ans == 1:
        item = int(input('Enter any item to insert: '))
        q.inqueue(item)
    
    if ans == 2:
        q.dequeue()

    if ans == 3:
        break