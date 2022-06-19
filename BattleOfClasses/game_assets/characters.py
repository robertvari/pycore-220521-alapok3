import random
from game_assets.items import Weapon


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
    pass


if __name__ == '__main__':
    player = Player()
    sword = Weapon("Sword", 10, 20)
    hammer = Weapon("Hammer", 10, 20)

    player.buy(sword)
    player.buy(hammer)

    pass