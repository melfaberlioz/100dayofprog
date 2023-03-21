year = int(input("which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'The {year} is leap year.')
        else:
            print(f'The {year} is not leap year.')
    else:
        print(f'The {year} is not leap year.')
else:
    print(f'The {year} is not leap year.')