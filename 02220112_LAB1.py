class CustomList:
    def __init__(self, capacity=10):
        self._maxcapacity = capacity
        self._currentsize = 0
        self._array = [None] * capacity
        print(f"Created new CustomList with capacity: {self._maxcapacity}")
        print(f"Current size: {self._currentsize}")    

    def append(self, element):
        if self._currentsize == self._maxcapacity:
            print("List is full, cannot append.")
            return
        self._array[self._currentsize] = element
        self._currentsize += 1
        print(f"Appended {element} to the list")
    
    def get(self, index):
        if 0 <= index < self._currentsize:
            return self._array[index]
        else:
            raise IndexError("Error!")
        
    def set(self, index, element):
        if 0 <= index < self._currentsize:
            self._array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            raise IndexError("Error!")
        
    def size(self):
        return self._currentsize  
cl = CustomList()
cl.append(5)
print(f"Element at index 0: {cl.get(0)}")
cl.set(0, 10)
print(f"Element at index 0: {cl.get(0)}")
print(f"Size of the list: {cl.size()}")
