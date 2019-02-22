from League import *
from Match import *
from Player import *
from Team import *


############# Player Class Test Area #################
p1 = Player()
p2 = Player()
p3 = Player("Cristiano Ronaldo", "Center", False)
p4 = Player("Lionel Messi", "Striker", True)

p1.setName("Paul Pogba")
p2.setName("Kylian Mbappe")

p1.setPosition("Left Back")
p2.setPosition("Goal Keeper")

p1.setSubstitute(True)
p2.setSubstitute(False)

p = [p1, p2, p3, p4]

for i in p:
    print("Name: ", i.getName())
    print("Position: ", i.getPosition())
    print("Substitute: ", i.isSubstitute(), "\n")



############# Team Class Test Area ####################




############# Match Class Test Area #####################



############# League Class Test Area ###########
t1 = Team("Team1", "coach1")
t2 = Team("Team2", "coach2")
t3 = Team("Team3", "coach3")
t4 = Team("Team4", "coach4")
t5 = Team("Team5", "coach5")

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

ts1 = [t1, t2, t3, t4, t5]

l1 = League()

for i in ts1:
    l1.addTeam(i)

l1.addTeam(t1) ##Error checking :D

l1.generateLeague()

l1.playLevel()
l1.generateNextLevel()
l1.playLevel()
l1.generateNextLevel()
l1.playLevel()

print(l1.calculateRanking())

