#Python Excersises: Lists
# 3.4
guests = ['Jordy', 'Michael Jackson', 'Mike Tyson']
print(guests)

# 3.5
cant_make_it = guests[-1]
print(f'Unfortunately {cant_make_it}, is unable to make it tonight')
guests.remove(guests[-1])

print(f'\nBut {guests} can make it!')

guests.append('Jean Dawson')
print(f'\n{guests} are the new guests for tonight')

for guest in guests:
    print(f'\nDear {guest}, you are invited to dinner tonight at my place.')

# 3.6
print('\nI just found a bigger dinner table!')
guests.insert(0, 'James')   # at the beginning
guests.insert(2, 'Jack')    # in the middle
guests.append('John')       # at the end


for guest in guests:
    print(f'\nYou are all welcome to my Dinner! cant wait to see you {guest}')

#3.7
print('\nUnfortunately the table wont arrive on time, i can only invite 2 people')

un_invited_guest_one = guests.pop()
print(f"I'm so sorry {un_invited_guest_one} but unfortunately you cannot come.")
un_invited_guest_two = guests.pop()
print(f"I'm so sorry {un_invited_guest_two} but unfortunately you cannot come.")
un_invited_guest_three = guests.pop()
print(f"I'm so sorry {un_invited_guest_three} but unfortunately you cannot come.")
un_invited_guest_four = guests.pop()
print(f"I'm so sorry {un_invited_guest_four} but unfortunately you cannot come.")

for guest in guests:
    print("{guests} you are still able to attend.")

del guests[0]
del guests[0]

print(f"{guests}")

#3.8
dream_locations = ['New York', 'London', 'Japan', 'Sweden', 'Spain']
print(f'{dream_locations}')
sorted_locations = sorted(dream_locations)
print(f'{sorted_locations}')
print(f'{dream_locations}')
print(f'{sorted_locations.reverse()}')

#3.9
print(len(guests))

#4.1
favourite_pizzas = ['pepperoni', 'salami', 'cheese']

for pizza in favourite_pizzas:
    print(f'I like {pizza}')

print('\nI only really eat Pepperoni, but I really like pizza!')

#4.2
#too easy innit

#4.3
for number in range(1, 21):
        print(number) #This will print the raising range from 1 to 20

#4.4//4.5
numbers_list = list(range(1, 1000001))
for number in numbers_list:
     print(min(numbers_list))
     print(max(numbers_list))
     break

#4.6
small_numbers_list = list(range(1, 21, 2)) #prints all of the odd numbers
for num in small_numbers_list:
    print(num) 
                
#4.7
three_numbers_list = list(range(3, 31, 3))
for num in three_numbers_list:
     print(num)


#4.8
pre_cube_number = list(range(1,11))
for num in pre_cube_number:
    cubed_number = num ** 3
    print(cubed_number)


#4.9
cubes = [value ** 3 for value in range(1,11)]
print(cubes)


#4.10
favourite_pizzas = ['pepperoni', 'salami', 'cheese']
favourite_pizzas.append('BBQ')
favourite_pizzas.append('Chicken')
favourite_pizzas.append('caramilized onions')
favourite_pizzas.append('double cheese')
print(favourite_pizzas)
print(favourite_pizzas[:3])
print(favourite_pizzas[2:5])
print(f"The last three pizzas are {favourite_pizzas[4:]}")

#4.11
friends_pizzas = ['pepperoni', 'salami', 'cheese', 'BBQ', 'Chicken', 'caramilized onions', 'double cheese']
friends_pizzas.append('american')
favourite_pizzas.append('BAF')
print('My favourite pizzas are: ')
for pizza in favourite_pizzas:
     print(pizza)

print('My friends favourite pizzas are: ')
for pizza in friends_pizzas:
     print(pizza)
