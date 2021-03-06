from random import shuffle, randint, choice
import time


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

    def give_reward(self, value):
        self._credits += value
        print(f"The winner is: {self._name}")
        print(f"{self._name} wins {value}. Now has {self._credits}")

    def reset(self):
        self._in_game = True

    def init_hand(self, deck):
        self._hand.clear()
        new_card = deck.draw_card()
        self._hand.append(new_card)

        new_card = deck.draw_card()
        if self.hand_value > 10 and "Ace" in new_card.name:
            new_card.set_value(1)

        self._hand.append(new_card)

    def give_bet(self, value):
        self._credits -= value
        if self._credits <= 0:
            self._in_game = False
        return value

    def draw_cards(self, deck):
        print("-"*20, f"{self._name} turns", "-"*20,)
        print(f"Hand: {self._hand}")
        print(f"Hand value: {self.hand_value}")

        while self._in_game:
            if self.hand_value < 19:
                new_card = deck.draw_card()

                print(f"{self._name} draws a card: {new_card}")
                time.sleep(1)
                if "Ace" in new_card.name and self.hand_value > 10:
                    new_card.set_value(1)

                self._hand.append(new_card)
            else:
                print(f"{self._name} finishes his/her turn")
                if self.hand_value > 21:
                    print(f"{self._name} lost this turn. Hand value: {self.hand_value}")
                time.sleep(1)
                self._in_game = False

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

        print("Wellcome to the game")
        print(f"You have {self._credits} credits to spend")
        print(f"Good luck!")

    def draw_cards(self, deck):
        print("This is your turn")

        while self._in_game:
            print(f"Your cards: {self._hand}")
            print(f"Your hand value: {self.hand_value}")

            player_input = input("Do you want to draw a new card? (y/n)")

            if player_input == "y":
                my_new_card = deck.draw_card()
                print(f"Your new card: {my_new_card}")
                if "Ace" in my_new_card.name and self.hand_value > 10:
                    my_new_card.set_value(1)

                self._hand.append(my_new_card)
            else:
                self._in_game = False


if __name__ == '__main__':
    deck = Deck()
    deck.create()

    player = Player()
    ai_player1 = AIPlayer()
    ai_player2 = AIPlayer()
    ai_player3 = AIPlayer()

    player.init_hand(deck)
    ai_player1.init_hand(deck)
    ai_player2.init_hand(deck)
    ai_player3.init_hand(deck)

    player_list = [player, ai_player1, ai_player2, ai_player3]

    for p in player_list:
        p.draw_cards(deck)