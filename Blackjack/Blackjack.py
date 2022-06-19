from game_assets.assets import Deck, AIPlayer, Player


class Blackjack:
    def __init__(self):
        self._intro()

        self._deck = Deck()

        self._players = [
            Player(),
            AIPlayer(),
            AIPlayer(),
            AIPlayer(),
        ]

        self._reward = 0

        self.start()

    def start(self):
        # reset _reward
        self._reward = 0

        # reset deck
        self._deck.create()

        # get bet from all players: 10 credits
        for p in self._players:
            self._reward += p.give_bet(10)

        # todo start player turns
        for p in self._players:
            p.init_hand(self._deck)
            p.draw_cards(self._deck)

        # todo finish game and announce winner

        # todo ask player if want to play again

    @staticmethod
    def exit():
        print("See you later!")
        exit()

    @staticmethod
    def _intro():
        print("-" * 50, "BLACKJACK", "-" * 50)


Blackjack()