import random


class Dice:
    color_list = ["blue", "red", "white"]

    def __init__(self, color, sides):
        # public attribute.
        # self.color = color
        # self.sides = sides

        # protected attributes
        # self._color = color
        # self._sides = sides

        # private attribute
        self.__color = color
        self.__sides = sides

    def set_color(self, new_color):
        assert new_color in Dice.color_list, f"Color must be set to these: {Dice.color_list}"
        self.__color = new_color

    def set_sides(self, new_sides):
        assert isinstance(new_sides, int), "Sides must be of type int!"
        self.__sides = new_sides

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def roll(self):
        print(random.randint(1, self.__sides))

    def __str__(self):
        return f"{self.__color} {self.__sides}"


white6 = Dice("white", 6)
white6.set_color("blue")
white6.roll()
print(white6)