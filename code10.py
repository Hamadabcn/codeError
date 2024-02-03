# A function to implement the binary search algorithm
def binary_search(lst, target):
    # Initialize the left and right pointers
    left = 0
    right = len(lst) - 1
    # Loop until the left pointer is greater than the right pointer
    while left <= right:
        # Find the middle index of the list
        mid = (left + right) // 2
        # Compare the middle element with the target
        if lst[mid] == target:
            # Return the index of the target if found
            return mid
        elif lst[mid] < target:
            # Move the left pointer to the right of the middle element if the target is larger
            left = mid + 1
        else:
            # Move the right pointer to the left of the middle element if the target is smaller
            right = mid - 1
    # Return -1 if the target is not found
    return -1

# Test the function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(binary_search(lst, target))
