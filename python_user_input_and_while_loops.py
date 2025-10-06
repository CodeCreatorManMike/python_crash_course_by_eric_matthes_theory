#7.1
rental_car_preferance = input('what kind of rental car would you like? ')
print(f'let me check if we have a {rental_car_preferance}.')

#7.2
number_of_people_at_dinner = int(input("How many people are in your dinner group? "))

if number_of_people_at_dinner > 8:
    print(f"youll have to wait for a table for {number_of_people_at_dinner} guests to be available")
else:
    print(f"your table for {number_of_people_at_dinner} guests is ready")


#7.3
is_this_a_multiple_of_ten = int(input('Give me a number? '))

if is_this_a_multiple_of_ten % 10 == 0:
    print(f'{is_this_a_multiple_of_ten} is a multiple of ten')
else:
    print(f'{is_this_a_multiple_of_ten} is not a multiple of ten')


#7.4
flag = True

while flag == True:
    pizza_toppings = []
    new_pizza_toppings = input('\nwhat toppings would you like on your pizza? Enter "exit" when your order is complete: ')
    pizza_toppings.append(new_pizza_toppings)
    if new_pizza_toppings == 'exit':
        print(pizza_toppings)
        flag = False
        break

#7.5
age = int(input('How old are you? '))

if age < 3:
    print('\nYour ticket is free')
elif age > 3 and age < 12:
    print('\nYour ticket is $10')
elif age > 12: 
    print('\nYour ticket is $15')


#7.8 // 7.9
sandwich_orders = ['BLT', 'american', 'ham and cheese', 'pastrami', 'chicken and mayo', 'pastrami', 'salami', 'pastrami']
finished_orders = []

print('\nThe deli has run out of pastrami sandwiches')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:

    print(f'\nyour {sandwich} is complete.')
    finished_orders.append(sandwich)

print(f'\n{finished_orders}')


#7.10
flag = True
locations_list = []

while flag:
    dream_vacation = input('\nIf you could travel to anywhere in the world, where would you go? ')
    locations_list.append(dream_vacation)  # always save the entry 

    continue_asking = input('\nWould you like to make another submission? Y/N ')
    if continue_asking.upper() == 'N':
        flag = False

print(f'\nHere are the dream vacation submissions: {locations_list}')

