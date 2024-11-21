# 2.8 Section 8 – Useful exceptions
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# We must be sure that angle != 90 + k * 180
try:
    assert angle % 180 != 90
    print(tan(radians(angle)))
except AssertionError:
    print('Invalid angle')
except BaseException:
    print('Erro')
