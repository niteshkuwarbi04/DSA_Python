import ctypes

class doubleEndedQueue:

    def __init__(self):
        self.arr = self.__make__array(5)
        for i in range(0,5):
            self.arr[i] = 0
        self.front = -1
        self.rear = -1
        self.count = 0

    def insertFromFront(self,item):
        if(self.front==0 and self.rear==4):
            print("Queue is Full")
            return
        
        if(self.rear!=4):
            k=self.count
            for i in range(self.count,0,-1):
                self.arr[i] = self.arr[i-1]
                k = k-1

            self.arr[k]=item
            self.count+=1

            if(self.front==-1):
                self.front=0
                self.rear=0
            else:
                self.rear+=1
        else:
            self.front-=1
            self.arr[self.front]=item
            self.count+=1

    def insertFromRear(self,item):
        if(self.front==0 and self.rear==4):
            print("Queue is full")
            return
        
        if(self.front!=0):
            k = 0
            for i in range(0,4):
                self.arr[i] = self.arr[i+1]
                k = k + 1
            self.arr[k] = item
            self.count = self.count + 1
            if(self.rear==-1 and self.front==-1):
                self.rear = 4
                self.front = 4
            else:
                self.front = self.front - 1
        
        else:
            self.rear = self.rear + 1
            self.arr[self.rear] = item
            self.count = self.count + 1

    def delFromFront(self):
        if self.front == -1:
            print("Queue is empty")
        
        x = self.arr[self.front]

        self.arr[self.front] = 0
        self.count = self.count - 1

        if self.front == self.rear:
            self.front = self.rear - 1
        else:
            if self.front == 4:
                self.front = 0
            else:
                self.front = self.front + 1

    def delFromRear(self):
        if(self.front==-1):
            print("Queue Is Empty")

        x=self.arr[self.rear]

        self.arr[self.rear]=0
        self.count-=1

        if(self.front==self.rear):
            self.front=self.rear=-1
        else:
            if(self.front==4):
                self.front=0
            else:
                self.rear-=1

    def display(self):
        for i in range(5):
            print(self.arr[i],end=" ")
        print(f"\nfront: {self.front}, rear: {self.rear}, count: {self.count}")

    def __make__array(self,capacity):
        # this code creates a ctype array(static, fixed, referential) with size capacity
        return (capacity*ctypes.py_object)()
    
D = doubleEndedQueue()

while (True):
    D.display()

    ans = int(input('Enter the following operation: \n 1. Insert(front)\n 2. Insert(rear)\n 3. Delete(front)\n 4. Delete(rear)\n 5. Exit\n'))

    if ans == 1:
        item = int(input('Enter any item to insert: '))
        D.insertFromFront(item)
    
    if ans == 2:
        item = int(input('Enter any item to insert: '))
        D.insertFromRear(item)

    if ans == 3:
        D.delFromFront()

    if ans == 4:
        D.delFromRear()
    
    if ans == 5:
        break
    