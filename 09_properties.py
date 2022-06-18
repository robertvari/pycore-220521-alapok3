import random


class Dice:
    color_list = ["blue", "red", "white"]

    def __init__(self, color, sides):
        # private attribute
        self.__color = color
        self.__sides = sides

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, new_sides):
        assert isinstance(new_sides, int), "sides must be of type int"
        assert new_sides > 3, "Sides must be > 3"
        self.__sides = new_sides

    def roll(self):
        print(random.randint(1, self.__sides))

    def __str__(self):
        return f"{self.__color} {self.__sides}"


class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"


robert = Person("Robert", "Vari")
print(robert.full_name)