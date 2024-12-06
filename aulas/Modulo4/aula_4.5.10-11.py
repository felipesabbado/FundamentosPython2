"""4.5 Section 5 – The datetime module - working with time- and date-related functions"""
# 4.5.10 The gmtime() and localtime() functions
'''
# struct_time class
The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst. The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes.

time.struct_time:
    tm_year   # Specifies the year.
    tm_mon    # Specifies the month (value from 1 to 12)
    tm_mday   # Specifies the day of the month (value from 1 to 31)
    tm_hour   # Specifies the hour (value from 0 to 23)
    tm_min    # Specifies the minute (value from 0 to 59)
    tm_sec    # Specifies the second (value from 0 to 61 )
    tm_wday   # Specifies the weekday (value from 0 to 6)
    tm_yday   # Specifies the year day (value from 1 to 366)
    tm_isdst  # Specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
    tm_zone   # Specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # Specifies the offset east of UTC (value in seconds)
'''

import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

'''The difference between them is that the gmtime function returns the struct_time object in UTC, while the localtime function returns local time. For the gmtime function, the tm_isdst attribute is always 0.'''

# 4.5.11 The asctime() and mktime() functions
'''The time module has functions that expect a struct_time object or a tuple that stores values according to the indexes presented when discussing the struct_time class. Run the example in the editor.'''

st = time.gmtime(timestamp)
print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
