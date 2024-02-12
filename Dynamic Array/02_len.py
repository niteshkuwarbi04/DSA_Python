import ctypes

class apnaList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # creating a c type array with size = self.size
        self.A = self.__make__array(self.size)

    def len(self):
        return self.n       # returns the length of array i.e., number of item (n)
    
    def __make__array(self,capacity):
        # this code is a ctype array(static, referential) with size capacity
        return (capacity*ctypes.py_object)()     
    
L = apnaList()
print(L.len()) 