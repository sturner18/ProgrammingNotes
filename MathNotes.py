# MATHgfg

# floats vs ints

my_int = 1
my_float = my_int / 2
print(my_int, my_float)

print(my_float + 1.2)

print(1.2 / 2 + 1.2)

# VARIABLES
# Naming

snake_case = "Lower case with under scores between words."
camelCase = "New words are capitalized."

# The following is not allowed:
# my variable  # spaces not allowed
# my_variable! # no special characters
# my.variable  # no decimals
# 8ball        # no numbers to start variable name
# ball8        # is allowed

# Assignment Operator - Equal sign
# The ONLY way to change a variable (sort of)
x = 5
x + 1
print(x)

x = x + 1
print(x)

# Math operators
# + - * /
# ** exponent
# // floor division, rounds down
print(3.8 // 2)
print(3.8 / 2)

# % modulo, remainder after division
print(7 % 2)
print(11 % 7)

# Compound Assignment Operators
# += -= *= /=
y = 1
y += 1
print(y)

y *= 3

y **= 2
print(y)

# Round Function
x = 1234.5678
print(round(x, 2))
print(round(x, -2))

# Format Function "{}".format()
# for formatting text
# Position:PlaceholderJustificationWidthDecorationsType

# Lets format some text
first = "Jerry"
last = "Garcia"

invite_list = [["Abe", "Anderson"], ["Bev", "Beverly"], ["Cam", "Carter"]]

for person in invite_list:
    print("{} {}, would like to come to the party.".format(person[0], person[1]))

# print the first name
print("{}".format(first))

# print first last
print("{} {}".format(first, last))

# print First: first Last: last
print("First: {} \t Last: {}".format(first, last))

# print last, first
print("{1}, {0}".format(first, last))

# Number formatting work similarly
# You may specify d for digit, f for float, e for exponent to force a format
# here are some common uses

# Round a float to a decimal place {:.3f} rounds to 3
pi = 3.1415926535897932348

print("{:.3f}".format(pi))

# add a sign to a number {:+}
# this works for positive and negative numbers (both use +)
print("{:+}".format(pi))

# add comma formatting to number {:,}
my_number = 1234567890
print("{:,}".format(my_number))

# right align :>x where x is the width of the text
print("{:>30}".format(pi))

# left align :<x
print("{:<30}".format(pi))

# center align :^x
print("{:^30}".format(pi))

# percent {:%} {:.2%}
print("{:.2%}".format(0.578))
