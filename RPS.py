import time
import random
import string
from random import randint
from random import choice, sample

def mainGame():
        #subfunctions
        def exceptionHandle():
                userAnswerCont = False
                while userAnswerCont == False:
                        print("Invalid Answer.")
                        time.sleep(0.5)
                        print("Please try again.")
                        time.sleep(.5)
                        break
                
                                
#This is to generate a random numbers and letters to be put together for nonPlayer (bot name)------------------------------
        randomNumber1 = str((random.randint(0,9)))
        randomNumber2 = str((random.randint(0,9)))
        randomNumber3 = str((random.randint(0,9)))
        randomNumber4 = str((random.randint(0,9)))
        randomLetter1 = random.choice(string.ascii_uppercase)
        randomLetter2 = random.choice(string.ascii_lowercase)
        nonPlayer = randomLetter1 + randomLetter2 + randomNumber1 + randomNumber2 + randomNumber3 + randomNumber4


#Acquires username and play confirmation. --------------------------------------------------------------------------------
        userNameA = input("Welcome to Rock, Paper, Scissors! What is your name?  ").lower()
        playGame = "y"
        while playGame == "y":
                time.sleep(0.5)
                print ("Hello, " + userNameA + ". My name is " + nonPlayer +". Are you ready to play?")
                time.sleep(0.5)
                confirmGame = input("Y/N?    ")
                if confirmGame.lower().startswith("y"):
                        print ("Then let us begin " + userNameA + ".")
                        print("     ")
                        break
                elif confirmGame.lower().startswith('n'):
                        confirmExit = input("Are you sure?")
                        if confirmExit.lower().startswith('n'):
                                print("Alright, then let us continue.")
                                print("           ")
                                time.sleep(0.5)
                                continue
                        
                        elif confirmGame.lower().startswith('y'):
                                print("Goodbye " + userNameA+".")
                                time.sleep(0.5)
                                print("Exiting in 3....")
                                time.sleep(0.5)
                                print("2..")
                                time.sleep(0.5)
                                print("1.")
                                time.sleep(0.5)
                                exit()
                        else:
                                exceptionHandle()
                        
                else:
                        exceptionHandle()
                


                                                



#Create list of play options
        rpsList = ['r',"p","s"]
#Comment lists for random comments when a certain perimeter is met.
        tauntList = ["You can do better than that can't you?", "This is a disgraceful game. I thought you'd be better than this.", \
                                        "I can stop destroying you, all you have to do is QUIT.", "Really, Are you this bad?"]
                                                

        defeatList = ["Who do you think you are?","You must be cheating", "Can't you give a bot a break?",\
                                        "Seriously, your hurting my feelings.","You can't win like this forever."]
        randTaunt = random.choice(tauntList)
        randDefeat = random.choice(defeatList)

#creates bot answer as well as sets the userAnswer variable to False as to have loop iteration control.

        botAnswer = rpsList[randint(0,2)].lower()
        userAnswer = False

#This will be the options settings. Still in development.



#Score variables.
        userScore = 0
        botScore = 0
#invokes game loop using previous userAnswer variable
        while userAnswer == False:

                time.sleep(0.5)
#set player to TRUE
                print("Type Rock, Paper, or Scissors to play!")
                print("Type EXIT to quit, RESET to reset scores or RESTART for a new game. ")
                print("    ")
                userAnswer = input("").lower()
                print("    ")
                #exit()


#If game is TIED
                if userAnswer.lower() == botAnswer.lower():
                        time.sleep(0.5)
                        print ("Tie!")
#If player chooses ROCK --------------------------------------------------------------------------
                elif userAnswer.lower().startswith("ro"):
                        if botAnswer == 'p':
                                time.sleep(0.5)
                                print ("You lose! " + 'Paper' + ' covers ' + 'rock' + "!")
                                botScore = botScore + 1
                        else:
                                time.sleep(0.5)
                                print ("You win! " + 'Rock' + ' smashes ' + 'scissors' + "!")
                                userScore = userScore + 1
#If player chooses PAPER -------------------------------------------------------------------------
                elif userAnswer.lower().startswith('pa'):
                        if botAnswer == 's':
                                time.sleep(0.5)
                                print("You lose! " + 'Scissors' + ' cut ' + 'paper' + "!")
                                botScore = botScore + 1
                        else:
                                time.sleep(0.5)
                                print("You win! " + 'Paper' + ' covers ' + 'scissors' + "!")
                                userScore = userScore + 1
#If player chooses SCISSORS ---------------------------------------------------------------------
                elif userAnswer.lower().startswith('sc'):
                        if botAnswer == 'r':
                                time.sleep(0.5)
                                print("You lose... " + 'Rock' + ' smashes ' + 'scissors' + "!")
                                botScore = botScore + 1
                        else:
                                time.sleep(0.5)
                                print("You win! " + 'Scissors ' +'cut ' + 'paper' + "!")
                                userScore = userScore + 1
