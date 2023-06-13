"""A  class that can be used to represent a lottery"""
from random import randint, random


class Lottery:
    def __init__(self, items=[], length=10, items_to_select=4,
                 words=['mario', 'luigi', 'pitch', 'browser', 'donki cong', 'kamek', 'toad', 'daisy', 'yoshi'],
                 my_ticket=''):
        """Initialize attributes to represent a Lottery"""
        self.items = items
        self.length = length
        self.items_select = items_to_select
        self.words = words
        self.my_ticket = my_ticket

    def fill_numbers(self):
        i = 0
        for value in range(1, 10):
            if i % 2 == 0:
                random_number = randint(1, 20)
                self.items.append(random_number)
            else:
                random_index = randint(0, 7)
                self.items.append(self.words[random_index])
            i = i + 1

    def print_values(self):
        for item in self.items:
            print(item)

    def lottery_analysis(self):
        flag = False
        counter = 1

        while not flag:

            if self.my_ticket in self.items:
                flag = True
            else:
                self.fill_numbers()
            counter = counter + 1

        print(f"Attemps {counter}")
