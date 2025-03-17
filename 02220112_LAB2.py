class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def  __init__(self):
        self.head =0
        self.tail =0
        self.size =0

    def display(self):
        print(f"Current size: {self.size}")
        print(f"Head: {self.head}")
        print(f"Tail: {self.tail}")
    
    def append(self, element):
        new_node = Node(element)  
        if not self.head:  
            self.head = new_node  
            self.tail = new_node  
        else:
            self.tail.next = new_node  
            self.tail = new_node  
        self.size += 1  
        print(f"Appended {element} to the list")
    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return None
        current = self.head
        for _ in range(index):
            current = current.next  
        return current.data  
    
    def set(self, index, element):
        if index < 0 or index >=self.size:
            print("Index out of bounds")
            return None
        current = self.head
        for _ in range(index):
            current = current.next  
        current.data = element  
        print(f"Set element at index {index} to {element}")

    def size(self):
        return self.size
    def prepend(self, element):
        new_node = Node(element)
        if not self.head:  
            self.head = new_node 
            self.tail = new_node  
        else:
            new_node.next = self.head  
            self.head = new_node 
        self.size += 1  
        print(f"Prepended {element} to the list")
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))  
            current = current.next 
        print("Print linked list: ", " ".join(elements))


print("Created new list")
list = LinkedList()
list.display()
list.append(5)
print(f"Element at index 0: {list.get(0)}")
list.set(0,10)
print(f"Element at index 0 to: {list.get(0)}")
print(f"Current size: {list.size}")
list.prepend(10)
list.append(5)
list.print_list()