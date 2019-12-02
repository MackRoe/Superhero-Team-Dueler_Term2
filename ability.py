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
        self.max_damage = 100
        self.attack_strength = attack_strength

    def attack(self, attack_strength):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        # Pick a random value between 0 and self.max_damage
        self.attack_strength = random.randint(0, self.max_damage)
        print(self.name + " attack of " + str(self.attack_strength))
        return self.attack_strength
