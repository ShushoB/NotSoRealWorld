from abc import ABC, abstractmethod
from concrete_classes import *

class Human(ABC):
    def __init__(self, full_name, age, gender, profession):
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.profession = profession

    @abstractmethod
    def job(self):
        pass

    def get_name(self):
        print(self.full_name)

    def set_name(self, full_name):
        self.full_name = full_name

class Child(Human):
    def verify(self):
        if self.age <= 18:
            pass
        else:
            print (self.full_name+" isn't a child")

    def job(self):
        print("Children don't work")


class Adult(Human):

    def job(self):
        print(self.full_name + "'s profession is: " + self.profession)

    def travel(self, country):
        self.country = Country
        print(self.full_name + " travels to " + country.get_name())

    def call(self, phone, receiver):
        self.phone = Phone
        print(self.full_name + " calls from their " + phone.get_brand() + " phone to " + receiver)

    def adopt_pet(self, pet):
        self.pet = Animal
        print(self.full_name + " adopted " + pet.get_name())


class Animal(ABC):
    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender

    def set_name(self, name):
        self.name = name
        return self.name

    def get_name(self):
        return self.name

    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print(self.name + " says 'meow'")

class Dog(Animal):
    def make_sound(self):
        print(self.name + " says 'woof'")