# this is used to incert the data from external file to code
import pandas 
# it helps us to get a map web view
import folium

# assign the file to a variable
data = pandas.read_csv("Volcanoes.txt")
# getting the lat, lon & popup data as list
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# creating the function
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.89],zoom_start=5, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
# looping the map to get all the data
for lt, ln, el in zip(lat, lon, elev):
# folium.Marker for normal map spot "icon=folium.Icon(color=color_producer(el)""
# folium.CircleMarker for circle also we use radius color opacity
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" mukilan", 
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

# json added to a variable and Note:- the recent version of folium needs a string insted of
# file data input. Therfore you need to add utf.read() method
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


# LayerControl for Volcanoes
map.add_child(fgv)
# LayerControl for Population
map.add_child(fgp)
# LayerControl is a empty map
map.add_child(folium.LayerControl())


# finaly if we save the file and run html will generat auto
map.save("Map1.html")

# Note: You may get a blank webpage if there are quotes(') 
# in the strings. To avoid that change the pupup argumentto:
#     popup=folium.Popup(str(el),parse_html=True)
# However, for simple strings like elevation values this is not
# a problem since there are no quotes in them.