# Data Types

# String
print('Hello'[0])   #it'll print 'H'.
print('Hello'[-1])  #but here it'll print an 'o'.
print('Hello'[-2])  #and here an 'l'

# Number
print(123_453_567)

# ***
# num_char = len(input("What is your name?"))
# # converting num_char into a string
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")
# # to know which type of variable do we have
# print(type(num_char))

a = str(123)
print(type(a))
print(70 + float('100.5'))


# ***
two_digit_num = input("Type a two digit numbers: ")
first_digit = two_digit_num[0]
second_digit = two_digit_num[1]
print(int(first_digit) + int(second_digit))



# Exercise 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
result = int(weight) / float(height)**2
print(int(result))

# Rounding result
print(round(8 / 3, 2))  # here 2 after 3 is a specification of number after comma we want to output
                        # (round to two decimal places
print(8 // 3)  #here is a floor division. It chops all decimal places from the whole number


# Life in weeks
age = input("What is your current age? ")

age_left = 90 - int(age)
print(f"You have {int(age_left) * 365} days, {int(age_left) * 52} weeks, and {int(age_left) * 12} months left.")

