"""4.5 Section 5 – The datetime module - working with time- and date-related functions"""
# 4.5.15 Date and time formatting
'''strftime method - String format time
A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter.'''
from datetime import date, time, datetime

d = date(2020, 1, 4)
print('Date:', d.strftime('%Y/%m/%d'))

t = time(14, 53)
print('Time:', t.strftime('%H:%M:%S'))

dt = datetime(2020, 11, 4, 14, 53)
print('Datetime:', dt.strftime('%y/%B/%d %H:%M:%S'))

'''You can find all available directives in https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes'''

# 4.5.16 The strftime() function in the time module
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print()
print(time.strftime('%Y/%m/%d %H:%M:%S', st))
print(time.strftime('%Y/%m/%d %H:%M:%S'))

'''You can find all available directives in the time module in https://docs.python.org/3/library/time.html#time.strftime'''

# 4.5.17 The strptime() method
print()
d2 = datetime.strptime('2019/11/04 14:53:00', '%Y/%m/%d %H:%M:%S')
print(d2)
print(d2.year)

'''In the time module, you can find a function called strptime, which parses a string representing a time to a struct_time object. Its use is analogous to the strptime method in the datetime class.'''

print(time.strptime('2019/11/04 14:53:00', '%Y/%m/%d %H:%M:%S'))
