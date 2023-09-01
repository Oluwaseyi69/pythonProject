class Animal:
    def __init__(self):
        self.number_of_nose = 1

    def eat(self):
        print("eating")

class Dog (Animal):
    # overiding

    def __init__(self):
        self.number_of_nose = 4
        super().__init__()


# getter
    @property
    def number_of_legs(self):
        return self.number_of_legs

    # setter
    @number_of_legs.setter
    def number_of_legs(self, number_of_legs):
        if number_of_legs != 4:
            self.number_of_legs = number_of_legs

    def walk(self):
        print("walking")

class Fish(Animal):
    def swim(self):
        print("swimming")


f1 = Fish.swim
