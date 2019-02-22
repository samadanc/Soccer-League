from math import *
from Team import *
from Player import *
from random import *
from Match import *


class League():
    def __init__(self):
        self._teams = {}
        self._ranking = []
        self._league = [[]]
        self._next = []


    #Add teams to the league
    def addTeam(self, team):
        if team in self._teams:
            print("Team is already in the league")
        else:
            self._teams[team] = team.getWins() - team.getLosses()


    #Generate levels of the tournament and add teams to it
    def generateLeague(self):
        for i in range(ceil((log(len(self._teams))/log(2)))):
            self._league.append([False])
        self._league[0].append(False)
        #This false represents that this levels haven't been cleared
            
        temp = list(self._teams.keys())
        shuffle(temp)
        while len(temp) != 0:
            if len(temp) == 1:
                team = temp.pop()
                self._league[0].append(Match(team, team))
            elif len(temp) == 2:
                self._league[0].append(Match(temp.pop(),temp.pop()))
            else:
                t1 = temp.pop()
                t2 = temp.pop()
                self._league[0].append(Match(t1,t2))



    #Plays a level of the tournament starting from the bottom
    ## Account for draws later
    def playLevel(self):
        self._next.clear()
        for i in range(len(self._league)):
            if self._league[i][0] == False:
                play = self._league[i]
                nextLevel = i
                print("The matches for level ", i, " have begun.\n")
                break

        
        for i in range(1,len(play)):
            currentMatch = play[i]
            print("Match: ", i)
            print("Team 1: ", currentMatch.getTeam1().getName())
            print(" vs ")
            print("Team 2: ", currentMatch.getTeam2().getName(), "\n")

            #Need to make this more abstract, but for now the user enters the team no# to indicate a goal
            inp = int(input("Insert the team number to score a goal and -1 to end match: "))
            if inp == -1:
                currentMatch.endMatch()
                print("The winner of the match is: ", currentMatch.getWinner().getName())
                self._next.append(currentMatch.getWinner())
                self._teams[currentMatch.getTeam1()] = currentMatch.getTeam1().getWins() - currentMatch.getTeam1().getLosses()
                self._teams[currentMatch.getTeam2()] = currentMatch.getTeam2().getWins() - currentMatch.getTeam2().getLosses()
                
            else:
                while inp != -1:
                    if inp == 1:
                        currentMatch.incrementTeamOneScore()
                        inp = int(input("Insert the team number to score a goal and -1 to end match: "))
                    elif inp == 2:
                        currentMatch.incrementTeamTwoScore()
                        inp = int(input("Insert the team number to score a goal and -1 to end match: "))

                currentMatch.endMatch()
                self._teams[currentMatch.getTeam1()] = currentMatch.getTeam1().getWins() - currentMatch.getTeam1().getLosses()
                self._teams[currentMatch.getTeam2()] = currentMatch.getTeam2().getWins() - currentMatch.getTeam2().getLosses()
                print("The winner of the match is: ", currentMatch.getWinner().getName())
                self._next.append(currentMatch.getWinner())

        self._league[nextLevel][0] = True

    def generateNextLevel(self):
        for i in range(len(self._league)):
            if self._league[i][0] == False:
                nextLevel = i
                break
            
        while len(self._next) != 0:
            if len(self._next) == 1:
                team = self._next.pop()
                self._league[nextLevel].append(Match(team, team))
            elif len(self._next) == 2:
                self._league[nextLevel].append(Match(self._next.pop(),self._next.pop()))
            else:
                t1 = self._next.pop()
                t2 = self._next.pop()
                self._league[nextLevel].append(Match(t1,t2))
        

    #Calculates the ranking of the teams in the league
    def calculateRanking(self):
        self._ranking = sorted(self._teams.items(), key=lambda kv: kv[1])
        return self._ranking
    

                


                        

