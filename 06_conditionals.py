#!/usr/bin/env python

price = input('Whats the price?? ')

price = float(price)
if price >= 1.00:
    tax = .07
    print('Tax rate is ' + str(tax))
else:
    tax = 0
    print('No tax rate for you!')

print('Final price ' + str(price+price*tax))
