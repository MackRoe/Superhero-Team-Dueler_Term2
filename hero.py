from ability import Ability
from weapon import Weapon


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
          kills: Integer
          deaths: Integer
      '''
    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
        self.abilities = []
        self.armors = []
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        # Update the constructor for Hero class to track deaths and kills
        self.deaths = 0
        self.kills = 0

    def __str__(self):
        '''string conversion method'''
        return self.name

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We used the append method to add strings to a list
        # in the Rainbow Checklist tutorial. This time,
        # we're not adding strings, instead we'll add ability objects.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
      '''
    # start our total out at 0
        print("--attack method called--")
        total_damage = 0
        # loop through all of our hero's abilities
        for each in self.abilities:
            # add the damage of each attack to our running total

            total_damage += each.attack()
            print("Total Damage is " + str(total_damage))
        # return the total damage
        return int(total_damage)

    def add_armor(self, armor):
        '''Add armor to self.armors
    Armor: Armor Object
  '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
     return: total_block:Int
  '''
    # TODO: This method should run the block method on each armor
    # in self.armors
        defense = 0
        # initializes the defense variable
        # which stores the accumated values of all block actions
        if len(self.armors) > 0:
            for each_armor in self.armors:
                defense += each_armor.block()
            print(f"Armor blocks " + str(defense) + " points of damage")
            return defense
        else:
            return 0

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
  '''
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self):
        '''Check current_health. If less than or equal to zero, return
        False. Otherwise return True'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        '''Current Hero will take turns fighting an opponent hero'''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has
        #   abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and
        #   each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent
        #   is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName
        #   with the name of the hero, and end the fight loop
        print("-- hero.fight method called --")
        print(f"Hero abilities: {self.abilities}")
        print(f"Opponent abilities: {opponent.abilities}")

        while self.is_alive() and opponent.is_alive():
            if self.abilities == opponent.abilities:
                # declare a draw if combatant abilities are equivalent
                print("Hero abilities are equivalent. No victor possible.")
                print("Match declared a Draw")
                return
            # attack opponent
            damage = self.attack()
            # accumulate opponent's damage
            opponent.take_damage(damage)
            # be attacked by opponent
            damage = opponent.attack()
            # be attacked by opponent
            self.take_damage(damage)

        if self.current_health > 0:
            print(self.name + " is victorious!")
            self.add_kill(1)
            opponent.add_death(1)
        else:
            print(opponent.name + " is victorious!")
            self.add_death(1)
            opponent.add_kill(1)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths
