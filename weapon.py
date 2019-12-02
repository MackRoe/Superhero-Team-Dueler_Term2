from ability import Ability
import random


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between
        # half of max_damage and max_damage
        print("max damage of " + self.name + " is ")
        print(str(self.attack_strength))
        min_damage = self.attack_strength // 2
        weapon_attack_value = random.randint(min_damage, self.attack_strength)
        return weapon_attack_value
