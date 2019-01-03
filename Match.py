from Team import *

class Match():
    def __init__(self, team1, team2):
        self._team1 = team1
        self._team2 = team2
        self._winner = None
        self._score1 = 0
        self._score2 = 0

    def getTeam1(self):
        return self._team1

    def getTeam2(self):
        return self._team2
        
    def incrementTeamOneScore(self):
        self._score1 += 1

    def decrementTeamOneScore(self):
        self._score1 -= 1

    def incrementTeamTwoScore(self):
        self._score2 += 1
        
    def decrementTeamTwoScore(self):
        self._score2 -= 1
        
    def endMatch(self):
        self._team1.incrementTotalGoals(self._score1)
        self._team2.incrementTotalGoals(self._score2)
        if self._score1 == self._score2:
            self._score1 = 0
            self._score2 = 0
        elif self._score1 > self._score2:
            self._team1.incrementWins()
            self._team2.incrementLosses()
            self._winner = self._team1
        else:
            self._team2.incrementWins()
            self._team1.incrementLosses()
            self._winner = self._team2

    def getWinner(self):
        return self._winner

    def getScores(self):
        return (str(self._score1)+ ":"+str(self._score2))
