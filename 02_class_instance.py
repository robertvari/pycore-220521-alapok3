class Dice:
    # class variables
    sides = 6
    color = "white"


# create an instance of a class: Dice
white_dice = Dice()
blue_dice = Dice()
blue_dice.color = "blue"

print(white_dice.color)
print(blue_dice.color)