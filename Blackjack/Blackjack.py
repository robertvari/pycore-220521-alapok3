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
        pass

        #

    @staticmethod
    def exit():
        print("See you later!")
        exit()

    @staticmethod
    def _intro():
        print("-" * 50, "BLACKJACK", "-" * 50)


Blackjack()