from gmplot import *
import csv

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"

mymap = GoogleMapPlotter(41.923127, -87.638219, 12, apikey=apikey)

mymap.marker(41.923127, -87.638219)

mymap.circle(41.933127, -87.638219, 500, "#FF0000", ew=10)

lats = [41.923127 for x in range(10)]
longs = [-87.638219 - x/100 for x in range(10)]
lats[4] = 41.933127

mymap.plot(lats, longs, "blue")

mymap.polygon(lats, longs, "red") # lats, longs, color, face color(fc), edge color (ec)

with open("/Users/simoneturner/Downloads/Parks_-_Public_Art.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data.pop(0))

lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]

mymap.scatter(lats, longs, color="green", marker=True, size=1, opacity=1)

'''
for i in range(len(lats)):
    mymap.circle(lats[i], longs[i], i)
'''

mymap.heatmap(lats, longs, maxIntensity=5, radius=50, dissipating=True)

mymap.draw("mymap.html")