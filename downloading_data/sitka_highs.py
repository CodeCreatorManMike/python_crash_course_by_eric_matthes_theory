import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.xlsx'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # next() is a built in csv function which returns information from the next line when passed a reader object
    # we only call the next() function once to only return the header of the csv

    # get the dates and high temperatures from this title
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') # we convert the dates (string) to a datetime object and append it to dates
        high = int(row[5]) # loop through column 5 and extract each int for max temp
        dates.append(current_date)
        highs.append(high)

    # plot the high temperatures 
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red') # we append the dates and high temp values ot plot()

    # format plot
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # this draws date labels diagonally so they do not overlap
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

"""    for index, column_header in enumerate(header_row): # the enumerate function returns both the index of each item and the value
        print(index, column_header) # this loop prints each header and its position in the list """

print(highs)
