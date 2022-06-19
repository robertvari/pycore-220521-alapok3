class ItemBase:
    def __init__(self, name, price, attr_modifier):
        self._name = name
        self._price = price
        self._attr_modifier = attr_modifier
        
    def __repr__(self):
        return self._name

    def __str__(self):
        return f"Name: {self._name}\nPrice: {self._price}\nAttr Modifier: {self._attr_modifier}"