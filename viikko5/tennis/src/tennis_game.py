class TennisGame:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):        
        if self.player1_score == self.player2_score:
            return self.even()        
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage_or_win()
        else:
            return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
    
    def even(self):
        if self.player1_score < 3:
            score_name = self.SCORE_NAMES.get(self.player1_score, "Deuce")
            return score_name + "-All"
        else:
            return "Deuce"
        
    def advantage_or_win(self):
        diff = self.player1_score - self.player2_score
        if diff == 1:
            return "Advantage player1"
        elif diff == -1:
            return "Advantage player2"
        elif diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
