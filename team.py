import random


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        ''' Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero)

    def add_hero(self, hero):
        '''Add hero to self.heroes'''
        self.heroes.append(hero)

    def stats(self):
        '''print team stats'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name, kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        # added team arg
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()
        # changed list() to team and other_team

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # TODO: Complete the following steps:
            # Randomly select a living hero from each team (√)
            random_living_hero = random.choice(living_heroes)
            random_living_opponent = random.choice(living_opponents)
            # have the heroes fight each other (√)
            random_living_hero.fight(random_living_opponent)
            # update the list of living_heroes and living_opponents
            # to reflect the result of the fight (√)
            status = hero.is_alive()
            if random_living_hero.is_alive():
                living_opponents.remove(random_living_opponent)
            else:
                living_heroes.remove(random_living_hero)
