class ItemBase:
    def __init__(self, name, price, attr_modifier):
        self._name = name
        self._price = price
        self._attr_modifier = attr_modifier

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self._name

    def __str__(self):
        return f"{self._name} Price: {self._price} Attr Modifier: {self._attr_modifier}"


class CommonItem(ItemBase):
    pass


class Weapon(ItemBase):
    pass


if __name__ == '__main__':
    bread = CommonItem(name="Bread", price=5, attr_modifier=10)
    milk = CommonItem("Milk", 10, 20)
    cheese = CommonItem("Cheese", 30, 50)

    hammer = Weapon("Hammer", 40, 30)
    sword = Weapon("Sword", 10, 10)

    shop_items = [
        bread,
        milk,
        cheese,
        hammer,
        sword
    ]

    for index, i in enumerate(shop_items):
        print(index, i)