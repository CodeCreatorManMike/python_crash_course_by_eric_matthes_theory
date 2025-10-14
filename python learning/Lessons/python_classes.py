import python_module_restaurant
import random
# 9.1 & 9.4
"""class Restaurant:
    # Make a class that replicates a restaurant

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"\nWelcome to {self.restaurant_name}, we make {self.cuisine_type} style food.")

    def restaurant_open(self):
        print("\nWe are open all week from 9AM to 10PM")
        print("\nWe are now open. Welcome!")

    def set_number_served(self):
        self.number_served = int(input('How many customers have been served today? '))

    def increment_number_served(self):
        more_served = int(input('How many more customers have you served? '))
        self.number_served += more_served


# create an instance of that class
Italiano = Restaurant("Papa Mike's", 'Italian')

# individually print the attributes
print(f"Restaurant name: {Italiano.restaurant_name}")
print(f"Cuisine type: {Italiano.cuisine_type}")
print(f"Number served: {Italiano.number_served}")

Italiano.increment_number_served()
print(f"Number served: {Italiano.number_served}")


# call both methods
Italiano.describe_restaurant()
Italiano.restaurant_open()

# 9.2
Chinese = Restaurant("Won-Ton", 'Chinese')
Thai = Restaurant("Thai Ting", 'Thai')
American = Restaurant("Fat Joe Burgers", 'American')

Chinese.describe_restaurant()
Thai.describe_restaurant()
Italiano.describe_restaurant()"""

# 9.3 & 9.5
class User:
    def __init__(self, first_name, last_name, age, interests, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.interests = interests
        self.login_attempts = login_attempts

    def describe_users(self):  
        print(
            f"\nHello {self.first_name} {self.last_name}. As a {self.age} year old, it is impressive you like {self.interests}."
        )

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0 

Me = User('Michael', 'Jones', 'Nineteen', 'coding', 0)
Me.describe_users()
Me.increment_login_attempts()
Me.increment_login_attempts()
print(f'\n{Me.login_attempts}')
Me.reset_login_attempts()
print(f'\n{Me.login_attempts}')

# 9.6
"""class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = flavors

    def display_flavors(self):
        flavors = ['choc chip', 'birthday cake', 'vanilla', 'chocolate', 'strawberry']

        for flavor in flavors:
            print(f"\nWe have {flavor} in stock")


franks_flavors = IceCreamStand('franks flavors', 'ice cream', ['choc chip', 'birthday cake', 'vanilla', 'chocolate', 'strawberry'])
franks_flavors.display_flavors()"""

# 9,7
class Admin(User):
    def __init__(self, first_name, last_name, age, interests, login_attempts, privileges):
        super().__init__(first_name, last_name, age, interests, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        print(f"\nAdmin's have these privileges: {self.privileges}")

main_admin = Admin('Michael', 'Jones', '19', 'programming', 0, ["can add post", "can delete post", "can ban user"])
main_admin.show_privileges()

# 9.9 - too easy
# 9.10
my_restaurant = python_module_restaurant.Restaurant("Mike's", "New Yorken", number_served=100)
my_restaurant.describe_restaurant()

# 9.11 9.12 - have to make so many files to repeat 9.10 just cause its working with multiple modules


# 9.13
class Dice:
    # storing default value of sides
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        landed_value = random.randint(1, self.sides)
        return landed_value  

my_die = Dice()

print("\nYou rolled", my_die.roll_die())

for i in range(10):
    print("\nRoll", i+1, ":", my_die.roll_die())

# 9.14
lottery_number = [1, 7, 8, 3, 4, 5, 2, 1, 8, 2,
                  'D', 'E', 'A', 'E', 'X']

# random.sample(list, number of random selection from list)
winning_ticket = random.sample(lottery_number, 4)
print("\nWinning ticket is: ", winning_ticket)

# 9.14
my_ticket = [7, 5, 'A', 'X']

attempts = 0 

while True:
    attempts += 1
    draw = random.sample(lottery_number, 4)

    if draw == my_ticket:
        print(f"Winning ticket {draw} found after {attempts} tries!")
        break