fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list 
# comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]


# Exercise 2 - create a variable named capitalized_fruits and use list 
# comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', 
# etc...]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
## you can also use .title because of mandarin orange


# Exercise 3 - Use a list comprehension to make a variable named 
# fruits_with_more_than_two_vowels. Hint: You'll need a way to check if 
# something is a vowel.

fruits_with_more_than_two_vowels = [for fruit in fruits if count_vowels(fruit) > 2]
len[letter for letter in fruit1 if letter in 'aeiou']
fruits_with_more_than_two_vowels = fruit for fruit in fruits if len(letter for letter in fruit if letter in 'aeiou')


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The 
# result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [for fruit in fruits count_vowels(fruit) == 2]
fruit for fruit in fruits if len([letter for letter in fruit if letter in 'aeiou'])

# Exercise 5 - make a list that contains each fruit with more than 5 characters

fruit = [fruit for fruits in fruits if len(fruit) > 5]


# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruit = [fruit for fruits in fruits if len(fruit) == 5]


# Exercise 7 - Make a list that contains fruits that have less than 5 characters

fruit = [fruit for fruit in fruits if len(fruit) < 5]


# Exercise 8 - Make a list containing the number of characters in each 
# fruit. Output would be [5, 4, 10, etc... ]

fruit = [len(fruit) for fruit in fruits]


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a 
# list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]


# Exercise 10 - Make a variable named even_numbers that holds only the 
# even numbers 

even_numbers = [num for num in numbers if num % 2 == 0]


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [num for num in numbers if num % 2 != 0]


# Exercise 12 - Make a variable named positive_numbers that holds only the 
# positive numbers

positive_numbers = [num for num in numbers if num > 0]


# Exercise 13 - Make a variable named negative_numbers that holds only 
# the negative numbers

negative_numbers = [num for num in numbers if num < 0]

# Exercise 14 - use a list comprehension w/ a conditional in order to 
# produce a list of numbers with 2 or more numerals

numbers_with_two_or_more_numerals = [n for n in numbers if n >= 10 or n <= -10]


# Exercise 15 - Make a variable named numbers_squared that contains the 
# numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = [num ** 2 for num in numbers]


# Exercise 16 - Make a variable named odd_negative_numbers that contains 
# only the numbers that are both odd and negative.

odd_negative_numbers = [num for num in numbers if (num < 0 and num % 2 == 1]


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list 
# containing each number plus five. 

numbers_plus_5 = [num + 5 for num in numbers]


# BONUS Make a variable named "primes" that is a list containing the 
# prime numbers in the numbers list. *Hint* you may want to make or find 
# a helper function that determines if a given number is prime or not.

