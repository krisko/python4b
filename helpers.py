#!/usr/bin/env python


def display(msg, isWarn=False):
    if isWarn:
        print('WARNING!! ' + msg)
    else:
        print(msg)


def error(msg, isErr=False):
    if isErr:
        print('ERROR!! ' + msg)
    else:
        print(msg)
