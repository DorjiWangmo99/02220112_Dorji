#Part 2 by Dorji Wangmo
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0  
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1  

        if arr[mid] == target:
            return mid, comparisons  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1, comparisons  

def binary_search_recursive(arr, target, low, high, comparisons=0):
    if low > high:
        return -1, comparisons  

    mid = (low + high) // 2
    comparisons += 1  

    if arr[mid] == target:
        return mid, comparisons  
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)

# Example usage
if __name__ == "__main__":
    arr = [12, 23, 34, 45, 56, 67, 89]
    target = 67

    print("Sorted List:", arr)
    
    # Iterative version
    index_iterative, comparisons_iterative = binary_search_iterative(arr, target)
    if index_iterative != -1:
        print(f"Found at index {index_iterative}")
    else:
        print("Not found")
    print(f"Number of comparisons (iterative): {comparisons_iterative}")

    # Recursive version
    index_recursive, comparisons_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if index_recursive != -1:
        print(f"Found at index {index_recursive}")
    else:
        print("Not found")
    print(f"Number of comparisons (recursive): {comparisons_recursive}")
