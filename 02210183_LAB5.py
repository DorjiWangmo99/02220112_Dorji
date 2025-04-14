#Part 1: Sequential Search Implementation by Phurpa Lhamo


def sequential_search(arr, target):
    comparisons = 0
    for index, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return index, comparisons
    return -1, comparisons


arr = [23, 45, 12, 67, 89, 34, 56]
target = 67

print(f"List: {arr}")
print(f"Searching for {target} using Sequential Search")

index, comparisons = sequential_search(arr, target)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

print(f"Number of comparisons: {comparisons}")


