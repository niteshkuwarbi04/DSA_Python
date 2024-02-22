import ctypes

class DQueue:

    def __init__(self):
        self.arr = self.__make__array(5)
        for i in range(0,5):
            self.arr[i] = 0
        self.front = -1
        self.rear = -1
        self.count = 0

    def insertFromFront(self,item):
        if(self.front==0 and self.rear==4):
            print("Queue is full")
            return
        
        if(self.front==-1):
            self.front = self.rear = 0
        
        if(self.front!=4):
            k = self.count
            for i in range(self.count,0,-1):
                self.arr[i] = self.arr[i-1]
                k = k - 1
            self.arr[k] = item
            self.count += 1
            self.rear += 1
        else:
            self.front = self.front - 1
            self.arr[self.front] = item
            self.count = self.count + 1

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
                self.rear = self.rear + 1
                self.arr[self.rear] = item

    def display(self):
        for i in range(5):
            print(self.arr[i],end=" ")
        print(f"front {self.front}, rear {self.rear}, self.count {self.count}")

    def __make__array(self,capacity):
        # this code creates a ctype array(static, fixed, referential) with size capacity
        return (capacity*ctypes.py_object)()
    
D = DQueue()

D.insertFromFront(10)
D.insertFromFront(20)
D.insertFromRear(30)

D.display()