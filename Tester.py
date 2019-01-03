from Team import *
from Player import *
from League import *
from Match import *

p1 = Player("Player1", "Mid-Fielder")
p2 = Player("Player2", "Defence")
p3 = Player("Player3", "Goal Keeper")
p4 = Player("Player4", "Striker")
p5 = Player("Player5", "Mid-Fielder")
p6 = Player("Player6", "Defence")
p7 = Player("Player7", "Striker")
p8 = Player("Player8", "Striker")
p9 = Player("Player9", "Mid-Fielder")
p10 = Player("Player10", "Defence")
p11 = Player("Player11", "Defence")
p12 = Player("Player12", "Striker", True)

ps1 = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
##ps2 = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
##ps3 = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
##ps4 = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
##ps5 = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]

t1 = Team("Team1", "coach1")
t2 = Team("Team2", "coach2")
t3 = Team("Team3", "coach3")
t4 = Team("Team4", "coach4")
t5 = Team("Team5", "coach5")

ts1 = [t1, t2, t3, t4, t5]

for i in range(12):
    t1.addPlayer(ps1[i])
    t2.addPlayer(ps1[i])
    t3.addPlayer(ps1[i])
    t4.addPlayer(ps1[i])
    t5.addPlayer(ps1[i])
    
l1 = League()

for i in ts1:
    l1.addTeam(i)

m1 = Match(t1, t2)
m1.incrementTeamOneScore()
m1.incrementTeamOneScore()
m1.incrementTeamTwoScore()
m1.incrementTeamTwoScore()
m1.incrementTeamTwoScore()
m1.endMatch()

m2 = Match(t3, t4)
m2.incrementTeamOneScore()
m2.incrementTeamOneScore()
m2.incrementTeamOneScore()
m2.incrementTeamTwoScore()
m2.endMatch()

m3 = Match(t3, t5)
m3.incrementTeamOneScore()
m3.incrementTeamOneScore()
m3.incrementTeamOneScore()
m3.incrementTeamTwoScore()
m3.incrementTeamTwoScore()
m3.incrementTeamTwoScore()
m3.endMatch()

m4 = Match(t2, t1)
m4.incrementTeamOneScore()
m4.incrementTeamTwoScore()
m4.incrementTeamTwoScore()
m4.incrementTeamTwoScore()
m4.endMatch()

ms1 = [m1, m2, m3, m4]

for i in ms1:
    l1.addMatch(i)

r4 = l1.getRankings()

for i in r4:
    print(i.getName())
##r = l1.getRankings()
##
##for i,j in r.iteritems():
##    print(i, ": ", j)



