import ctypes

class apnaList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # creating a c type array with size = self.size
        self.A = self.__make__array(self.size)
    
    def len(self):
        return self.n
    
    def append(self, item):
        if self.size == self.size:
            # resize
            self.__resize(self.size*2)

        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__make__array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def __str__(self):
        # [1,2,3]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        
        return '[' +  result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
        
    def pop(self):
        if self.n == 0:
            return 'Empty List'

        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return 'ValueError - Not in list'
    
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def __delitem__(self,pos):
        # delete
        if 0<= pos < self.n:        # checks whether the item's position is between 0 and nth 
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]  
            
            self.n = self.n - 1

    def __make__array(self,capacity):
        # this code is a ctype array(static, referential) with size capacity
        return (capacity*ctypes.py_object)() 

L = apnaList()
L.append('hello')
L.append(True)
L.append(1008) 
L.append(4.6) 

print(L)
del L[3]
print(L)