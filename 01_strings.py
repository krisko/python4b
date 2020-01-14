#!/usr/bin/env python

fname = 'KaISa'
lname = 'Ko'

print('Hello ' + fname.capitalize() + ' ' + lname.upper())
# print('text: ' + fgh)


outputA = 'Hello, {} {}'.format(fname, lname)
outputB = 'Hello, {1} {0}'.format(fname, lname)
outputC = f'Hello, {fname} {lname}'

print(outputA + "::" + outputB + "::"+ outputC)
