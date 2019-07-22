import time
import random
import string
from random import randint
from random import choice, sample
import datetime
from datetime import datetime
import tkinter
from tkinter import *


def mainGame():
        #Subfunctions
        #customTimeDelay = input("Please input script delay according to taste. Input number between 0.1 - 5. (0.5 is recommended)")
        def callTime():
                today = datetime.today()
                todayCal = ('%s/%s/%s' % (today.month, today.day, today.year))
                todayClock = ('%s:%s:%s' % (today.hour, today.minute, today.second))
                print (todayCal)
                timeLapse()
                print(todayClock)
                timeLapse()
        def timeLapse():
            print("     ")
            time.sleep(0.5)

        def exceptionHandle():
                userAnswerCont = False
                while userAnswerCont == False:
                        print("Invalid Answer.")
                        timeLapse()
                        print("Please try again.")
                        timeLapse()
                        break
        def versionNumber():
            versionNumberVar = "0.2.2"
            print("Version" + versionNumberVar)
            print('Version number should be read as "MAJOR#.MINOR#.UPDATE#" ')
            timeLapse()

        def bugList():
            print("List of Known Bugs: ")
            print("#1 Selecting Paper is not handleing correctly. Paper does not cover Scissors.")
            print("#2 Entire program does not use classes appropriately.")
            timeLapse()


    #    ######------GUI SECTION---------#########
        #www.usingpython.com/using-tkinter/   used to help build section
        #Create a new window
     #   root = Tk()
        #Create a label widget called 'lbl'
      #  lbl = Label(root, text="Select your choice below")

      #  ent = Entry(root)

     #   btnrock = Button(root, text="Rock")
     #   btnscis = Button(root, text="Scissors")
    #    btnPape = Button(root, text="Paper")

        
        #Set window title
     #   root.title("RPS in Python")
        #Set the window size
      #  root.geometry("800x800")
        #Set the window icon
      #  root.wm_iconbitmap('RPS.ico')

     #   lbl.pack()
     #   ent.pack()
     #   btn.pack()
        #Draw the window, and start the 'application'
    #    root.mainloop()
        
#This is to generate a random numbers and letters to be put together for nonPlayer (bot name)------------------------------
        randomNumber1 = str((random.randint(0,9)))
        randomNumber2 = str((random.randint(0,9)))
        randomNumber3 = str((random.randint(0,9)))
        randomNumber4 = str((random.randint(0,9)))
        randomLetter1 = random.choice(string.ascii_uppercase)
        randomLetter2 = random.choice(string.ascii_lowercase)
        nonPlayer = randomLetter1 + randomLetter2 + randomNumber1 + randomNumber2 + randomNumber3 + randomNumber4
#Acquires username and play confirmation. --------------------------------------------------------------------------------
        callTime()
        versionNumber()
        bugList()
        confirmUsername = False
        while confirmUsername == False:
                userNameA = input("Welcome to Rock, Paper, Scissors! What is your name?  ")
                time.sleep(0.5)
                confirmUsername_A = input("Confirm '" + userNameA + "' as your username? Y/N   ")
                if confirmUsername_A.lower().startswith('y'):
                        confirmUsername = True
                elif confirmUsername_A.lower().startswith('n'):
                        confirmUsername = False
                else:
                        exceptionHandle()
        playGame = "y"
        while playGame == "y":
                timeLapse()
                print ("Hello, " + userNameA + ". My name is " + nonPlayer +". Are you ready to play?")
                timeLapse()
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
                                timeLapse()
                                break
                        
                        elif confirmGame.lower().startswith('y'):
                                print("Goodbye " + userNameA+".")
                                timeLapse()
                                print("Exiting in 3....")
                                timeLapse()
                                print("2..")
                                timeLapse()
                                print("1.")
                                timeLapse()
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
                print('Type "Dev" for Developer Commands *FOR DEVELOPER USE ONLY* or for cheating... Your call. ')
                print("Type EXIT to quit, RESET to reset scores or RESTART for a new game. ")
                print("    ")
                userAnswer = input("").lower()
                print("    ")
                #exit()


#If game is TIED
                if userAnswer.lower() == botAnswer.lower():
                        timeLapse()
                        print ("Tie!")
