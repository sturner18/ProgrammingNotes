'''
Function and Module Notes
v1.0
by Simone Turner
'''

from random import * # random - star is the wild car(it means all)
#from math import *
from  math import pi
import my_module

# When you use the keyword from, you are importing directly into your file (no need to use random.randrange, just random)

# Functions and Modules
print(randrange(900, 1000))

if __name__ == "__main__":
    '''
    This code only runs if this is the executed code/file.
    '''
    print(randrange(100))
    print(random())
    print(pi)

    e = 5
    print(e)
    print("This is my period", my_module.period)
    my_module.hello("Simone")
    product, sum = my_module.product_sum(10, 20)
    print(product, sum)

    print(3, 4, sep = ",", end = "")
    print(5, 6)
    my_module.hello(name = "Francis")
    my_module.hello()