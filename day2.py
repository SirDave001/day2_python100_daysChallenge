print('Welcome to the tip calculator.')
bill = float(input('What is the total bill? $'))
tip = int(input('What percentage of tip would you like to give? '))
people = int(input('How many people to split the bill? '))
total_bill = (tip / 100 * bill) + bill
split_bill = total_bill / people
final_bill = round(split_bill, 2)
print(f'Each person should pay ${final_bill}.')