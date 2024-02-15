import ctypes

class stack:
    def __init__(self):
        self.arr = self.__make__array(5)
        self.top = -1

    def push(self, item):
        if self.top == 4:
            print('Overflow/Stackfull')

        else:
            self.top = self.top + 1
            self.arr[self.top] = item

    def len(self):
        return self.top
    
    def display(self):
        for i in range(self.top, -1, -1):
            print(self.arr[i]) 

    def __make__array(self,capacity):
        # this code creates a ctype array(static, fixed, referential) with size capacity
        return (capacity*ctypes.py_object)() 
    
S = stack()
S.push(2)
S.push(3)
S.push(4)

S.display()
