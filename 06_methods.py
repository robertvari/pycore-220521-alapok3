import random, time


class Dice:
    def __init__(self, color, sides):
        # instance attribute is unique to the instance
        self.color = color
        self.sides = sides
        self.current_side = 1

    def report(self):
        print(f"Color: {self.color} Sides: {self.sides} Current Side: {self.current_side}")

    def roll(self):
        self.current_side = random.randint(1, self.sides)
        print(f"{self.color} {self.sides} rolled...")
        time.sleep(random.randint(1, 3))
        print(f"Current side: {self.current_side}")


white6 = Dice("white", 6)
red10 = Dice("red", 10)
blue20 = Dice("blue", 20)

white6.roll()