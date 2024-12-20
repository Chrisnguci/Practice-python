# Lession
'''import math


# 1. Importing module
# using Pi
print(math.pi*5**2)

# using fsum (floating point numbers)
# using sum 
numbers = [0.1, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(sum(numbers))  # 0.9999999999999999
 # -> might be crash

# using fsum
numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(math.fsum(numbers))

# 2. Importing specific things from modules
# tedious : chan ngat
# just use pi
from math import pi, tau
print(globals())


# 3. Alias imports
import numpy as np

#4 Import using *
# -> Import everything
# -> don't use it'''


# Excercise
# ex 1
from fractions import Fraction

f = Fraction(2.5)
print(f)

# Ex2
import math
numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]

fsum = math.fsum(numbers)
print(fsum)

# Ex3 :
import random as rd

r_number = rd.randint(1,100)
print(r_number)

#4
