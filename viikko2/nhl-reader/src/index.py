import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['nationality'],
            player_dict['games'],
            player_dict['goals'],
            player_dict['assists']
        )
        players.append(player)
    
    print("Players from FIN\n")

    finnish_players = [player for player in players if player.nationality == "FIN"]

    sort_finnish_players = sorted(
        finnish_players,
        key=lambda i: i.goals + i.assists,
        reverse=True
    )

    for player in sort_finnish_players:
        print(
            f"{player.name:20} {player.team} {player.goals} + {player.assists} = {player.goals + player.assists}"
        )



if __name__ == "__main__":
    main()
