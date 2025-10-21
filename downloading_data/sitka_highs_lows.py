import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # if data is missing python will return a ValueError - this needs to be delt with using error handling

    # get dates, and high and low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], 'Y%-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
# getting x/y co ordinates for the fill_between() method
ax.plot(dates, highs, c='red', alpha=0.5) # alpha arguement controls transparency
ax.plot(dates, lows, c='blue',alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # this draws date labels diagonally so they do not overlap
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

"""    for index, column_header in enumerate(header_row): # the enumerate function returns both the index of each item and the value
        print(index, column_header) # this loop prints each header and its position in the list """

print(highs)
