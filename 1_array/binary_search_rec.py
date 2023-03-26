def binary_search_recursive(arr, low, high, x):
    # Base case: the element isn't in the array
    if low > high:
        return -1

    # Find the middle index
    mid = (low + high) // 2

    # Check if the middle element is the value we're looking for
    if arr[mid] == x:
        return mid

    # If the middle element is greater than x, search the left half of the array
    elif arr[mid] > x:
        return binary_search_recursive(arr, low, mid - 1, x)

    # If the middle element is less than x, search the right half of the array
    else:
        return binary_search_recursive(arr, mid + 1, high, x)


# Test the binary search function
arr = [2, 5, 8, 3, 1, 6]
x = 8
result = binary_search_recursive(arr, 0, len(arr) - 1, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")
