#TODO: Add support for scoring module

import random

class Game(object):
    """Game class compares two teams ratings to determine which team is better.
    The higher rated team is declared as winner and returned.
    Scoring property also prints a projected score for the game.
    Scoring defaults to False, as it is only used for the championship game.
    """
    # TODO: refactor scoring to use season's scores for teams and historical
    # TODO: scores for matchups between these two teams
    def __init__(self, team1, team2, scoring=False):
        self.team1 = team1
        self.team2 = team2
        self.winner = None
        self.scoring = scoring
        self.play()

    def play(self):
        if self.team1.rating > self.team2.rating:
            self.winner = self.team1
        elif self.team1.rating < self.team2.rating:
            self.winner = self.team2
        else:
            self.winner = random.choice([self.team1, self.team2])

        print("%s\n\t >  %s\n%s\n" %
              (self.team1.name, self.winner.name, self.team2.name))
        if self.scoring:
            score = (71, 65)
            print("Projected score: %d - %d" % (score[0], score[1]))
        return self.winner
