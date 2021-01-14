import folium #  to visualize data that’s been manipulated in Python on an interactive leaflet map.
import pandas #  so we can use our csv file

data = pandas.read_csv("Volcanoes.csv") #  Loads the csv containing details of the volcanoes
lat = list(data["LAT"]) #  pulls the Latitude from the data variable as a list
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation): #  function to color markers based on volcanoes elevation
    if elevation < 1000:
        return 'green'
    elif elevation <= 1000 or elevation <= 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain") #  Builds the maps starting location to view

fg = folium.FeatureGroup(name="My Map") #  create a variable to call multiple features(volcanoes) later

for lt, ln, el, nm in zip(lat, lon, elev, name): #  zip used to call data from multiple lists in the for loop
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=f"Elevation = {el}m\n Name = {nm}",
    fill_color=color_producer(el), color = 'grey', fill = True, fill_opacity=0.7)) #  shows location of volcanoes with styling

map.add_child(fg) #  every time the for loop runs, add location to map

map.save("Map1.html") #  save to a html page