class Dice:
    def __init__(self, sides, color):
        # instance variables
        self.sides = sides
        self.color = color


white6 = Dice(6, "white")
blue10 = Dice(10, "blue")
red20 = Dice(20, "red")

print(white6.sides, white6.color)
print(blue10.sides, blue10.color)
print(red20.sides, red20.color)