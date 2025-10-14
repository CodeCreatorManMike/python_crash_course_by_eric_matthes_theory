import matplotlib.pyplot as plt

#use a for loop to calculate data automatically
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # list comprehension which squares each number in x values

"""x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]"""

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
"""ax.scatter(x_values, y_values, c='red' s=10) # we use a smaller point size
# to plot a series of points we pass scatter both x/y values
# to change the color of points pass c to scatter(), and the name of the color you wish to use
# or you could use RGB by passing in a tuple of 3 values 'c=(0,0.8,0)
"""

# a color map is a gradient for displaying colors built into matplotlib
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) 
# we pass a list of y-values to c, then specify which color map to use

# set chart title and label axes

ax.set_title("Square Numbers", fontsize=24) # sets the title of the graph
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square Of Value", fontsize=14)
# xlabel/ylabel allow you to set labels for each axes

ax.axis([0, 1100, 0, 1100000]) # because this is a larger data set we use the axis() method
# it requires 4 values, the minimum/maximum for x/y axis

plt.show() # the show() method opens pyplot viewer and displays the plot

"""
If you want to save a plot to a file automatically:
plt.savefig('squares_plot.png', bbox_inches='tight')

First arguement is a filename and the plot image
The second arguement trims extra whitespace from the plot/omit this if you want extra white space around the chart
"""
