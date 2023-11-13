class Player:
    def __init__(self, name, team, nationality, games, goals, assists):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.games = games
        self.goals = goals
        self.assists = assists

    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"
