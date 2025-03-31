#Part 1: Queue Implementation using Array
#By Phurpa Lhamo
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity, self.queue, self.front, self.rear = capacity, [None] * capacity, -1, -1
        print(f"Created new Queue with capacity: {capacity}")

    def is_empty(self): return self.front == -1
    def is_full(self): return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, element):
        if self.is_full(): return print("Queue is full! Cannot enqueue.")
        if self.is_empty(): self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        print(f"Enqueued {element} to the queue")
    
    def dequeue(self):
        if self.is_empty(): return print("Queue is empty! Cannot dequeue.")
        element, self.front = self.queue[self.front], (self.front + 1) % self.capacity if self.front != self.rear else -1
        if self.front == -1: self.rear = -1
        print(f"Dequeued element: {element}")
        return element
    
    def peek(self):
        return print(f"Front element: {self.queue[self.front]}") if not self.is_empty() else print("Queue is empty! No front element.")
    
    def size(self): return 0 if self.is_empty() else (self.rear - self.front + self.capacity) % self.capacity + 1
    
    def display(self):
        if self.is_empty(): return print("Queue is empty!")
        elements, index = [], self.front
        while index != self.rear:
            elements.append(self.queue[index])
            index = (index + 1) % self.capacity
        elements.append(self.queue[self.rear])
        print(f"Display queue: {elements}")


queue = ArrayQueue()
print("Queue is empty:", queue.is_empty())
queue.enqueue(10)
queue.display()
queue.enqueue(20)
queue.display()
queue.enqueue(30)
queue.display()
queue.peek()
queue.dequeue()
queue.display()
print("Queue size:", queue.size())
