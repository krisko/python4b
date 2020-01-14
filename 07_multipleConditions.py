#!/usr/bin/env python

letter = input("Choose your letter: ")
if letter in ('a', 'b', 'c'):
    print('ABC')
elif letter == 'd' or letter == 'e':
    print('DE')
else:
    print('Other')
