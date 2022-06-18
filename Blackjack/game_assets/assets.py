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


class Deck:
    def __init__(self):
        self._cards = []

    def create(self):
        self._cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card in cards:
                card_name = f"{name} {card[0]}"
                value = card[1]
                card = Card(card_name, value)
                self._cards.append(card)

        print(self._cards)


if __name__ == '__main__':
    deck = Deck()
    deck.create()