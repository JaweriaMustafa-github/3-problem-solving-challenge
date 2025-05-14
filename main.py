#Problem 1
#Reverse a String 
#Write a function that takes a string as input and returns the reversed string.
def reverse_string(s):
    return s[::-1]
#The [::-1] slice reverses the string efficiently.

# Example
print(reverse_string("hello"))  # Output: "olleh"


#Problem 2
#Count Vowels in a String
# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive). 
def count_vowels(s):
    vowels = set("aeiou")
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
#.lower() Converts the string to lowercase and checks each character against a set of vowels.
# Example
print(count_vowels("Apple"))  # Output: 2


#Problem 3:
# Sum of Digits
#Write a function that takes a non-negative integer and returns the sum of its digits.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example
print(sum_of_digits(1234))  # Output: 10
