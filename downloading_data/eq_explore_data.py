from pathlib import Path
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# explore the structure of the data
filename = r"C:\Users\MJones\OneDrive - VIADEX\Desktop\python\python_learning\downloading_data\data\eq_data_30_day_m1.json"
# point to the JSON file

# --- open and load the JSON file ---
with open(filename) as f:
    all_eq_data = json.load(f)  # save loaded file content in a variable
    # .load() converts the data into a format which python can work with
    # extracting list of alll earthquakes

# --- inspect part of the data ---
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)


# map the earthquakes
# data = [Scattergeo(lon=lons, lat=lats)] - easier way of specifying data which doesnt allow for alot of customization
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text, 
    'marker': {
        'size': [5*mag for mag in mags], # this is an example of a list comprehension which runs a loop on magnitudes and returns the values
        'color': mags, # magnitude determines what color the markers are on the scale
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}},
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout} # defining the figures data and layout
offline.plot(fig, filename='global_earthquakes.html')

