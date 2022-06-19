import os
from game_assets.characters import Player


class BattleOfClasses:
    def __init__(self):
        self._intro()

        self._player = Player()

        self._main_menu()

    def _intro(self):
        self._clear_screen()
        print("-"*50, "BATTLE OF CLASSES", "-"*50)

    @staticmethod
    def _exit():
        print("Have nice day!")
        exit()

    @staticmethod
    def _clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def _main_menu(self):
        print(f"Wellcome in this small town PLAYER_NAME")
        print("There is a tavern on the right and an arena on the left.")
        print("Where do you want to go?")
        print("1. Black Horse tavern")
        print("2. Arena")
        print("3. Exit game")

        player_input = input()

        if player_input == "1":
            print("Go to Black Horse tavern...")
        elif player_input == "2":
            print("Go to the Arena")
        else:
            self._exit()


BattleOfClasses()
