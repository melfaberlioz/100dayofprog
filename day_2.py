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
print(result)

