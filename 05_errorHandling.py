#!/usr/bin/env python

x = 42
y = 0

try:
    print(x / y)
except ZeroDivisionError as e:
    print('dividing by zero???')
else:
    print('ooops, nothing to see here')
finally:
    print('be cool, you did it')