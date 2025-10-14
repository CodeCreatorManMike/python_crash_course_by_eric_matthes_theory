import matplotlib.pyplot as plt # plt acts an alias in this example
# plt; this is a common convention to avoid repeatedly writing pyplot

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # this list holds the data we will plot

plt.style.use('seaborn-v0_8') # prebuilt pyplot style

fig, ax = plt.subplots() #sub.plots() is another common convention
# this convention can generate one or more plots in the same figure
# fig; (variable) represents the entire figure or collection of plots
# the variable ax, represents a single plot in the figure

ax.plot(input_values, squares, linewidth=3) # the plot method plots the data we want on our graph
# line width argument sets the width of the line on the graph
# plot() assumes your first value corrosponds to a value of 0 (ours doesnt)
# we can overwrite the default behaviour by giving plot() an input and output value

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24) # sets the title of the graph
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square Of Value", fontsize=14)
# xlabel/ylabel allow you to set labels for each axes

ax.tick_params(axis='both', labelsize=14) # styles the tick marks

plt.show() # the show() method opens pyplot viewer and displays the plot

