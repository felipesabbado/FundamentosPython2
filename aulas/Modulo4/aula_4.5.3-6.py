"""4.5 Section 5 – The datetime module - working with time- and date-related functions"""
# 4.5.3 Creating a date object from a timestamp
from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print('Date:', d)

# 4.5.4 Creating a date object using the ISO format
'''The fromisoformat() function is used to constructs a date object from a specified string that contains a date in ISO format. i.e., yyyy-mm-dd.'''

d2 = date.fromisoformat('2019-11-04')
print('ISO Format:', d2)

# 4.5.5 The replace() method
'''The year, month, and day parameters are optional. You can pass only one parameter to the replace method, e.g., year, or all three as in the example. The replace method returns a changed date object, so you must remember to assign it to some variable.'''

d2 = d2.replace(year=2000, month=12, day=16)
print('New date:', d2)

# 4.5.6 What day of the week is it?
'''The weekday method returns the day of the week as an integer, where 0 is Monday and 6 is Sunday. Run the code in the editor.'''

d3 = date(2019, 11, 4)
print('Weekday:', d3.weekday())

'''The date class has a similar method called isoweekday, which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday.'''

print('ISO Weekday', d3.isoweekday())
