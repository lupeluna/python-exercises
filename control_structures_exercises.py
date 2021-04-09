# 1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day 
# is Monday or not.  

day_of_week = input('What day is it:')

day_of week 

if day_of_week = input('What day is it')
    if day == 'Monday':
        print('weekday')
    else:
        print('weekend')

# b. prompt the user for a day of the week, print out whether the day is a 
# weekday or a weekend


if day_of_week.lower().startswith('s'):
    print('weekend')
else:
    print('weekday')

# c. create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

hours_worked = 45
hourly_rate = 10

if hours_worked <= 40:
    weekly_pay = hours_worked * hourly_rate
else:
    weekly_pay = (40 * hourly_rate) + ((hours_worked - 40) * (1.5 * hourly_rate))
        
print(weekly_pay)


# 2. While

i = 5

while i <= 15:
    print(i)
    i += 1


i = 0
while i <= 100:
    print(i)
    i += 2


i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i <= 1000000:
    print(i)
    i **= 2

i = 100
while i <= 5:
    print(i)
    i += -5


# 2b. For Loops

num = int(input("Please input a positive integer"))

for n in range(1, 11):
    print(f'{num} x {n} = {num * n}')


for n in range(1,10):
    print(str(n) * n) 


#  2c. Prompt the user for an odd number between 1 and 50. Use a loop 
# and a break statement to continue prompting the user if they enter 
# invalid input. (Hint: use the isdigit method on strings to determine 
# this). Use a loop and the continue statement to output all the odd 
# numbers between 1 and 50, except for the number the user entered


while True:
    num = input("Please insert an odd number between 1 and 50:")
    if num.isdigit():
        if int(num) % 2 == 1 and int(int(num) >= 50)):
            break



## The input function can be used to prompt for input and use that input 
# in your python code. Prompt the user to enter a positive number and 
# write a loop that counts from 0 to that number. (Hints: first make sure 
# that the value the user entered is a valid number, also note that the 
# input function returns a string, so you'll need to convert this to a 
# numeric type.)

while True:
    num = input('Please in sert a positive integer:')
    if num.isdigit():
        if int(num) > 0:
            break
num = int(num)
for num in range(0, num +1):

    print(num)




## Write a program that prompts the user for a positive integer. Next 
# write a loop that prints out the numbers from the number the user 
# entered down to 1.

while True:
    num = input('Please in sert a positive integer:')
    if num.isdigit():
        if int(num) > 0:
            break
num = int(num)
for num in range(0, num +1):

    print(num)


##3.  Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".


for i in range(1, 101):
    if % 3 == 0 and I % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
print(i)


## 4. Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

while True:
    posited_num = input('Please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
proceed = input('Do you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number | squared | cubed')
    print('------' | '-------' | '--------')
    for i in range(1, posited_num + 1):
        i_squared - i ** 2
        i_cubed = i ** 3
        print(f{i:6})



