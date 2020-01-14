#!/usr/bin/env python

import datetime


def print_time(desc):
    print(desc)
    print(datetime.datetime.now())
    print()


name = 'kaisa'
print_time('name is set to ' + name)

for x in range(0, 10):
    print(x)
print_time('loop is done, name initial is: ' + name[0:1].upper())


def yourInit(input):
    return input[0:1].upper()


print('Initials function ' + yourInit(name))
