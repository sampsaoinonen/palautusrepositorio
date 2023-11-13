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

    for player in players:
        if player.nationality == "FIN":
            print(
                f"{player.name} team {player.team} goals {player.goals} assists {player.assists}"
            )


if __name__ == "__main__":
    main()
