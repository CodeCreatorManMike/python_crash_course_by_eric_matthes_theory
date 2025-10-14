# a random walk is a set of data based on randomness
# we use a class to mimic this real world situation
# the class needs 3 attributes (one variable for number of points in the walk)
# and then two lists to store the x and y co ordicnate values of each point in the walk

from random import choice

class RandomWalk:
    """a class to generate random walks"""

    def __init__(self, num_points=5000):
        """initialize attributes of a walk"""
        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

# to make random choices, we will store possible moves in a list
# we will use the fill_walk() method to fill the walk with points

    def fill_walk(self):
        """calculate all the points in a walk"""

        #keep taking steps until the qalk is completed
        while len(self.x_values) < self.num_points:

            # decide which direction to go on how far to go in a direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # rejects moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            
            