class Animal(object):
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(self.name + " sleeps for")
        print(self.sleep_duration + " hours")

    def eat(self):
        print(self.name + "is eating")

    def drink(self):
        print(self.name + "is drinking")


class Frog(Animal):
    has_wings = None

    def jump(self):
        if has_wings:
            print(self.name + "jumps and doesn't bump their butt")
        else:
            print(self.name + "jumps and bumps their butt")
