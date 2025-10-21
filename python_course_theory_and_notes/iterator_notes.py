# iterator notes

# define a list
my_list = [1, 4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element from that list
print(next(iterator)) # prints 1

# get the next item from that list
print(next(iterator))