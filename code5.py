# A function to print the multiplication table of a given number
def multiplication_table(n):
    for i in range(1, 11):
        # print(n, "x", i, "=", n * i)
         print(f"{n} x {i} = {n * i}")  # the correct way of putting it

# Test the function
multiplication_table(5)
