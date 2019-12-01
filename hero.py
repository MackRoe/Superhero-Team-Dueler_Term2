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

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We used the append method to add strings to a list
        # in the Rainbow Checklist tutorial. This time,
        # we're not adding strings, instead we'll add ability objects.
        self.abilities.append(ability)
        print("add_ability method called")
        # for ability in self.abilities:
        #     print(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
      '''
    # start our total out at 0
        print("--attack method called--")
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
            print("Total Damage is " + str(total_damage))
        # return the total damage
        return total_damage

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
            return defense
        else:
            return 0

    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense
