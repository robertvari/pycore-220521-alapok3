class Person:
    def __init__(self, name, age=None, email=None, address=None):
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}\nAddress: {self.address}"

    def __repr__(self):
        return self.name


tamas = Person(name="Tamás", age=32, email="tamas@gmail.com", address="Budapest")
robert = Person(name="Robert", age=42, email="robert@gmail.com", address="Pécs")
csilla = Person(name="Csilla", age=28, email="csilla@gmail.com", address="Debrecen")

my_friends = [tamas, robert, csilla]
print(my_friends)
print(csilla)
