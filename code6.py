# A function to convert a temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f

# A function to convert a temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9
    return c

# Test the functions
print(celsius_to_fahrenheit(0))
print(fahrenheit_to_celsius(32))
