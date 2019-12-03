import random


class Ability:
    def __init__(self, name, attack_strength):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        # self.max_damage = 100
        self.attack_strength = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by
        self.attack_strength.'''

        # Pick a random value between 0 and self.attack_strength
        whatever = random.randint(0, self.attack_strength)
        print(self.name + " attack of " + str(whatever))
        return whatever
