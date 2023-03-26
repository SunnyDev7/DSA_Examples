def linear_search_iterative(arr, x):
    """
    Search for the element x in the array arr iteratively.
    Returns the index of x if found, otherwise returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# Test the linear search function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
result = linear_search_iterative(arr, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")
