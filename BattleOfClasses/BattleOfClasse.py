import os
from game_assets.characters import Player
from game_assets.places import Arena, Tavern


class BattleOfClasses:
    def __init__(self):
        self._intro()

        self._player = Player()
        self._arena = Arena("Arena", self)
        self._tavern = Tavern("Black Horse tavern", self)

        self.main_menu()

    def _intro(self):
        self.clear_screen()
        print("-"*50, "BATTLE OF CLASSES", "-"*50)

    @staticmethod
    def _exit():
        print("Have nice day!")
        exit()

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def main_menu(self):
        self.clear_screen()

        print(f"Wellcome in this small town {self._player}")
        print("There is a tavern on the right and an arena on the left.")
        print("Where do you want to go?")
        print("1. Black Horse tavern")
        print("2. Arena")
        print("3. Exit game")

        player_input = input()

        if player_input == "1":
            self._tavern.enter(self._player)
        elif player_input == "2":
            self._arena.enter(self._player)
        else:
            self._exit()


BattleOfClasses()
