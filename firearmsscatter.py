import csv
import matplotlib.pyplot as plt
import numpy as np

with open("Data/World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

print(data)
headers = data.pop(0)
print(headers)

# plot homicides by firearm per 100k vs Firearms per 100
homicides_per100k = []
firearms_per100 = []
countries_to_plot = ["United States", "France", "Canada", "Germany", "England and Wales", "Ireland", "Sweden", "Switzerland", "Norway", "Denmark", "Netherlands", "Spain", "Japan", "South Korea", "Australia", "Russia", "China", "Israel"]
country_names = []

for i in range(len(data)):
    if data[i][0] in countries_to_plot:
        try:
            homicide = float(data[i][5])
            firearm = float(data[i][7])
            homicides_per100k.append(homicide)
            firearms_per100.append(firearm)
            country_names.append(data[i][0])
        except:
            print(data[i][0], "has no data.")

plt.figure(1, figsize=(12, 7))
plt.scatter(firearms_per100, homicides_per100k, s=10, c='red')
plt.title("World Homicide Rates vs Firearm Ownership")
plt.xlabel("Firearms per 100 People")
plt.ylabel("Homicides by Firearm per 100k Population")

# make a best fit
m, b = np.polyfit(firearms_per100, homicides_per100k, 1) # 1 for linear, returns slope and y intercept

x = [0, 100]
y = [m * point + b for point in x]
plt.plot(x, y, color='green')

for i in range(len(country_names)):
    plt.annotate(country_names[i], xy=(firearms_per100[i], homicides_per100k[i])) # text, xy =()

plt.show()