#If player invokes EXIT command ----------------------------------------------------------------
                elif userAnswer.lower() == 'exit':
                                time.sleep(0.5)
                                print("Goodbye " + userNameA + "!" )
                                exit()
#TESTING-----------------------------------------------------------------------------------------                                

#This is to restart game, giving the option for new enemy, and to input new username. ----------
                elif userAnswer.lower() == 'restart':
                        time.sleep(0.5)
                        print ("RESTARTING....")
                        time.sleep(0.5)
                        mainGame()


#This is to RESET scores. ---------------------------------------------------------------------
                elif userAnswer.lower().startswith('reset'):
                        time.sleep(0.5)
                        print ("Score has been reset for both players.")
                        userScore = 0
                        botScore = 0
                        userAnswer = False



#Subtracts -1 to the opponent's score. For DEV purposes only and should not be displayed.-----
                elif userAnswer == 'minusb':
                        time.sleep(0.5)
                        print("One point subtracted from " + nonPlayer)
                        botScore = botScore -1

#Subtracts -1 to the player's score. For DEV purposes only and should not be displayed.-------
                elif userAnswer == 'minusp':
                        time.sleep(0.5)
                        print ("One point subtracted from " + userNameA)
                        userScore = userScore -1
#Adds +1 to opponent's score. For DEV purposes only and should not be displayed. -------------
                elif userAnswer == 'givve':
                        time.sleep(0.5)
                        print("One point added to " + nonPlayer)
                        time.sleep(0.5)
                        botScore = botScore + 1
#Adds +1 to player's score. For DEV purposes only and should not be displayed. --------------
                elif userAnswer == 'gimme':
                        time.sleep(0.5)
                        print("One point added to " + userNameA)
                        time.sleep(1)
                        userScore = userScore + 1
#Drops Player score to zero. For DEV purposes only and should not be displayed. ------------
                elif userAnswer == 'surrender':
                        time.sleep(0.5)
                        print("Your hand shakes as you give into the opponent's fury.")
                        userScore = 0
                        userAnswer = False
#Drops opponent score to zero. For DEV purposes only and should not be displayed. ---------
                elif userAnswer == 'nuke':
                        time.sleep(0.5)
                        print("Your opponent feels the heat of the bomb dropped.")
                        botScore = 0
                        userAnswer = False
#prints DEV commands. ---------------------------------------------------------------------
                elif userAnswer == 'dev':
                        time.sleep(0.5)
                        print("       ")
                        print("GIVVE ---- Adds one point to OPPONENT.")
                        print("GIMME ---- Adds one point to PLAYER.")
                        print("SURRENDER ---- Resets player score to ZERO.")
                        print("NUKE ---- Resets opponent score to ZERO.")
                        print("MINUSP --- Subtracts one point from PLAYER.")
                        print("MINUSB --- Subtracts one point from OPPONENT.")
                        print("      ")
#This is to catch spelling errors, and give the option to quit. ---------------------------
                else:
                        exceptionHandle()
 

#Resets loops conditions as well as creates new bot answer.------------------------------
                userAnswer = False
                botAnswer = rpsList[randint(0,2)]
#PRINTS both scores ------------
                print (userNameA + ":" + str(userScore) + "    " + nonPlayer + ":" + str(botScore))
                print("     ")
                time.sleep(1)

####This is to randomly select from list of comments. 
                randTaunt = random.choice(tauntList)
                randDefeat = random.choice(defeatList)

                if botScore >= userScore + (userScore * .5) and botScore >= 3:
                        print (nonPlayer + " says: " + randTaunt)
                        time.sleep(1)
                elif userScore >= botScore + (botScore * .5) and userScore >=3:
                        print (nonPlayer + " says: " + randDefeat)
                        time.sleep(1)
                else:
                        userAnswer = False
                        print("     ")






mainGame()


#######----------- FUTURE FEATURES -------------------------------------------------------------------------------------------------------------------------------------
                #SETTINGS MENU that will change the nature of the game when accessed. Game will default to normal settings if not invoked.
                #Options to choose BEST OUT OF THREE, BEST OUT OF TEN, UNLIMITED, or 1 ROUND.
                #Option to keep highschore on unlimited setting using locally stored text file?
                #Option to choose 1, 2, 3, or Arrow keys to correlate with rock paper or scissors
                #Optional TIE = DIE mode where tieing in game causes score to either RESET or subtract from both players.
                #TUG OF WAR gamemode where TIEING causes you to steal the opponent's current score.
                
                









