from game_assets.items import CommonItem, Weapon
from game_assets.characters import AIPlayer


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
    def __init__(self, name, game):
        super().__init__(name, game)
        self._items = []
        self._create_shopping_list()

    def _create_shopping_list(self):
        item_data = [
            {"type": "CommonItem", "name": "Bread", "price": 10, "attr_modifier": 5},
            {"type": "CommonItem", "name": "Milk", "price": 20, "attr_modifier": 13},
            {"type": "CommonItem", "name": "Cheese", "price": 34, "attr_modifier": 40},
            {"type": "CommonItem", "name": "Meat", "price": 40, "attr_modifier": 60},
            {"type": "Weapon", "name": "Hammer", "price": 24, "attr_modifier": 30},
            {"type": "Weapon", "name": "Sword", "price": 12, "attr_modifier": 15},
        ]

        for i in item_data:
            if i["type"] == "CommonItem":
                self._items.append(CommonItem(i["name"], i["price"], i["attr_modifier"]))
            elif i["type"] == "Weapon":
                self._items.append(Weapon(i["name"], i["price"], i["attr_modifier"]))

    def _main_menu(self):
        self._game.clear_screen()

        print("1. Buy something")
        print("2. Go back to the street.")

        user_input = input()

        if user_input == "1":
            self._shop_menu()
        else:
            self._game.main_menu()

    def _shop_menu(self):
        self._game.clear_screen()
        print(f"You have {self._player.golds} golds.")
        print("-"*50)

        index = 0
        for index, i in enumerate(self._items):
            print(f"{index} {i}")

        print("-"*50)
        print(f"{index + 1} Back to main menu")

        user_input = int(input())

        if user_input == index + 1:
            self._main_menu()

        chosen_item = self._items[user_input]
        if chosen_item.price > self._player.golds:
            print(f"You don't have enough gold to buy a: {chosen_item.name}")
            input("Press enter to continue")
            self._shop_menu()

        self._player.buy(chosen_item)
        print(f"You bought a {chosen_item.name}")
        print("Press enter to continue")
        input()
        self._main_menu()


class Arena(PlaceBase):
    def __init__(self, name, game):
        super().__init__(name, game)
        self._enemy_list = []
        for _ in range(20):
            self._enemy_list.append(AIPlayer())

    def _main_menu(self):
        self._game.clear_screen()

        print("1. Challenge yourself!")
        print("2. Go back to the street.")

        user_input = input()

        if user_input == "1":
            print("TODO Start challenge...")
        else:
            self._game.main_menu()

    def start_challenge(self):
        self._game.clear_screen()


if __name__ == '__main__':
    arena = Arena("Arena", None)
    pass