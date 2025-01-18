#Day 56: Sorting algorithms


#Implement sorting algorithms (e.g., bubble sort, merge sort).

# Implementation of Sorting Algorithms

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking for leftover elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example Usage
if __name__ == "__main__":
    # Test array for Bubble Sort
    bubble_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array for Bubble Sort:", bubble_array)
    bubble_sort(bubble_array)
    print("Sorted array with Bubble Sort:", bubble_array)

    # Test array for Merge Sort
    merge_array = [38, 27, 43, 3, 9, 82, 10]
    print("\nOriginal array for Merge Sort:", merge_array)
    merge_sort(merge_array)
    print("Sorted array with Merge Sort:", merge_array)
