"""A class that can be used to represent a dice"""
from random import randint


class Dice:
    def __init__(self, side=6):
        """Initialize atributes to represent a Die"""
        self.side = side

    def print_side(self):
        """Method to print the number side"""
        print(f"Dice has {self.side} sides")

    def roll_die(self):
        """Method to prints a random number between 1 and the number or sides the die has"""
        number_random = randint(1, self.side)
        return number_random

