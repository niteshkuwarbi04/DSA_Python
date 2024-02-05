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

    def __make__array(self,capacity):
        # this code is a ctype array(static, referential) with size capacity
        return (capacity*ctypes.py_object)() 

L = apnaList()
print(L.len())
