class PlaceBase:
    def __init__(self, name):
        self._name = name
        self._player = None

    def enter(self, player):
        self._player = player
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
            print("TODO Go back to main menu")


class Arena(PlaceBase):
    def _main_menu(self):
        print("1. Challenge yourself!")
        print("2. Go back to the street.")

        user_input = input()

        if user_input == "1":
            print("TODO Start challenge...")
        else:
            print("TODO Go back to main menu")