# Loops and Random Number

# FOR LOOPS
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(-5, 5):
    print(i)

for i in range(5, 15, 3): # (start, stop, step)
    print(i)

# Random Numbers
import random

# random integers
print(random.randrange(10))
print(random.randrange(5, 16)) # 5 to 15
print(random.randrange(-5, 5))
print(random.randrange(5, 15, 3))
print(random.randrange(10, - 10, -2))

# random floats
print(random.random()) # random float from 0 to 1
print(random.random() * 10 + 5) # random float from 5 to 15

# BREAK
# immediately edits or breaks out of the current loop
# keep rolling a die until you get a six
for i in range(100):
    roll  = random.randrange(1, 7)
    print("You rolled a", roll, "on roll number", i)
    if roll == 6:
        break

# CONTINUE
# skips the rest of the current iteration
for i in range(10):
    roll = random.randrange(1, 7)
    if roll % 2:
        continue
    print(roll)

# FOR ELSE
# if you make it all the way through the for loop without breaking,
# then you do the else statement

for i in range(10):
    n = random.randrange(10)
    print(n)
    if n == 0:
        break
else:
    print("Did not roll a zero.")
