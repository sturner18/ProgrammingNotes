# SEARCHING (Chapter 15 from programming arcade games)

file = open('data/villains.txt', 'r') # open file to read (creates object named file)
print(file)

for line in file:
    print(line.strip()) # .strip() method removes spaces and \t \r from beginning and end

for line in file:
    print("Hello", line.strip())
    # can't go through twice because it read through the document and is
    # now at the bottom, need to reset if you want to print again

file.close()

'''
# you can also open a file to write (overwrites all previous)
file = open('data/villains.txt', 'w')
# file.write("Lee The Merciless")
'''

# open a file to append (adds on to bottom of the file)
# file = open("data/villains.txt", "a")
# file.write("Lee The Merciless\n")

# file.close()

# Read the file into an array (list)
file = open("data/villains.txt", "r")
villains = []

for line in file:
    villains.append(line.strip())

print(villains)

# Linear Search
key = "The Vindictive Fury" # what we are searching for
i = 0 # index for the loop

while i < len(villains) - 1 and key != villains[i]:
    i += 1

if i < len(villains):
    print("Found", key, "at position", i)
