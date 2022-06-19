import os


class BattleOfClasses:
    def __init__(self):
        self._intro()

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


BattleOfClasses()
