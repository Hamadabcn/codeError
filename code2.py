# A function to sort a list of numbers using bubble sort algorithm
def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# A function to sort a list of numbers using insertion sort algorithm
def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# A function to sort a list of numbers using selection sort algorithm
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

original_lst = [5, 3, 7, 2, 9, 1, 4, 6, 8]

# Test bubble sort
bubble_sorted_lst = bubble_sort(original_lst.copy())
print("Bubble Sort:", bubble_sorted_lst)

# Test insertion sort
insertion_sorted_lst = insertion_sort(original_lst.copy())
print("Insertion Sort:", insertion_sorted_lst)

# Test selection sort
selection_sorted_lst = selection_sort(original_lst.copy())
print("Selection Sort:", selection_sorted_lst)
