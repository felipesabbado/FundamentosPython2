"""4.5 Section 5 – The datetime module - working with time- and date-related functions"""
# 4.5.12 Creating datetime objects
'''datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)'''

from datetime import datetime

d = datetime(2019, 11, 4, 14, 53, 0, 0)
print('Datetime:', d)
print('Date:', d.date())
print('Time:', d.time())

# 4.5.13 Methods that return the current date and time
'''
* today() — returns the current local date and time with the tzinfo attribute set to None;
* now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass;
* utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.
'''

print('today:', datetime.today())
print('now:', datetime.now())
# print('utcnow', datetime.utcnow()) # Deprecated

# 4.5.14 Getting a timestamp
dt = datetime(2020, 10, 4, 14, 55)
print('Timestamp:', dt.timestamp())
print('d timestamp:', d.timestamp())
