# Plotting and comma separated variable
import csv
import matplotlib.pyplot as plt

with open("data/Libraries_-_2017_Computer_Sessions_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

names = [x[0] for x in data] # grabbing list of library names
names = names[1:] # chop off the header
print(names) # prints library names (alphabetical)

ytd = [x[-1] for x in data] [1:] # grabbing list of year to date values
ytd = [int(x) for x in ytd]
print(ytd) # prints year to date values

library_number = [x for x in range(len(names))]
print(library_number)

# We want to plot computer users YTD vs. library

plt.figure(1, figsize=(12, 8), tight_layout=True)
plt.bar(library_number, ytd)
plt.title("Chicago Library Branch Computer Usage - 2017")
plt.ylabel("Computer Users")

plt.xticks(library_number, names, rotation=90, fontsize=6) # plotted data, text to plot

plt.show()