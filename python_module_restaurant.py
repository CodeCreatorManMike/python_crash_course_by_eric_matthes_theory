# module for restraunt class
class Restaurant:
    """Make a class that replicates a restaurant"""

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