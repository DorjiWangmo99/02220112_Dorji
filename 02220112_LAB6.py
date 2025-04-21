#Part two by Dorji Wangmo
def merge_sort(arr):
    comparisons = 0
    array_accesses = 0

    def merge(left, right):
        nonlocal comparisons, array_accesses
        sorted_array = []
        i = j = 0

        while i < len(left) and j < len(right):
            array_accesses += 2  
            comparisons += 1 

            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        while i < len(left):
            array_accesses += 1  
            sorted_array.append(left[i])
            i += 1

        while j < len(right):
            array_accesses += 1  
            sorted_array.append(right[j])
            j += 1

        return sorted_array

    def merge_sort_recursive(arr):
        nonlocal comparisons, array_accesses
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        array_accesses += len(left) + len(right)  
        left_sorted = merge_sort_recursive(left)
        right_sorted = merge_sort_recursive(right)

        return merge(left_sorted, right_sorted)

    sorted_arr = merge_sort_recursive(arr)
    return sorted_arr, comparisons, array_accesses


arr = [38, 27, 43, 3, 9, 82, 10]
print(f"Original List: {arr}")

sorted_list, num_comparisons, num_array_accesses = merge_sort(arr)

print(f"Sorted using Merge Sort: {sorted_list}")
print(f"Number of comparisons: {num_comparisons}")
print(f"Number of array accesses: {num_array_accesses}")