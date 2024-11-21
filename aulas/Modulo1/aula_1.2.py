# 1.2 Section 2 – Selected Python modules (math, random, platform)

# import math
#
# for name in dir(math):
#     print(name, end='\t')
# print()

# -------------------------------------------
# from math import pi, radians, degrees, sin, cos, tan, asin
#
# ad = 90
# ar = radians(ad)
# ad = degrees(ar)
#
# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)

# -------------------------------------------
# from math import e, exp, log
#
# print(pow(e, 1) == exp(log(e)))
# print(pow(2, 2) == exp(2 * log(2)))
# print(log(e, e) == exp(0))

# -------------------------------------------
# from math import ceil, floor, trunc
#
# x = 1.4
# y = 2.6
#
# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))

# -------------------------------------------
# 1.2.3 Is there real randomness in computers?

# from random import random
#
# for i in range(5):
#     print(int(random() * 10 + 1))

# -------------------------------------------
# from random import random, seed
#
# seed(0) # The values are always the same
# # 0.8444218515250481
# # 0.7579544029403025
# # 0.420571580830845
# # 0.25891675029296335
# # 0.5112747213686085
#
# for i in range(5):
#     print(random())

# -------------------------------------------
# from random import randint
#
# for i in range(10):
#     print(randint(1, 10), end=',')
# print()

# -------------------------------------------
# from random import choice, sample
#
# my_list = [x for x in range(1, 11)]
#
# print('List:', my_list)
# print('Choice:', choice(my_list))
# print('Sample of #5:', sample(my_list, 5))
# print('Sample of #10:', sample(my_list, 10))

# -------------------------------------------
# 1.2.6 Selected functions from the platform module

# from platform import platform, machine, processor, system, version
#
# print(platform())
# print(platform(True))
# print(platform(False, True))
# print(machine())
# print(processor())
# print(system())
# print(version())

# -------------------------------------------
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr, end='.')
print()