#If player chooses ROCK --------------------------------------------------------------------------
                elif userAnswer.lower().startswith("ro"):
                        if botAnswer == 'p':
                                timeLapse()
                                print ("You lose! " + 'Paper' + ' covers ' + 'rock' + "!")
                                botScore = botScore + 1
                        else:
                                timeLapse()
                                print ("You win! " + 'Rock' + ' smashes ' + 'scissors' + "!")
                                userScore = userScore + 1
#If player chooses PAPER -------------------------------------------------------------------------
                elif userAnswer.lower().startswith('pa'):
                        if botAnswer == 's':
                                timeLapse()
                                print("You lose! " + 'Scissors' + ' cut ' + 'paper' + "!")
                                botScore = botScore + 1
                        else:
                                timeLapse()
                                print("You win! " + 'Paper' + ' covers ' + 'scissors' + "!")
                                userScore = userScore + 1
#If player chooses SCISSORS ---------------------------------------------------------------------
                elif userAnswer.lower().startswith('sc'):
                        if botAnswer == 'r':
                                timeLapse()
                                print("You lose... " + 'Rock' + ' smashes ' + 'scissors' + "!")
                                botScore = botScore + 1
                        else:
                                timeLapse()
                                print("You win! " + 'Scissors ' +'cut ' + 'paper' + "!")
                                userScore = userScore + 1
#If player invokes EXIT command ----------------------------------------------------------------
                elif userAnswer.lower() == 'exit':
                                timeLapse()
                                print("Goodbye " + userNameA + "!" )
                                exit()
#TESTING-----------------------------------------------------------------------------------------                                

#This is to restart game, giving the option for new enemy, and to input new username. ----------
                elif userAnswer.lower() == 'restart':
                        timeLapse()
                        print ("RESTARTING....")
                        timeLapse()
                        mainGame()


#This is to RESET scores. ---------------------------------------------------------------------
                elif userAnswer.lower().startswith('reset'):
                        timeLapse()
                        print ("Score has been reset for both players.")
                        userScore = 0
                        botScore = 0
                        userAnswer = False



#Subtracts -1 to the opponent's score. For DEV purposes only and should not be displayed.-----
                elif userAnswer == 'minusb':
                        timeLapse()
                        print("One point subtracted from " + nonPlayer)
                        botScore = botScore -1

#Subtracts -1 to the player's score. For DEV purposes only and should not be displayed.-------
                elif userAnswer == 'minusp':
                        timeLapse()
                        print ("One point subtracted from " + userNameA)
                        userScore = userScore -1
#Adds +1 to opponent's score. For DEV purposes only and should not be displayed. -------------
                elif userAnswer == 'givve':
                        timeLapse()
                        print("One point added to " + nonPlayer)
                        timeLapse()
                        botScore = botScore + 1
#Adds +1 to player's score. For DEV purposes only and should not be displayed. --------------
                elif userAnswer == 'gimme':
                        timeLapse()
                        print("One point added to " + userNameA)
                        timeLapse()
                        userScore = userScore + 1
#Drops Player score to zero. For DEV purposes only and should not be displayed. ------------
                elif userAnswer == 'surrender':
                        timeLapse()
                        print("Your hand shakes as you give into the opponent's fury.")
                        userScore = 0
                        userAnswer = False
#Drops opponent score to zero. For DEV purposes only and should not be displayed. ---------
                elif userAnswer == 'nuke':
                        timeLapse()
                        print("Your opponent feels the heat of the bomb dropped.")
                        botScore = 0
                        userAnswer = False
#prints DEV commands. ---------------------------------------------------------------------
                elif userAnswer == 'dev':
                        timeLapse()
                        print("       ")
                        print("GIVVE ---- Adds one point to OPPONENT.")
                        print("GIMME ---- Adds one point to PLAYER.")
                        print("SURRENDER ---- Resets player score to ZERO.")
                        print("NUKE ---- Resets opponent score to ZERO.")
                        print("MINUSP --- Subtracts one point from PLAYER.")
                        print("MINUSB --- Subtracts one point from OPPONENT.")
                        print("      ")
                #callTime
                elif userAnswer.lower() == 'time':
                        callTime()
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
                        timeLapse()
                elif userScore >= botScore + (botScore * .5) and userScore >=3:
                        print (nonPlayer + " says: " + randDefeat)
                        timeLapse()
                else:
                        userAnswer = False
                        print("     ")

mainGame()

                









