def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Find the middle index
        mid = low + (low + high) // 2

        # Check if the middle element is the value we're looking for
        if arr[mid] == x:
            return mid

        # If the middle element is greater than x, search the left half of the array
        elif arr[mid] > x:
            high = mid - 1

        # If the middle element is less than x, search the right half of the array
        else:
            low = mid + 1

    # If the element isn't in the array, return -1
    return -1


# Test the binary search function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 2
result = binary_search_iterative(arr, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")
