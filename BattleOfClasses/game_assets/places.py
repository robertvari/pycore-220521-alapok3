class PlaceBase:
    def __init__(self, name, game):
        self._name = name
        self._game = game
        self._player = None

    def enter(self, player):
        self._player = player
        self._game.clear_screen()
        print(f"Wellcome in the {self._name} {self._player}")

        self._main_menu()

    def _main_menu(self):
        print("PlaceBase _main_menu")


class Tavern(PlaceBase):
    def _main_menu(self):
        print("1. Buy something")
        print("2. Go back to the street.")

        user_input = input()

        if user_input == "1":
            print("TODO Buy something...")
        else:
            self._game.main_menu()

    def shop_menu(self):
        self._game.clear_screen()
        print(f"You have {self._player.golds} golds.")
        print("-"*50)




class Arena(PlaceBase):
    def _main_menu(self):
        print("1. Challenge yourself!")
        print("2. Go back to the street.")

        user_input = input()

        if user_input == "1":
            print("TODO Start challenge...")
        else:
            self._game.main_menu()