#  1.  Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number or the string 2, 
# False otherwise.

def is_two(n):
    if n == 2 or n == '2':
        return True
    else:
        return False
print(is_two(10))


# 2.  Define a function named is_vowel. It should return True if the 
# passed string is a vowel, False otherwise.

def is_vowel(vow):
    if vow in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


# 3.  Define a function named is_consonant. It should return True if the 
# passed string is a consonant, False otherwise. Use your is_vowel 
# function to accomplish this.

def is_consonant(c):
    if c in is_vowel:
        return False
    else: 
        return True


# 4.  Define a function that accepts a string that is a word. The function 
# should capitalize the first letter of the word if the word starts with 
# a consonant.

def any_word(value):
    if value[0] not in 'aeiouAEIOU':
        return value.capitalize()
print(any_word('cat'))  


# 5. Define a function named calculate_tip. It should accept a tip 
# percentage (a number between 0 and 1) and the bill total, and return 
# the amount to tip.

def calculate_tip(tip, total_bill):
    return tip * total_bill
calculate_tip(.25, 99)


# 6. Define a function named apply_discount. It should accept a original 
# price, and a discount percentage, and return the price after the 
# discount is applied.

def apply_discount(org_price, disc_perct):
    return org_price - (org_price * disc_perct) 
apply_discount(200, .25)    


# 7. Define a function named handle_commas. It should accept a string that 
# is a number that contains commas in it as input, and return a number as 
# output.

def handle_commas(n):
    num = n.replace(',', '')
    return int(num)
print(handle_commas('9,000,097'))


# 8. Define a function named get_letter_grade. It should accept a number 
# and return the letter grade associated with that number (A-F).

def get_letter_grade(num_grade):
    if num_grade <= 100:
        letter_grade = 'A'
    if num_grade <= 90:
        letter_grade = 'B'
    if num_grade <= 80:
        letter_grade = 'C'
    if num_grade <= 70:
        letter_grade = 'D'
    if num_grade <= 60:
        letter_grade = 'F'
    return letter_grade
print(get_letter_grade(88))


# 9. Define a function named remove_vowels that accepts a string and 
# returns a string with all the vowels removed.

def remove_vowel(n):
    vowel = 'aeiouAEIOU'
    for value in n:
        if value in vowel:
            n = n.replace(value,'')
    return n
print(remove_vowel('castle'))




# 10. Define a function named normalize_name. It should accept a string 
# and return a valid python identifier, that is:

def normalize_name(string_in):
    string_out = ''
    for char in string_in:
        if char.isalpha() or char == ' ':
            string_out += char
    string_out = string_out.strip()
    string_out = string_out.replace(' ', '_')
    string_out = string_out.lower()
    return string_out
print(normalize_name(' 458  HeLlo AlEx $#8$95'))