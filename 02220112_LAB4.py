# Task 3: Implement the Node and LinkedQueue Class Structure
class Node:
    def __init__(self, data=None):
        self.data = data  
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0     
        print("Created new LinkedQueue")  
        
#Task 4: Implement Linked List-based Queue Operations 
    def enqueue(self, element):
        new_node = Node(element)  
        if self.rear is None:
            self.front = self.rear = new_node 
        else:
            self.rear.next = new_node  
            self.rear = new_node      
        self.size += 1  
        print(f"Enqueued {element} to the queue")
        self.display()  

    def dequeue(self):
        if self.is_empty():
            return None 
        dequeued_element = self.front.data  
        self.front = self.front.next  
        if self.front is None: 
            self.rear = None  
        self.size -= 1  
        print(f"Dequeued element: {dequeued_element}")
        return dequeued_element

    def peek(self):
        if not self.is_empty():
            print(f"Front element: {self.front.data}")
            return self.front.data
        return None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def display(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Display queue: {elements}")
        return elements

queue = LinkedQueue()  
queue.enqueue(10)  
queue.enqueue(20)  
queue.enqueue(30)  
queue.peek()  
queue.dequeue()  
queue.display()  
print(f"Queue size: {queue.size}") 