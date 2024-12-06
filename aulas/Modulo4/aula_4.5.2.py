"""4.5 Section 5 – The datetime module - working with time- and date-related functions"""
# 4.5.2 Getting the current local date and creating date objects

from datetime import date

today = date.today()
my_date = date(2019, 11, 4)
dates = (today, my_date)

for d in dates:
    print('-' * 20)
    print('Date:', d)
    print('Year:', d.year)
    print('Month:', d.month)
    print('Day:', d.day)
print('-' * 20)
