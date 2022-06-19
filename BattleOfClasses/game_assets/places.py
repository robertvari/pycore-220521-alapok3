class PlaceBase:
    def __init__(self, name):
        self._name = name
        self._player = None

    def enter(self, player):
        self._player = player
        print(f"Wellcome in the {self._name} {self._player}")


class Tavern(PlaceBase):
    pass


class Arena(PlaceBase):
    pass