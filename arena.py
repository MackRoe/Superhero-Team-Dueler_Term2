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
