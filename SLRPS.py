# Özerali Burkaz 21831088
import random

class Delikanlı:
    def __init__(self, name, spock, lizard, rock, paper, scissors, health):
        self.__name = name
        self.__spockprob = spock
        self.__lizardprob = lizard
        self.__rockprob = rock
        self.__paperprob = paper
        self.__scissorsprob = scissors
        self.__health = health
    def __str__(self):
        myman = self.__name+" is here!"
        return(myman)
    def checkhealth(self):
        return self.__health
    def whichone(self):
        prob = random.randint(1, 100)
        if prob <= self.__spockprob*100 :
            return "Spock"
        elif prob <= self.__spockprob*100+self.__lizardprob*100 :
            return "Lizard"
        elif prob <= self.__spockprob*100+self.__lizardprob*100+self.__rockprob*100 :
            return "Rock"
        elif prob <= self.__spockprob*100+self.__lizardprob*100+self.__rockprob*100+self.__paperprob*100 :
            return "Paper"
        elif prob <= self.__spockprob*100+self.__lizardprob*100+self.__rockprob*100+self.__paperprob*100+self.__scissorsprob :
            return "Scissors"


# class Feynman(Delikanlı):
#     def __init__(self, name="Feynman", spock=0.20, lizard=0.20, rock=0.20, paper=0.20, scissors=0.20, health=100):
#         Delikanlı.__init__(self,name,spock,lizard,rock,paper,scissors,health)
# class Curie(Delikanlı):
#     def __init__(self, name="Curie", spock=0.35, lizard=0.35, rock=0.10, paper=0.10, scissors=0.10, health=90):
#         Delikanlı.__init__(self,name,spock,lizard,rock,paper,scissors,health)
# class Schrodinger(Delikanlı):
#     def __init__(self, name="Schrödinger", spock=0.10, lizard=0.35, rock=0.35, paper=0.10, scissors=0.10, health=80):
#         Delikanlı.__init__(self,name,spock,lizard,rock,paper,scissors,health)
# class Dirac(Delikanlı):
#     def __init__(self, name="Dirac", spock=0.10, lizard=0.10, rock=0.35, paper=0.35, scissors=0.10, health=70):
#         Delikanlı.__init__(self,name,spock,lizard,rock,paper,scissors,health)
# class Newton(Delikanlı):
#     def __init__(self, name="Newton", spock=0.10, lizard=0.10, rock=0.10, paper=0.35, scissors=0.35, health=60):
#         Delikanlı.__init__(self,name,spock,lizard,rock,paper,scissors,health)
# class Pauli(Delikanlı):
#     def __init__(self, name="Pauli", spock=0.35, lizard=0.10, rock=0.10, paper=0.10, scissors=0.35, health=50):
#         Delikanlı.__init__(self,name,spock,lizard,rock,paper,scissors,health)

