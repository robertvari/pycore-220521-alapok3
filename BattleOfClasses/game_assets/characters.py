import random
from game_assets.items import Weapon, CommonItem


class CharacterBase:
    def __init__(self):
        self._name = None

        # todo add attributes here...
        self._golds = random.randint(2, 20)
        self._inventory = []
        self._right_hand = None

        self._create()

    @property
    def golds(self):
        return self._golds

    def _create(self):
        self._name = self.get_fantasy_name()

    @staticmethod
    def get_fantasy_name():
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        return f"{random.choice(FIRST)}{random.choice(SECOND)}"

    def __str__(self):
        return self._name


class Player(CharacterBase):
    def _create(self):
        # self._name = input("What is your name?")
        self._name = "Robert Vari"

        # todo remove this!!
        self._golds = 100

    def buy(self, item):
        self._golds -= item.price

        if isinstance(item, Weapon) and not self._right_hand:
            self._right_hand = item
        else:
            self._inventory.append(item)

        # if item type == Weapon att to right hand


class AIPlayer(CharacterBase):
    def _create(self):
        super(AIPlayer, self)._create()

        item_data = [
            {"type": "CommonItem", "name": "Bread", "price": 10, "attr_modifier": 5},
            {"type": "CommonItem", "name": "Milk", "price": 20, "attr_modifier": 13},
            {"type": "CommonItem", "name": "Cheese", "price": 34, "attr_modifier": 40},
            {"type": "CommonItem", "name": "Meat", "price": 40, "attr_modifier": 60},
            {"type": "Weapon", "name": "Hammer", "price": 24, "attr_modifier": 30},
            {"type": "Weapon", "name": "Sword", "price": 12, "attr_modifier": 15},
            {"type": "Weapon", "name": "Dagger", "price": 20, "attr_modifier": 23},
            {"type": "Weapon", "name": "Spear", "price": 34, "attr_modifier": 40},
        ]

        chosen_item = random.choice(item_data)
        if chosen_item["type"] == "Weapon":
            self._right_hand = Weapon(chosen_item["name"], chosen_item["price"], chosen_item["attr_modifier"])
        else:
            self._inventory.append(CommonItem(chosen_item["name"], chosen_item["price"], chosen_item["attr_modifier"]))


if __name__ == '__main__':
    enemy1 = AIPlayer()
    enemy2 = AIPlayer()
    enemy3 = AIPlayer()
    enemy4 = AIPlayer()
