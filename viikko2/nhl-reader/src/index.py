import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
        self.get_json_data()

    def get_json_data(self):
        self.response = requests.get(self.url).json()

    def get_players(self):
        return [Player(
            player['name'],
            player['team'],
            player['nationality'],
            player['games'],
            player['goals'],
            player['assists']
        ) for player in self.response]

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        finnish_players = filter(lambda x: x.nationality == nationality, self.players)
        return sorted(
            finnish_players,
            key=lambda x: x.goals + x.assists,
            reverse=True
        )

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    players = reader.get_players()

    stats = PlayerStats(players)
    finnish_players = stats.top_scorers_by_nationality("FIN")

    for player in finnish_players:
        print(player)

if __name__ == "__main__":
    main()
