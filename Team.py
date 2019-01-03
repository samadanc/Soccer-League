from Player import *

class Team():

    def __init__(self, name = "", coach_name = "", wins = 0, losses = 0):
        self._name = name
        self._coachName = coach_name
        self._wins = wins
        self._losses = losses
        self._totalGoals = 0
        self._players = []

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getTotalGoals(self):
        return self._totalGoals

    def incrementTotalGoals(self, goals):
        self._totalGoals += goals

    def setCoach(self, name):
        self._coachName = name

    def getCoach(self):
        return self._coachName
    
    def getWins(self):
        return self._wins

    def getLosses(self):
        return self._losses

    def setWins(self, wins):
        self._wins = wins

    def incrementWins(self):
        self._wins += 1

    def incrementLosses(self):
        self._losses += 1
         
    def setLosses(self, losses):
        self._losses = losses

    def rank(self):
        pass

    def setStrategy(self, strategy):
        pass

    def addPlayer(self, p):
        self._players.append(p)

    def removePlayer(self, p):
        for i in self._players:
            if i == p:
                self._players.remove(p)
    def getPlayers(self):
        return self._players


## Test##
##x = Team()
##print(x.getName())
##x.setName("Team1")
##print(x.getName())
##x.setCoach("Hammad")
##print(x.getCoach())
##print("Wins: ", x.getWins(), "Losses: ", x.getLosses())
##x.setWins(5)
##x.setLosses(4)
##print("Wins: ", x.getWins(), "Losses: ", x.getLosses())
