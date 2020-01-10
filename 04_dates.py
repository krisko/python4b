#!/usr/bin/env python

from datetime import datetime, timedelta

current_date = datetime.now()

print('Today is: ' + str(current_date))
print('Day only: ' + str(current_date.day))


one_day = timedelta(days=1)
yesterday = current_date - one_day
print(timedelta(days=1))
print('Yesterday was: ' + str(yesterday))

today = datetime.now()
print('Hour: ' + str(today.hour))
print()

bday = input('Enter you Bday (dd/mm/yyy): ')
bday_date = datetime.strptime(bday, '%d/%m/%Y')

print('Your Bday is at ' + str(bday_date))
