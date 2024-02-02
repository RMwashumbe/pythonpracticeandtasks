class Animal:
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age

    def speak(self):
        raise NotImplementedError("Child classes must implement this method")


class Dog(Animal):
    def speak(self):
        return "Barks"


class Cat(Animal):
    def speak(self):
        return "Meows"


class Lion(Animal):
    def speak(self):
        return "Roars"


dog = Dog("Bosco", "Black and white", "3 years")
print(dog.name)
print(dog.colour)
print(dog.speak)

cat = Cat("Sucrose", "Grey", "2 years")
print(cat.name)
print(cat.colour)
print(cat.speak)

lion = Lion("The wild lion", "Golden Brown", "3 Years")
print(lion.name)
print(lion.speak)
print(lion.colour)
