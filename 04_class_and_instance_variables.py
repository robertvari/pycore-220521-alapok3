class Dice:
    # class variable
    color = "blue"

    def __init__(self, sides, color):
        # instance variables
        self.sides = sides
        self.color = color


my_dice = Dice(6, "white")
# print(my_dice.color)
# print(Dice.color)

my_dice.color = "red"
Dice.color = "green"
print(my_dice.color)
print(Dice.color)