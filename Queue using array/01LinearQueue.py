import ctypes

class Queue:
    def __init__(self):
        self.arr = self.__make__array(5) 
        self.front = -1
        self.rear = -1

    def insert(self,item):
        if self.rear== 4:
            print('Overflow/Stackfull')
            self.over=1

        else:
            self.rear = self.rear + 1
            self.arr[self.rear] = item

            if self.front == -1:
                self.front = 0
    
    def delete(self):
        if self.front == -1:
            print('Underflow/Queue is empty')

        else:
            x = self.arr[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = self.front + 1
            
            print(f'Deleted item is: {x}')

    def display(self):
        if(self.front==-1):
            return
        for i in range(self.front,self.rear+1):
            print(self.arr[i],end=" ")
        print("\n")

    def __make__array(self,capacity):
        # this code creates a ctype array(static, fixed, referential) with size capacity
        return (capacity*ctypes.py_object)() 
    
q = Queue()

while(True):

    q.display()

    ans = int(input('Enter any following operation: \n 1. Insertion \n 2. Deletion \n 3. Exit \n'))

    if ans == 1:
        item = int(input('Enter any item to insert: '))
        q.insert(item)
    
    if ans == 2:
        q.delete()

    if ans == 3:
        break