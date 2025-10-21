#Python Excersises: If Statements

#5.1 - i aint writing out ten different conditional tests
car = 'audi'
print("Is car == 'audi'? I predict True.")
print(car == 'audi')

print("\nIs car == 'sabaru'? I predict False.")
print(car == 'sabaru')

#5.2
car = 'BMW'
print("\nIs car == 'BMW'? i predict true")
print(car.lower() == 'bmw')

car = 'bmw'
print("\nIs car == 'BMW'? i predict true")
print(car.upper() == 'BMW')
correct_number = 10

while True:
    answer = input("Would you like to play? ")
    
    if answer.lower() != "yes":
        break   

    print("Great! Let's start.")
    player_guess = int(input("\nPick a number from 1 to one hundred? "))

    if player_guess == correct_number:
        print("Congratulations! You guessed the number correctly")
        break   
    else:
        print("WRONG!!")


print("Thanks for playing (or not)!")


#testing if an item is in a list
list = ['item 1', 'item 2']
'item 1' in list # returns True
'item 6' in list # returns False

#testing if item is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title}, you can post a response if you wish.")


#5.3
alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!')

alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points!')

#5.4 // 5.5
alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points')
elif alien_color == 'yellow':
    print('You just earned 10 points')
else:
    print('You just earned 15 points')

#5.6
person_age = int('35')

if person_age < 2:
    print('You are a baby')
elif 2 <= person_age < 4:
    print('You are a toddler')
elif 4 <= person_age < 13:
    print('You are a kid')
elif 13 <= person_age < 20:
    print('You are a teenager')
elif 20 <= person_age < 65:
    print('You are an adult')
else:
    print('You are an elder')

#5.7 - I aint doing all of em
favourite_fruits = ['apple', 'orange', 'strawberry']

if 'apple' in favourite_fruits:
    print('You like apples')

#5.8
user_names = ['admin', 'michael', 'jordan']

if not user_names:
    print('We need to find some users')

user_name = input('What is your user name?')

# check if the name is already in the list
if user_name not in user_names:
    user_names.append(user_name)
    print(f"{user_name} added successfully.")
else:
    print(f"{user_name} already exists in the system.")

if not user_names:
    print('We need to find some users')

# special message for admin
if user_name == 'admin':
    print('Hello Admin, what would you like to mess with today?')
else:
    print(f"Hello {user_name}, welcome back!")


#5.10
current_users = ['admin', 'michael', 'jordan', 'james', 'luke']
new_users = ['michael', 'jordan', 'jackson', 'john']

for new_user in new_users: # this loops through new users list
    if new_user in current_users: # this checks the new user against the current user list
        print(f'User "{new_user}" already exists')
    else:
        current_users.append(new_user)
        print(f'User "{new_user}" added successfully')

print("\nUpdated users list:", current_users)

#5.11
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

for number in numbers:
    if number == '1':
        print(f'{number}st')
    elif number == '2':
        print(f'{number}nd')
    elif number == '3':
        print(f'{number}rd')
    else:
        print(f'{number}th')