# def Showmaze(list):
#     print(list[0:9])
#     print(list[9:18])     #IT IS NOT WORKING, SO I COULD NOT USE IT AND DID NOT CONTINUE CODING.WE ARE GOING TO TRY A SIMPLE LIST.
#     print(list[18:27])
#     print(list[27:36])
#     print(list[36:45])
#     print(list[45:54])
#     print(list[54:63])
#     print(list[63:72])
#     print(list[72:81])
#
#
# def Progress():
#     # 0 = UNREACHABLE POINT
#     # 1 = STARTING POINT
#     # OTHERS = EMPTY CELL
#     # 44 = ENDING POINT
#     maze =  [[0], [1], [2], [3], [0], [4], [5], [6],[0],
#             [10],[11],[12],[13],[14],[15],[16],[17],[18],
#             [20],[21],[22],[23],[24],[25],[26],[27],[28],
#             [30],[31],[32],[33],[34],[35],[36],[37],[38],
#             [0], [41],[42],[43],[44],[45],[46],[47],[0],
#             [50],[51],[52],[53],[54],[55],[56],[57],[58],
#             [60],[61],[62],[63],[64],[65],[66],[67],[68],
#             [70],[71],[72],[73],[74],[75],[76],[77],[78],
#             [0], [81],[82],[83],[0],[84],[85],[86],[0]]
#     startingp = [1,2,3,5,6,7,9,18,27,45,54,63,17,26,35,53,62,71,73,74,75,77,78,79]
#     a = random.choice(startingp)
#     print("You will start here man >>"+ str(maze[a]))
#     Showmaze(maze)
#     maze[a] = ["H"] #4 is you.
#     for i in range(1,2) :
#         print("YOU HAVE TO REACH 44 LETS GO")
#         wayinput = input("Type the first letter of which direction you want to go(up,down,left,right)>>>")
#         if wayinput == "u" or "U":
#             if maze[1] == maze[a] or maze[2] == maze[a] or maze[3] == maze[a] or maze[5] == maze[a] or maze[6] == maze[a] or maze[7] == maze[a] or maze[9] == maze[a] or maze[18] == maze[a] or maze[27] == maze[a] or maze[36] == maze[a] or maze[45] == maze[a] or maze[54] == maze[a] or maze[63] == maze[a] or maze[17] == maze[a] or maze[26] == maze[a] or maze[35] == maze[a] or maze[44] == maze[a] or maze[53] == maze[a] or maze[62] == maze[a] or maze[71] == maze[a] :
#                 print("You cannot go up!")
#                 Showmaze(maze)
#             else :
#                 maze[a] = maze[a-10]
#                 maze[a] = ["H"]
#                 Showmaze(maze)
#         elif wayinput == "d" or "D":
#             if maze[9] == maze[a] or maze[18] == maze[a] or maze[27] == maze[a] or maze[36] == maze[a] or maze[45] == maze[a] or maze[54] == maze[a] or maze[63] == maze[a] or maze[17] == maze[a] or maze[26] == maze[a] or maze[35] == maze[a] or maze[44] == maze[a] or maze[53] == maze[a] or maze[62] == maze[a] or maze[71] == maze[a] or maze[73] == maze[a] or maze[74] == maze[a] or maze[75] == maze[a] or maze[77] == maze[a] or maze[78] == maze[a] or maze[79] == maze[a] :
#                 print("You cannot go down!")
#                 Showmaze(maze)
#             else :
#                 maze[a] = maze[a+10]
#                 maze[a] = ["H"]
#                 Showmaze(maze)
#         elif wayinput == "l" or "L":
#             if maze[1] == maze[a] or maze[2] == maze[a] or maze[3] == maze[a] or maze[5] == maze[a] or maze[6] == maze[a] or maze[7] == maze[a] or maze[9] == maze[a] or maze[18] == maze[a] or maze[27] == maze[a] or maze[36] == maze[a] or maze[45] == maze[a] or maze[54] == maze[a] or maze[63] == maze[a] or maze[73] == maze[a] or maze[74] == maze[a] or maze[75] == maze[a] or maze[77] == maze[a] or maze[78] == maze[a] or maze[79] == maze[a] :
#                 print("You cannot go left!")
#                 Showmaze(maze)
#             else :
#                 maze[a] = maze[a-1]
#                 maze[a] = ["H"]
#                 Showmaze(maze)
#         elif wayinput == "r" or "R":
#             if maze[1] == maze[a] or maze[2] == maze[a] or maze[3] == maze[a] or maze[5] == maze[a] or maze[6] == maze[a] or maze[7] == maze[a] or maze[17] == maze[a] or maze[26] == maze[a] or maze[35] == maze[a] or maze[44] == maze[a] or maze[53] == maze[a] or maze[62] == maze[a] or maze[71] == maze[a] or maze[73] == maze[a] or maze[74] == maze[a] or maze[75] == maze[a] or maze[77] == maze[a] or maze[78] == maze[a] or maze[79] == maze[a] :
#                 print("You cannot go right")
#                 Showmaze(maze)
#             else :
#                 maze[a] = maze[a+1]
#                 maze[a] = ["H"]
#                 Showmaze(maze)

hero_health = 200

delikanlı_list = [Delikanlı("Feynman",0.20,0.20,0.20,0.20,0.20,100),Delikanlı("Curie",0.35,0.35,0.10,0.10,0.10,90),
                  Delikanlı("Schrödinger",0.10,0.35,0.35,0.10,0.10,80),Delikanlı("Dirac",0.10,0.10,0.35,0.35,0.10,70),
                  Delikanlı("Newton",0.10,0.10,0.10,0.35,0.35,60),Delikanlı("Pauli",0.35,0.10,0.10,0.10,0.35,50)]
