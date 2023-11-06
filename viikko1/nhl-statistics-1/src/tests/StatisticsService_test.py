import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_correct_player(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_for_unknown_player(self):
        player = self.stats.search("Jeejeejepppis")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        players = self.stats.team("COL")        
        self.assertTrue(all(player.team == "COL" for player in players))
    
    def test_team_returns_empty_list_for_unknown_team(self):
        players = self.stats.team("Jeppiiss")
        self.assertEqual(len(players), 0)
    
    def test_top_returns_players_in_order(self):
        top_players = self.stats.top(3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_return_by_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual([player.name for player in top_players], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_returns_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual([player.name for player in top_players], ["Lemieux", "Yzerman", "Kurri"])

    def test_top_returns_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual([player.name for player in top_players], ["Gretzky", "Yzerman", "Lemieux"])

    def test_top_returns_by_points(self):
        top_players = self.stats.top(3)
        self.assertEqual([player.name for player in top_players], ["Gretzky", "Lemieux", "Yzerman"])

