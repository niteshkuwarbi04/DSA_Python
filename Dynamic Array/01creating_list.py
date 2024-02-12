import ctypes       # by importing ctype: we'll create our own list with the help of C type array

class apnaList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # creating a c type array with size = self.size
        self.A = self.__make__array(self.size)

    def __make__array(self,capacity):
        # this code creates a ctype array(static, fixed, referential) with size capacity
        return (capacity*ctypes.py_object)() 
    
L = apnaList()
print(L)    # prints the memory address of object L