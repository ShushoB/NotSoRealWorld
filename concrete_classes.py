from abc import ABC, abstractmethod
from abstract_classes import *

class Country():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def recognize_Artsakh(self):
        print(self.name + " recogizes Artsakh")

    def win_Eurovision(self, win):
        if win == 'yes':
            print(self.name + ' wins Eurovision 2023')
        elif win == 'no':
            print(self.name + " didn't win, better luck next year")

class Phone():
    def __init__(self, brand, owner):
        self.owner = owner
        self.brand = brand

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        print(self.brand)
        return self.brand
