total_bill = float(input('Welcome to the tip calculator.\nWhat was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
split_bill_between = int(input('How may people to split the bill? '))

split_bill = ((((tip/100) * total_bill) + total_bill) / split_bill_between)

result = print(f'Each person should pay: ${round(split_bill, 2)}')
