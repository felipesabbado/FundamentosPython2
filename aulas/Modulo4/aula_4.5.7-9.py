"""4.5 Section 5 – The datetime module - working with time- and date-related functions"""
# 4.5.7 Creating time objects
'''time(hour, minute, second, microsecond, tzinfo, fold)'''

from datetime import time
t = time(14, 53, 20, 1)

print('Time:', t)
print('Hour:', t.hour)
print('Minute:', t.minute)
print('Second:', t.second)
print('Microsecond:', t.microsecond)

# 4.5.8 The time module
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print('I slept well! I feel great!')

student = Student()
# student.take_nap(5)

# 4.5.9 The ctime() function
'''The ctime function returns a string for the passed timestamp.'''

timestamp = 1572879180
print('String from timestamp:', time.ctime(timestamp))
print('Current time:', time.ctime())
