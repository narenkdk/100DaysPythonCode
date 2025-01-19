#Day 57: Search algorithms


#Implement searching algorithms (e.g., binary search).

def binary_search_iterative(arr, target):
    """
    Iterative binary search to find the index of the target in a sorted array.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, left, right, target):
    """
    Recursive binary search to find the index of the target in a sorted array.
    """
    if left > right:
        return -1  # Base case: target not found
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, right, target)
    else:
        return binary_search_recursive(arr, left, mid - 1, target)

# Test both functions
if __name__ == "__main__":
    # Sorted array
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    
    # Iterative binary search
    result_iterative = binary_search_iterative(sorted_array, target)
    print(f"Iterative: Target found at index {result_iterative}" if result_iterative != -1 else "Target not found")
    
    # Recursive binary search
    result_recursive = binary_search_recursive(sorted_array, 0, len(sorted_array) - 1, target)
    print(f"Recursive: Target found at index {result_recursive}" if result_recursive != -1 else "Target not found")
