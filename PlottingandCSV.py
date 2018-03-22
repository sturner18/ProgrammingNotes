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

plt.figure(1, figsize=(12, 8), tight_layout=True, facecolor="lightblue")
plt.bar(library_number, ytd, color='red')
plt.title("Chicago Library Branch Computer Usage - 2017")
plt.ylabel("Computer Users")

plt.xticks(library_number, names, rotation=90, fontsize=6) # plotted data, text to plot

# Make a line graph of computer users at three libraries by month

print(data)
month_names = data.pop(0)[1:-1]
print(month_names)

month_numbers = [x for x in range(12)]
print(month_numbers)

library_names = [x[0] for x in data]
print(library_names)

bwp_data = data[library_names.index('Bucktown-Wicker Park')] [1:-1]
# bwp_data.pop(0)
# bwp_data.pop()
bwp_data = [int(x) for x in bwp_data]
print(bwp_data)

lp_data = data[library_names.index('Lincoln Park')] [1:-1]
# lp_data.pop(0)
# lp_data.pop()
lp_data = [int(x) for x in lp_data]
print(lp_data)

hp_data = data[library_names.index('Humboldt Park')] [1:-1]
# hp_data.pop(0)
# hp_data.pop()
hp_data = [int(x) for x in hp_data]
print(hp_data)

plt.figure(2)

plt.plot(month_numbers, bwp_data)
plt.plot(month_numbers, lp_data)
plt.plot(month_numbers, hp_data)

plt.show()