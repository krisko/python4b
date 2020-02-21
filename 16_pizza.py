#!/usr/bin/env python

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'You will get: {self.ingredients!r} on your pizza'
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

out = Pizza.margherita()

print(out)

