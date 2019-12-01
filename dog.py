# dog.py
from animal import Animal


class Dog(Animal):
    # def __init__(self, name, sleep_duration, breed):
    #     super().__init__(self, name, sleep_duration)
    #     # turns class into a subclass
    #     self.breed = breed

    def bark(self):
        print(self.name + ": Woof!")

    def sit(self):
        print(self.name + " sits")

    def roll_over(self):
        print(self.name + " rolls over")
