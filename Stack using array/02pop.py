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

    def pop(self):
        if self.top == -1:
            print('Underflow/Stack is empty')
        
        else:
            x = self.arr[self.top]
            print(f'Popped item is: {x}.')
            self.top = self.top - 1

    def len(self):
        return self.top
    
    def display(self):
        for i in range(self.top, -1, -1):
            print(self.arr[i]) 
            
    def __make__array(self,capacity):
        # this code creates a ctype array(static, fixed, referential) with size capacity
        return (capacity*ctypes.py_object)() 
    
S = stack() 

while(True):
    S.display()

    ans = int(input('Enter any following operations: \n 1. Push \n 2. Pop \n 3. Exit \n'))

    if ans == 1:
        item = int(input('Enter any item: '))
        S.push(item)

    if ans == 2:
        S.pop()

    if ans == 3:
        break