def linear_search_recursive(arr, x, index=0):
    """
    Search for the element x in the array arr recursively.
    Returns the index of x if found, otherwise returns -1.
    """
    # Base case: if the array is empty, x is not in the array
    if index == len(arr):
        return -1

    # If the element is found, return its index
    if arr[index] == x:
        return index

    # Recursively search the rest of the array
    return linear_search_recursive(arr, x, index + 1)


# Test the linear search function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
result = linear_search_recursive(arr, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")
