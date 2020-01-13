#!/usr/bin/env python

# dictionary
name = {}
name['first'] = 'Michal'
name['last'] = 'Krisko'

print(name)

nextname = {'first': 'Kaisa', 'last': 'Ko'}

print(nextname)

# list/array
people = [name, nextname]
print(people)
people.append({'first': 'Abc', 'last': 'FGH'})

print(people)
