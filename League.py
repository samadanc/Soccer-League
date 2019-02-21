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
        for i in self._league:
            i.insert(0, False)   #This false represents that this levels hasn't been cleared
        temp = self._teams
        while temp != 0:
            if len(temp) == 1:
                team = temp.pop()
                self._league[0].append(Match(team, team))
                
            t1 = temp.pop(randint(0, len(temp)-1))
            t2 = temp.pop(randint(0, len(temp)-1))
            self._league[0].append(Match(t1,t2))


    #Plays a level of the tournament starting from the bottom
    def playLevel(self):
        for i in self._league:
            if i[0] == False:
                play = i
                print("The matches for level ", i, " have begun.\n")
                break

        
        for i in range(len(play)):
            currentMatch = play[i]
            print("Match: ", i+1)
            print("Team 1: ", currentMatch.getTeam1())
            print(" vs \n","Team 2: ", currentMatch.getTeam2, "\n")

            #Need to make this more abstract, but for now the user enters the team no# to indicate a goal
            inp = input("Insert the team number to score a goal and -1 to end match: ")
            if inp == -1:
                currentMatch.endMatch()
                print("The winner of the match is: ", currentMatch.getWinner())

            else:
                while inp != -1:
                    if inp == 1:
                        currentMatch.incrementTeamOneScore()
                        inp = input("Insert the team number to score a goal and -1 to end match: ")
                    elif inp == 2:
                        currentMatch.incrementTeamTwoScore()
                        inp = input("Insert the team number to score a goal and -1 to end match: ")

                currentMatch.endMatch()
                print("The winner of the match is: ", currentMatch.getWinner())
                
                
                        

