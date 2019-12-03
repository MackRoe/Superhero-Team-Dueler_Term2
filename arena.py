from hero import Hero
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = team_one
        self.team_two = team_two

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the weapon?  ")
        max_damage = input(
            "What is the max damage of the weapon?  ")

        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new
        #   armor object.
        #  return the new armor object with values set by user.
        name = input("What is the name of the armor?  ")
        max_damage = input(
            "What is the max damage of the armor?  ")

        return Armor(name, max_damage)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            print("[1] Add ability\n[2] Add weapon\n[3] Add armor")
            add_item = input("[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                # add an ability to the hero
                create_ability()
            elif add_item == "2":
                # add a weapon to the hero
                create_weapon()
            elif add_item == "3":
                # add an armor to the hero
                create_armor()
        return hero

    def build_teams(self):
        '''helper function for build_team_one and build_team_two'''
        # 1) Prompt the user for the name of the team (√)
        team_name = input("Name your team: ")
        # 2) Prompt the user for the number of Heroes on the team
        team_size = input("How many members are in your team? ")
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        built_team = []
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        while team_size > 0:
            team_member = self.create_hero()
            team_size -= 1
            built_team.append(team_member)
        return built_team

    def build_team_one(self):
        self.team1 = build_teams()
        return self.team1

    def build_team_two(self):
        self.team2 = build_teams()
        return self.team2

    def team_battle(self, team1, team2):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        Team.attack(team1, team2)