b = random.choice(delikanlı_list)
def play_game(b,hero_health):
    deli_health = b.checkhealth()
    while deli_health > 0 and hero_health >0: #Game
        hero_input = input("Spock,Lizard,Rock,Paper,Scissors,choose one of them and enter it exactly as typed>>>")
        deli_choice = b.whichone()
        if hero_input == "Spock" and deli_choice == "Spock":
            print("Draw!")
            continue
        elif hero_input == "Spock" and deli_choice == "Paper":
            hero_health -=50
        elif hero_input == "Spock" and deli_choice == "Rock":
            deli_health -= 50
        elif hero_input == "Spock" and deli_choice == "Lizard":
            hero_health -=50
        elif hero_input == "Spock" and deli_choice == "Scissors":
            deli_health -=50
        elif hero_input == "Rock" and deli_choice == "Rock":
            print("Draw!")
            continue
        elif hero_input == "Rock" and deli_choice == "Spock":
            hero_health -=50
        elif hero_input == "Rock" and deli_choice == "Lizard":
            deli_health -= 50
        elif hero_input == "Rock" and deli_choice == "Paper":
            hero_health -=50
        elif hero_input == "Rock" and deli_choice == "Scissors":
            deli_health -=50
        elif hero_input == "Paper" and deli_choice == "Paper":
            print("Draw!")
            continue
        elif hero_input == "Paper" and deli_choice == "Spock":
            deli_health -=50
        elif hero_input == "Paper" and deli_choice == "Rock":
            deli_health -= 50
        elif hero_input == "Paper" and deli_choice == "Lizard":
            hero_health -=50
        elif hero_input == "Paper" and deli_choice == "Scissors":
            hero_health -=50
        elif hero_input == "Scissors" and deli_choice == "Scissors":
            print("Draw!")
            continue
        elif hero_input == "Scissors" and deli_choice == "Lizard":
            deli_health -=50
        elif hero_input == "Scissors" and deli_choice == "Spock":
            deli_health -= 50
        elif hero_input == "Scissors" and deli_choice == "Rock":
            hero_health -=50
        elif hero_input == "Scissors" and deli_choice == "Paper":
            deli_health -=50
        elif hero_input == "Lizard" and deli_choice == "Lizard":
            print("Draw!")
            continue
        elif hero_input == "Lizard" and deli_choice == "Spock":
            deli_health -=50
        elif hero_input == "Lizard" and deli_choice == "Rock":
            hero_health -= 50
        elif hero_input == "Lizard" and deli_choice == "Paper":
            deli_health -=50
        elif hero_input == "Lizard" and deli_choice == "Scissors":
            hero_health -=50
        print("Your HP- ",hero_health,">>>","Delikanlıs HP-",deli_health)
    if deli_health < 0:
        hero_health = hero_health - (deli_health)
    if hero_health <= 0:
        print("REQUIESCAT IN PACE AMIGO!NOTHING IS TRUE,EVERYTHING IS PERMITTED")
    if hero_health > 0 and startingp != 44:
        print("Bravo you won this one but,do not trust your fortune everytime")

    global hero_newhealth
    hero_newhealth = hero_health

all_cells = [11,12,13,15,16,17,21,31,51,61,71,72,73,75,76,77,67,57,37,27,14,22,23,24,25,26,32,33,34,35,36,41,42,43,44,45,46,47,52,53,54,55,56,61,62,63,64,65,66,74]
startingcells = [11,12,13,15,16,17,21,31,51,61,71,72,73,75,76,77,67,57,37,27]
startingtop = [12,13,14,15,16]
startingdown = [72,73,74,75,76]
startingleft = [21,31,41,51,61]
startingright = [27,37,47,57,67]

startingp = random.choice(startingcells)
print("You are here now >>",startingp,".You have to reach cell 44 to win!")
print(b,"Prepare for SLRPS battle")
if b.checkhealth() == 100:
    print("I was born not knowing and have had only a little time to change that here and there.")
    print("")
elif b.checkhealth() == 90:
    print("Be less curious about people and more curious about ideas.")
    print("")
elif b.checkhealth() == 80:
    print("The present is the only things that has no end.")
    print("")
elif b.checkhealth() == 70:
    print("Pick a flower on Earth and you move the farthest star.")
    print("")
elif b.checkhealth() == 60:
    print("I can calculate the motion of heavenly bodies, but not the madness of people.")
    print("")
elif b.checkhealth() == 50:
    print("I do not mind if you think slowly, but I do object when you publish more quickly than you think.")
    print("")
play_game(b,hero_health)

while startingp != 44 and hero_newhealth > 0:
    if startingp == 11:
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "U":
            print("You can not go up man.")
        elif move == "D":
            startingp += 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "R":
            print("You can not go right man.")
        elif move == "L":
            startingp -= 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    elif startingp == 17:
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "U":
            print("You can not go up man.")
        elif move == "D":
            startingp += 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "R":
            print("You can not go right man.")
        elif move == "L":
            startingp -= 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    elif startingp == 71:
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "D":
            print("You can not go down man.")
        elif move == "U":
            startingp -= 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "L":
            print("You can not go left man.")
        elif move == "R":
            startingp += 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    elif startingp == 77:
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "D":
            print("You can not go down man.")
        elif move == "U":
            startingp -= 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "L":
            print("You can not go left man.")
        elif move == "R":
            startingp += 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    elif startingp in startingtop :
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "U":
            print("You can not go up man.")
        elif move == "D":
            startingp += 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "R":
            startingp += 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "L":
            startingp -= 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    elif startingp in startingdown :
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "D":
            print("You can not go down man.")
        elif move == "U":
            startingp -= 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "R":
            startingp += 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "L":
            startingp -= 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    elif startingp in startingleft :
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "L":
            print("You can not go left man.")
        elif move == "D":
            startingp += 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "R":
            startingp += 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "U":
            startingp -= 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    elif startingp in startingright :
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "R":
            print("You can not go right man.")
        elif move == "U":
            startingp -= 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "L":
            startingp -= 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "D":
            startingp += 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    else :
        move= input("Choose a direction to move: (U-D-L-R) ")
        if move == "R":
            startingp += 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "U":
            startingp -= 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "L":
            startingp -= 1
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
        elif move == "D":
            startingp += 10
            print(b)
            print("You are here now>>>", startingp)
            play_game(b,hero_newhealth)
    if hero_newhealth > 0:
        print("You are here now >>", startingp)
if startingp == 44 and hero_health > 0:
    print("Awesome! You surprised me. Congratulations YOU WON!")













