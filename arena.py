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
        self.team_one = []
        self.team_two = []
        self.team_size = 0
        self.team_one_size = 0
        self.team_two_size = 0

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
                self.create_ability()
            elif add_item == "2":
                # add a weapon to the hero
                self.create_weapon()
            elif add_item == "3":
                # add an armor to the hero
                self.create_armor()
        return hero

    def build_teams(self):
        '''helper function for build_team_one and build_team_two'''
        # 1) Prompt the user for the name of the team (√)
        team_name = input("Name your team: ")
        # 2) Prompt the user for the number of Heroes on the team
        self.team_size = int(input("How many members are in your team? "))
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        built_team = Team(team_name)  # changed from built_team = []
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        count = 0
        while self.team_size > count:
            team_member = self.create_hero()
            count += 1
            built_team.add_hero(team_member)
        return built_team, self.team_size

    def build_team_one(self):
        self.team_one, self.team_one_size = self.build_teams()
        return self.team_one, self.team_one_size

    def build_team_two(self):
        self.team_two, self.team_two_size = self.build_teams()
        return self.team_two, self.team_two_size

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:
        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        #
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        #
        # TODO for each team, calculate the total kills and deaths for each
        # hero, find the average kills and deaths by dividing the totals by the
        # number of heroes.
        # finally, divide the average number of kills by the average number of
        # deaths for each team
        # show winning team
        team_one_points = 0
        team_two_points = 0
        for hero in self.team_one.heroes:
            if hero.is_alive():
                team_one_points += 1
                print(hero.name + " survived")
            else:
                print(hero.name + " was vanquished")
        for hero in self.team_two.heroes:
            if hero.is_alive():
                team_two_points += 1
                print(hero.name + " survived")
            else:
                print(hero.name + " was vanquished ")
        if team_one_points > team_two_points:
            print(self.team_one.name + " Wins")
        else:
            print(self.team_two.name + " Wins")
        # calculate average kills for each team, based on number of kills made
        # by each team member
        for hero in self.team_one.heroes:
            total_kills = 0
            total_kills += hero.kills
        avg_kills = total_kills // self.team_one_size
        print(self.team_one.name + " avg kills: " + str(avg_kills))
        for hero in self.team_two.heroes:
            total_kills = 0
            total_kills += hero.kills
        avg_kills = total_kills // self.team_two_size
        print(self.team_two.name + " avg kills: " + str(avg_kills))

        # calculate average deaths and show kill/death ratio
        for hero in self.team_one.heroes:
            total_deaths = 0
            total_deaths += hero.deaths
            avg_deaths = total_deaths // self.team_one_size
            print("Team 1 kill/death ratio: ")
            print(str(avg_kills) + "/" + str(avg_deaths))
        for hero in self.team_two.heroes:
            total_deaths = 0
            total_deaths += hero.deaths
            avg_deaths = total_deaths // self.team_two_size
            print("Team 2 kill/death ratio: ")
            print(str(avg_kills) + "/" + str(avg_deaths))
