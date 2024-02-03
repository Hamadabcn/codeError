# A function to reverse a string
def reverse_string(s):
    reversed_s = s[::-1]
    return reversed_s

# A function to check if two strings are anagrams
def is_anagram(s1, s2):
    s1 = ''.join(e for e in s1 if e.isalnum()).lower()
    s2 = ''.join(e for e in s2 if e.isalnum()).lower()
    return sorted(s1) == sorted(s2)

# Test the functions
print(reverse_string("hello"))
print(is_anagram("listen", "silent"))
