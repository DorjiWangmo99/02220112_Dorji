# Part 1 by Phurpa Lhamo.

class ArrayStack:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._stack = [None] * self._capacity
        self._top = -1
        print(f"Created new ArrayStack with capacity: {self._capacity}")
    
    def is_empty(self):
        return self._top == -1
    
    def push(self, element):
        if self._top + 1 == self._capacity:
            print("Stack overflow! Cannot push more elements.")
            return
        self._top += 1
        self._stack[self._top] = element
        print(f"Pushed {element} to the stack")
    
    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop from an empty stack.")
            return None
        popped_element = self._stack[self._top]
        self._stack[self._top] = None 
        self._top -= 1
        print(f"Popped element: {popped_element}")
        return popped_element
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        print(f"Top element: {self._stack[self._top]}")
        return self._stack[self._top]
    
    def size(self):
        print(f"Stack size: {self._top + 1}")
        return self._top + 1
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Display stack:", [self._stack[i] for i in range(self._top + 1)])
    

stack = ArrayStack()
print("Stack is empty:", stack.is_empty())
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.peek()
stack.pop()
stack.size()
stack.display()
