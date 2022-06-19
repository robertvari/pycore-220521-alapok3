from random import shuffle, randint, choice


class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def set_value(self, new_value):
        assert "Ace" in self._name, "Card must be Ace"
        assert isinstance(new_value, int), "Value must be of type int"
        self._value = new_value

    @property
    def value(self):
        return self._value

    @property
    def name(self):
        return self._name

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

        shuffle(self._cards)

    def draw_card(self):
        new_card = self._cards[0]
        self._cards.remove(new_card)
        return new_card


class PlayerBase:
    def __init__(self):
        self._name = None
        self._hand = []
        self._credits = randint(10, 100)
        self._in_game = True

        self._create()

    def init_hand(self, deck):
        self._hand.clear()
        new_card = deck.draw_card()
        self._hand.append(new_card)

        new_card = deck.draw_card()
        if self.hand_value > 10 and "Ace" in new_card.name:
            new_card.set_value(1)

        self._hand.append(new_card)

    def draw_cards(self, deck):
        while self._in_game:
            if self.hand_value < 18:
                new_card = deck.draw_card()
                if "Ace" in new_card.name and self.hand_value > 10:
                    new_card.set_value(1)

                self._hand.append(new_card)


    @property
    def hand_value(self):
        return sum([card.value for card in self._hand])

    def _create(self):
        first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
        last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]
        self._name = f"{choice(first_names)} {choice(last_names)}"

    def report(self):
        print(f"Name: {self._name} Hand: {self._hand} Credits: {self._credits} Hand Value: {self.hand_value}")


class AIPlayer(PlayerBase):
    pass


class Player(PlayerBase):
    def _create(self):
        # player_name = input("What is your name?")
        player_name = "Robert Vari"
        self._name = player_name


if __name__ == '__main__':
    deck = Deck()
    deck.create()

    player = Player()
    ai_player = AIPlayer()

    player.init_hand(deck)
    ai_player.init_hand(deck)

    player_list = [player, ai_player]

    for p in player_list:
        p.draw_cards(deck)