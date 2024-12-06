""" 4.6 Section 6 – The calendar module - working with calendar-related functions """


def header(txt):
    txt = ' ' + txt + ' '
    print()
    print(txt.center(67, '-'))
    print()


# 4.6.1 Introduction to the calendar module
header('4.6.1 Introduction to the calendar module')
week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print('Day of the week\t\tInteger value\t\t\tConstant')
for k, v in enumerate(week_days):
    print(f'{v:^15}\t\t{k:^12}\t\tcalendar.{v.upper()}')

# 4.6.2 Your first calendar
header('4.6.2 Your first calendar')
import calendar

# print(calendar.calendar(2024, c=3))
'''
w – date column width (default 2)
l – number of lines per week (default 1)
c – number of spaces between month columns (default 6)
m – number of columns (default 3)
'''
calendar.prcal(2025, c=3) # It doesn't require to use the print function

# 4.6.3 Calendar for a specific month
header('4.6.3 Calendar for a specific month')
import calendar

print(calendar.month(2024, 12, w=3))
# calendar.prmonth(2024, 12) # The same as above but it doesn't need the print function
'''
w – date column width (default 2)
l – number of lines per week (default 1)
'''

# 4.6.4 The setfirstweekday() function
header('4.6.4 The setfirstweekday() function')
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2024, 12)

# 4.6.5 The weekday() function
header('4.6.5 The weekday() function')
print(calendar.weekday(2020, 12, 24))
print('The weekday function returns 3, which means that December 24, 2020 is a Thursday.')

# 4.6.6 The weekheader() function
header('4.6.6 The weekheader() function')
print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))
print(calendar.weekheader(4))
print(calendar.weekheader(5))

# 4.6.7 How do we check if a year is a leap year?
header('4.6.7 How do we check if a year is a leap year?')

year = 2024
print(f'Is {year} a leap year?', calendar.isleap(year))
'''leapdays - returns the number of leap years in the given range of years'''
print('Leap years in range 2010-2021:', calendar.leapdays(2010,2021)) # Up to but not including 2021

# 4.6.8 Classes for creating calendars
header('4.6.8 Classes for creating calendars')
print('* calendar.Calendar – provides methods to prepare calendar data for formatting;')
print('* calendar.TextCalendar – is used to create regular text calendars;')
print('* calendar.HTMLCalendar – is used to create HTML calendars;')
print('* calendar.LocalTextCalendar – is a subclass of the calendar.TextCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.')
print('* calendar.LocalHTMLCalendar – is a subclass of the calendar.HTMLCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.')

# 4.6.9 Creating a Calendar object
header('4.6.9 Creating a Calendar object')

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=' ')
print()

# 4.6.10 The itermonthdates() method
header('4.6.10 The itermonthdates() method')

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=' ')
print()

# 4.6.11 Other methods that return iterators
header('4.6.11 Other methods that return iterators')
'''
itermonthdates - takes year and month as parameters, and then returns the iterator to the days of the week represented by numbers.
itermonthdates2 – returns days in the form of tuples consisting of a day of the month number and a week day number;
itermonthdates3 – returns days in the form of tuples consisting of a year, a month, and a day of the month numbers.
itermonthdates4 – returns days in the form of tuples consisting of a year, a month, a day of the month, and a day of the week numbers.
'''
for i in c.itermonthdays(2019, 11):
    print(i, end=' ')
print()

# 4.6.12 The monthdays2calendar() method
header('4.6.12 The monthdays2calendar() method')
'''The Calendar class has several other useful methods that you can learn more about in the documentation (https://docs.python.org/3/library/calendar.html).
One of them is the monthdays2calendar method, which takes the year and month, and then returns a list of weeks in a specific month. Each week is a tuple consisting of day numbers and weekday numbers.'''
for data in c.monthdays2calendar(2020, 12):
    print(data)
