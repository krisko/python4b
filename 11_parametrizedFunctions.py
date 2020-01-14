#!/usr/bin/env python


def funcname(input, param):
    if param:
        uppercase = input.upper()
    else:
        uppercase = input
    return uppercase


print('Param ahoj, True: ' + funcname('ahoj', True))

print('Param ahoj, False: ' + funcname('ahoj', False))

print('Named notation: ' + funcname(input='MyName', param=True))
