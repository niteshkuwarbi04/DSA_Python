import ctypes

class Queue:
    def __init__(self):
        self.arr = self.__make__array(5)
        for i in range(0,5):
            self.arr[i] = 0
        self.front = -1
        self.rear = -1
    
    def inqueue(self,item):
        if (self.front == 0 and self.rear == 4) or (self.front == self.rear + 1):
            print(f'Overflow/Queue is full')

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
            print('Underflow/Queue is empty')

        else:
            x = self.arr[self.front]
            self.arr[self.front] = 0

            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                if self.front == 4:
                    self.front = 0
                else:
                    self.front = self.front + 1

    def display(self):
        for i in range(0, 5):
            print(self.arr[i], end=' ')
        print("\n")
        print(f"rear={self.rear} and front={self.front}")

    def __make__array(self,capacity):
        # this code creates a ctype array(static, fixed, referential) with size capacity
        return (capacity*ctypes.py_object)() 
    
q = Queue()

while(True):

    q.display()

    ans = int(input('Enter any following operation: \n 1. Insertion(rear) \n 2. Deletion(front) \n 3. Exit \n'))

    if ans == 1:
        item = int(input('Enter any item to insert: '))
        q.inqueue(item)
    
    if ans == 2:
        q.dequeue()

    if ans == 3:
        break