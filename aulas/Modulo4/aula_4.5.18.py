"""4.5 Section 5 – The datetime module - working with time- and date-related functions"""
# 4.5.18 Date and time operations
from datetime import date, datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)
print()

# 4.5.19 Creating timedelta objects
'''The arguments accepted by the class constructor are: days, seconds, microseconds, milliseconds, minutes, hours, and weeks. Each of them is optional and defaults to 0.

The timedelta object only stores days, seconds, and microseconds internally.'''
from datetime import timedelta, date, datetime

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
print('Days:', delta.days) # 2 weeks (14) + 2 days = 16 days
print('Seconds:', delta.seconds) # 3 hours = 10800 seconds
print('Microseconds:', delta.microseconds)

print(' deltatime usecase '.center(40, '-'))

delta = timedelta(weeks=2, days= 2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)
