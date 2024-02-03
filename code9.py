# A function to implement the merge sort algorithm
def merge_sort(lst):
    # Base case: if the list is empty or has one element, return it
    if len(lst) <= 1:
        return lst
    # Recursive case: divide the list into two halves and sort them separately
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    # Merge the two sorted halves into one sorted list
    return merge(left, right)

# A helper function to merge two sorted lists
def merge(left, right):
    result = []
    i = 0
    j = 0
    # Loop through both lists and compare their elements
    while i < len(left) and j < len(right):
        # If the left element is smaller, append it to the result and move to the next left element
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        # If the right element is smaller, append it to the result and move to the next right element
        else:
            result.append(right[j])
            j += 1
    # Append the remaining elements of the left or right list to the result
    result += left[i:]
    result += right[j:]
    return result

# Test the function
lst = [5, 3, 7, 2, 9, 1, 4, 6, 8]
print(merge_sort(lst))
