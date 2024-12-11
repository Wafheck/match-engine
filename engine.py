### Football match engine

#Test Database
import random

ratingnoise = list(range(-10,11))
timeperiod = list(range(1, 11))
timechoice = list(range(1, 91))
timepicked = list()
percent = list(range(1, 101))

for i in timeperiod:
    chosentime = random.choice(timechoice)
    timechoice.remove(chosentime)
    timepicked.append(chosentime)
    timepicked.sort()
    print(timepicked)

t1attck = int(input("Enter team 1 attack: "))
t1mid = int(input("Enter team 1 midfield: "))
t1def = int(input("Enter team 1 defense: "))
t2attck = int(input("Enter team 2 attack: "))
t2mid = int(input("Enter team 2 midfield: "))
t2def = int(input("Enter team 2 defense: "))

t1rating = int((t1attck + t1mid + t1def)/ 3)
t2rating = int((t2attck + t2mid + t2def)/ 3)
noise1 = random.choice(ratingnoise)
noise2 = random.choice(ratingnoise)

print("Team 1 rating: " + str(t1rating))
print("Team 2 rating: " + str(t2rating))

t1rating += noise1
t2rating += noise2

print("Team 1 rating[with noise]: " + str(t1rating))
print("Team 2 rating[with noise]: " + str(t2rating))

t1score = 0
t2score = 0
advcoeff = 0
t1coeff = 0
t2coeff = 0

if t1rating >= t2rating:
    diff = t1rating - t2rating
    advcoeff = float((t2rating - diff)/(t1rating + t2rating))
    t1coeff = 1 - advcoeff
    t2coeff = advcoeff
    print("team 1 coefficient: " + str(t1coeff))
    print("team 2 coefficient: " + str(t2coeff))
    
elif t2rating > t1rating:
    diff = t2rating - t1rating
    advcoeff = float((t1rating - diff)/(t1rating + t2rating))
    t1coeff = advcoeff
    t2coeff = 1 - advcoeff
    print("team 1 coefficient: " + str(t1coeff))
    print("team 2 coefficient: " + str(t2coeff))
    
team1chances = int(round(t1coeff * 10))
team2chances = int(round(t2coeff * 10))
print("Team 1 chances: " + str(team1chances))
print("Team 2 chances: " + str(team2chances))

team1chances = list(range(1, team1chances + 1))
team2chances = list(range(1, team2chances + 1))

def team1attempt():
    global time
    global t1score
    chancerate = random.choice(range(-5,6))
    composerate = random.choice(range(-5,6))
    t1_adjusted_attack = max(0, min(99, t1attck + chancerate))
    t2_adjusted_defense = max(0, min(99, t2def + composerate))
    diff = t1_adjusted_attack - t2_adjusted_defense
    scrcoeff = max(0, min(1, 0.4 + diff / 100))
    scorechance = round(scrcoeff * 100)
    yesgoal = random.choice(percent)
    if yesgoal <= scorechance:
        t1score += 1
        print("Team 1 scored. (" + str(t1score) + " - " + str(t2score) + ") [" + str(time) + "\']")
    else:
        print("Team 1 missed. (" + str(t1score) + " - " + str(t2score) + ") [" + str(time) + "\']")
        
def team2attempt():
    global time
    global t2score
    chancerate = random.choice(range(-5,6))
    composerate = random.choice(range(-5,6))
    t2_adjusted_attack = max(0, min(99, t2attck + chancerate))
    t1_adjusted_defense = max(0, min(99, t1def + composerate))
    diff = t2_adjusted_attack - t1_adjusted_defense
    scrcoeff = max(0, min(1, 0.5 + diff / 100))
    scorechance = round(scrcoeff * 100)
    yesgoal = random.choice(percent)
    if yesgoal <= scorechance:
        t2score += 1
        print("Team 2 scored. (" + str(t1score) + " - " + str(t2score) + ") [" + str(time) + "\']")
    else:
        print("Team 2 missed. (" + str(t1score) + " - " + str(t2score) + ") [" + str(time) + "\']") 

for i in timepicked:
    global time
    time = i
    teampicker = random.choice([1, 2])
    print(teampicker)
    if teampicker == 1:
        if len(team1chances) > 0:
            team1chances.remove(random.choice(team1chances))
            print("Team 1 has a chance to score. [ " + str(time) + "\' ]")
            team1attempt()
        else:
            team2chances.remove(random.choice(team2chances))
            print("Team 2 has a chance to score. [ " + str(time) + "\' ]")
            team2attempt()
    else:
        if len(team2chances) > 0:
            team2chances.remove(random.choice(team2chances))
            print("Team 2 has a chance to score. [ " + str(time) + "\' ]")
            team2attempt()
        else:
            team1chances.remove(random.choice(team1chances))
            print("Team 1 has a chance to score. [ " + str(time) + "\' ]")
            team1attempt()
