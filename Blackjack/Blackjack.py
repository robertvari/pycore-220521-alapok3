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

        self._start()

    def _start(self):
        # reset _reward
        self._reward = 0

        # reset deck
        self._deck.create()

        # get bet from all players: 10 credits
        for p in self._players:
            self._reward += p.give_bet(10)

        # start player turns
        for p in self._players:
            p.init_hand(self._deck)
            p.draw_cards(self._deck)

        # todo finish round and announce winner
        self._get_winner()

        # todo ask player if want to play again

    def _get_winner(self):
        players_in_turn = [p for p in self._players if p.hand_value <= 21]

        if players_in_turn:
            winner_list = sorted(players_in_turn, key=lambda p: p.hand_value)
            winner = winner_list[-1]
            winner.give_reward(self._reward)
        else:
            print("Nobody wins this time :(")

        player_input = input("Do you want to play again? (y/n)")
        if player_input == "y":
            self._start()
        else:
            self._exit()

    @staticmethod
    def _exit():
        print("See you later!")
        exit()

    @staticmethod
    def _intro():
        print("-" * 50, "BLACKJACK", "-" * 50)


Blackjack()