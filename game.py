import random
from time import sleep

#player class to keep all the info
class Player():
    """ Keeps the of player name and it's score! """

    def __init__(self, name):
        self.name=name
        self.score=0

    def increase(self):
        self.score+=1

    def current(self):
        return self.score

    def __str__(self):
        return f"{self.name} has {self.score} points! "

#computer class to keep the track of the score of computer
class Computer():
    """ Keeps the track of the computer's score """
    def __init__(self):
        self.score=0

    def increase(self):
        self.score+=1

    def current(self):
        return self.score

    def __str__(self):
        return f"Computer has {self.score} points! "

#return the option chose on the basis of number
def option(number):
    """ Return the name of the weapon chose :P :P """
    if number==1:
        return "ROCK"

    elif number ==2:
        return "PAPER"

    elif number ==3:
        return "SCISSORS"

    else:
        return -1

#checks who won the round
def battle(no_pc, no_person,i):
    """ Logic of Rock, Paper and Scissors  """

    flag=1
    if no_pc == no_person:
        player.increase()
        computer.increase()
        flag=0

    #pc
    elif no_pc==1:
        if no_person==2:
            player.increase()
            flag=1

        elif no_person==3:
            computer.increase()
            flag=-1

    #pc
    elif no_pc==2:
        if no_person==1:
            computer.increase()
            flag=-1

        elif no_person==3:
            player.increase()
            flag=1

    #pc
    elif no_pc==3:
        if no_person==1:
            player.increase()
            flag=1

        elif no_person==2:
            computer.increase()
            flag=-1

    #player
    elif no_person==1:
        if no_pc==2:
            computer.increase()
            flag=-1

        elif no_pc==3:
            player.increase()
            flag=1

    #player
    elif no_person==2:
        if no_pc==1:
            player.increase()
            flag=1

        elif no_pc==3:
            computer.increase()
            flag=-1

    #player
    elif no_person==3:
        if no_pc==1:
            computer.increase()
            flag=-1

        elif no_pc==2:
            player.increase()
            flag=1

    """ Return who won the Round """
    if flag==1:
        return f"{player.name} won the round {i}!"

    elif flag==-1:
        return f"Computer won the round {i}!"

    elif flag==0:
        return f"It's a TIE! Both are awarded 1 point!"


""" Body of the program """
def main():
    name=None

print("""
                    WELCOME TO THE GAME OF THE ROCK, PAPER AND SCISSORS!!!
                        Press the following keys to choose:

                            1 --->  ROCK
                            2 --->  PAPER
                            3 --->  SCISSORS


                    ****    MATCH IS OF 5 POINTS    ****
                    ****      FIRST TO 5 WINS       ****
""")

sleep(5)

#player enter ther name
while True:
    name=input("Enter your Name: ")
    confirm=input("Enter 'y' to confirm 'r' to re-enter and 'exit' to exit: ")

    if confirm.lower() =="y":
        break

    elif confirm.lower() == "r":
        continue

    elif confirm.lower() == "exit":
        exit()

#creating player and computer class
player=Player(name)
computer=Computer()

no_person=None
no_pc=None
i=1

while True:
    """ Getting option, checking who won and printing round results  """
    print(f"This is Round {i}!")
    sleep(2)

    while True:
        try:
            no_person=int(input("Choose ROCK, PAPER OR SCISSORS: "))
            if no_person in range(1,4):
                break

            else:
                print("Choose value in between 1 and 3")
                continue
        except:
            print("Choose value in between 1 and 3")
            continue
                
    weapon=option(no_person)
    print(f"You chose {weapon}!")

    sleep(1)

    no_pc=random.randint(1,3)
    weapon=option(no_pc)
    print(f"Computer chose {weapon}!")

    sleep(2)

    winner=battle(no_pc, no_person,i)

    print(f"{winner}\n")

    sleep(1)
    pc_now=computer.current()
    player_now=player.current()


    sleep(2)
    print()
    print(f"""Current score

                {player.name} : {player_now}
                Computer : {pc_now} 
    """)

    sleep(2)

    if player_now >= 5 and pc_now>=5:
        print("It's GAME POINT Round!")

    elif player_now>=5:
        print(f"Congratulations! {player.name}. You won the match!")
        exit()

    elif pc_now>=5:
        print(f"{player.name} better luck next time!")
        exit()

    i+=1
    sleep(2)
    
    print()
    print()

#calling in the main program
main()


"""  Author: Deepanshu Narang
     Command Line Based Game
"""
