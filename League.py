from math import *
from Team import *
from Player import *
from random import *
from Match import *

#from operator import itemgetter

class League():
    def __init__(self):
        self._teams = []
        self._matches = []
        self._ranking = []
        self._teamWins = {}
        self._league = [[]]

    def _setUpTeamWins(self):
        for i in self._teams:
            self._teamWins[i] = i.getWins()
            
    #Bad Efficiency Calculate Ranking
    def _calculateRanking(self):
        self._ranking.clear()
        self._setUpTeamWins()
        for i in range(len(self._teams)):
            itValues = iter(self._teamWins.values())
            itKeys = iter(self._teamWins.keys())
            currMaxWins = next(itValues)
            currMaxTeam = next(itKeys)
            for j in range(1,len(self._teamWins)):
                nextValue = next(itValues)
                nextTeam = next(itKeys)
                if nextValue == currMaxWins:
                    if nextTeam.getTotalGoals() > currMaxTeam.getTotalGoals():
                        currMaxWins = nextValue
                        currMaxTeam = nextTeam
                elif nextValue > currMaxWins:
                    currMaxWins = nextValue
                    currMaxTeam = nextTeam
            self._ranking.append(currMaxTeam)
            self._teamWins.pop(currMaxTeam)
        
    def addTeam(self, team):
        self._teams.append(team)

    def addMatch(self, match):
        self._calculateRanking()
        self._matches.append(match)
        self._teamWins.update({match.getTeam1(): match.getTeam1().getWins()})
        self._teamWins.update({match.getTeam2(): match.getTeam1().getWins()})
        
    def getRankings(self):
        if len(self._matches) == 0:
            self._calculateRanking()
        return self._ranking


######################Still in Development############################
    #Generate levels of the tournament and add teams to it
    def generateLeague(self):
        self._league * ceil((log(len(self._teams))/log(2)))
        temp = self._teams
        while temp != 0:
            if len(temp) == 1:
                team = temp.pop()
                self._league[0].append(Match(team, team))
                
            t1 = temp.pop(randint(0, len(temp)-1))
            t2 = temp.pop(randint(0, len(temp)-1))
            self._league[0].append(Match(t1,t2))
            


            

