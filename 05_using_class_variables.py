class Dice:
    # class attribute is shared attribute
    count = 0

    def __init__(self, color, sides):
        # instance attribute is unique to the instance
        self.color = color
        self.sides = sides

        Dice.count += 1


white6 = Dice("shite", 6)
red10 = Dice("red", 10)
green12 = Dice("green", 12)
blue20 = Dice("blue", 20)
print(Dice.count)
print(blue20.count)