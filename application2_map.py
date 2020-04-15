import folium
import pandas

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s Meters
"""
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    if 1000<=elevation<=3000:
        return 'red'
    else :
        return 'blue'

map = folium.Map(location = [35.709273, 139.906375], zoom_start = 6, title = 'Stamen Watercolor')

fgp = folium.FeatureGroup(name = "population")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000
 else'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
 else 'red' }))
# To add colors according to the population

volcanoes = pandas.read_csv('volcanoes.txt')
fgv = folium.FeatureGroup(name = "volcanoes")

for i in range(len(volcanoes)):
    iframe = folium.IFrame(html=html % (volcanoes.loc[i, 'NAME'], volcanoes.loc[i, 'NAME'], volcanoes.loc[i, 'ELEV']), width = 200, height = 100)
    fgv.add_child(folium.CircleMarker(location = [volcanoes.loc[i, 'LAT'], volcanoes.loc[i, 'LON']], fill = True, radius = 7, color = 'lightblue',  popup = folium.Popup(iframe), fill_color = color_producer(volcanoes.loc[i, 'ELEV']), fill_opacity = 0.7, tooltip = 'Click for information about this volcano'))
# To add markers and information about volcanoes.

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl()) # To turn features on and off
map.save("Map1.html")



