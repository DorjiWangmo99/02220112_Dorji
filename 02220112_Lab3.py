#Part2 by Dorji Wangmo
class Node:
    def __init__(self, data=None):
        self.data = data  
        self.next = None  
class LinkedStack:
    def __init__(self):
        self.top = None 
        self.size = 0     
        print("Created new LinkedStack")
        
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top  
        self.top = new_node  
        self.size += 1  
        print(f"Pushed {element} to the stack")
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")  
        popped_data = self.top.data  
        self.top = self.top.next  
        self.size -= 1  
        return popped_data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack") 
        return self.top.data  
    def is_empty(self):
        return self.size == 0  
    
    def size(self):
        return self.size  
    
    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Display stack: {elements}")
    
    def __str__(self):
        return f"Stack is empty: {self.is_empty()}"

stack = LinkedStack()  
print(stack)  
stack.push(10)  
stack.display()  
stack.push(20)  
stack.display()  
stack.push(30)  
stack.display()  
print(f"Top element: {stack.peek()}") 
popped_element = stack.pop()  
print(f"Popped element: {popped_element}") 
stack.display() 
print(f"Stack size: {stack.size}")  
print(stack)  
