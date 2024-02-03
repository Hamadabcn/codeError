import math # import the math module

# A function to calculate the average of a list of numbers
def average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

# A function to calculate the standard deviation of a list of numbers
def standard_deviation(lst):
    mean = average(lst)
    variance = 0
    for num in lst:
        variance += (num - mean) ** 2
    variance /= len(lst)  # Divide the variance by the length of the list
    std_deviation = math.sqrt(variance)  # Calculate the square root of the variance
    return std_deviation

# Test the functions
lst = [1, 2, 3, 4, 5]
print(average(lst))
print(standard_deviation(lst))
