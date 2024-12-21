class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Cat(Animal):
    def __init__(self, name, catage):
        Animal.__init__(self, name, species= "Dog")
        self.breed = catage

    def make_sound(self):
        print("Meow!")

d = Cat("Cat", "Catt")
d.make_sound()
a = Animal("Cat","Caat")
a.make_sound()