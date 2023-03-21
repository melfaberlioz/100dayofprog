height = int(input("Enter your height:"))
bill = 0

if height >= 120:
    print("You can ride!")
    age = int(input("Enter your age:"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print('Please pay $12')

    wants_photo = input('Do you want a photo taken? Y or N?')
    if wants_photo == 'Y':
        bill += 3
    print(f'Your final bill is {bill}.')
else:
    print('Sorry you can\'t ride')