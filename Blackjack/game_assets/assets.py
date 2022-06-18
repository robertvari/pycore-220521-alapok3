class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def set_value(self, new_value):
        assert "Ace" in self._name, "Card must be Ace"
        assert isinstance(new_value, int), "Value must be of type int"
        self._value = new_value

    def __str__(self):
        return f"Name: {self._name} Value: {self._value}"

    def __repr__(self):
        return self._name


if __name__ == '__main__':
    card1 = Card("Heart Ace", 11)
    card2 = Card("Club Ace", 11)
    card3 = Card("Diamond Ace", 11)
    card4 = Card("Spade King", 10)
    deck = [card1, card2, card3, card4]
    card1.set_value(1)