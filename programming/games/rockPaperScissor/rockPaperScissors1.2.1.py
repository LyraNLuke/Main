import random
import pyttsx3

# 1. give instructions

print("You are about to play a game of rock paper scissors. \nThe rules are simple.\n\npaper beats rock;\nrock beats scissors;\nscissors beats paper.\n")

streak = 0
maxStreak = 0
wins = 0
losses = 0
ties = 0
lastInput = ""
didPlayerWin = None

# 2. generate player input

def getPlayerPick():
    global lastInput, streak, maxStreak, wins, losses, ties, didPlayerWin

    playerPick = str(input("Pleas input 'r' for rock, 'p' for paper or 's' for scissors:: "))
    playerPick = playerPick.lower().strip()
    if playerPick.__contains__("b") or playerPick.__contains__("stop"):
        return "b"
    
    if playerPick == "reset": 
        lastInput == ""
        streak = 0
        maxStreak = 0
        wins = 0
        losses = 0
        ties = 0
        didPlayerWin = None
        print("Stats resettet. New game starts.")
        return getPlayerPick()
    
    if playerPick == "": return lastInput
    
    if playerPick.__contains__("rock"): return "r"
    elif playerPick.__contains__("paper"): return "p"
    elif playerPick.__contains__("scissors"): return "s"
    elif playerPick.__contains__("r"): return "r" 
    elif playerPick.__contains__("p"): return "p"
    elif playerPick.__contains__("s"): return "s"
    else:
        print("Invalid input")
        return getPlayerPick()

# game logic

def speak(text: str):
    engine = pyttsx3.init()  # ✅ Move init inside the function
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def loss():
    global streak, losses, didPlayerWin

    print ("\nYou lose. :(")
    streak = 0
    losses += 1
    didPlayerWin = False
    speak("You lost!")


def win():
    global streak, wins, didPlayerWin

    print ("\nYou win! :)")
    streak += 1
    wins += 1
    didPlayerWin = True
    
    speak("You winn!")


def tie():
    global ties, didPlayerWin

    print("\nIts a Tie!")
    ties += 1
    didPlayerWin = None
    speak("Its a Tie!")
    


def getComputerChoice():
    global lastInput, didPlayerWin

    bias = random.choice([True, False, True])

    if didPlayerWin == None:
        return random.choice(["r", "p", "s"])
    elif bias:
        if didPlayerWin:
            if lastInput == "r": return "p"
            elif lastInput == "p": return "s"
            elif  lastInput == "s": return "r"
        else:
            if lastInput == "r": return "r"
            elif lastInput == "p": return "p"
            elif lastInput == "s": return "s"
    else:
        return random.choice(["r", "p", "s"])
    

def game(): 
    global lastInput, streak, maxStreak, wins, ties, losses

    print(f"Win streak :: {streak} | Max win streak :: {maxStreak}")
    print(f"Wins :: {wins} | Losses :: {losses} | Ties :: {ties}")

    playerPick = getPlayerPick()
    if playerPick == "b": return
    lastInput = playerPick

    computerChoice = getComputerChoice()

    choices=[["r", "Rock"],["p", "Paper"],["s","Scissors"]]

    for item in choices:
        if playerPick == item[0]:
            print (f"Your choice is :: {item[1]}.")

    for item in choices:
        if computerChoice == item[0]:
            print (f"The computer chose :: {item[1]}")

    # print(f"Computer choice = {computerChoice}\n")

    if playerPick == "r":
        if computerChoice == "r":
            tie()
        elif computerChoice == "p":
            loss()
        elif computerChoice == "s":
            win()
    elif playerPick == "p":
        if computerChoice == "r":
            win()
        elif computerChoice == "p":
            tie()
        elif computerChoice == "s":
            loss()
    elif playerPick == "s":
        if computerChoice == "r":
            loss()
        elif computerChoice == "p":
            win()
        elif computerChoice == "s":
            tie()

    if streak > maxStreak: maxStreak = streak

    print("\nIf you want to play again just enter your next choice.\nTo stop playing enter 'b' or 'stop'.\n")
    game()

game()


'''
v1.0
A fully working  game of rock paper scissors.
Anny input will automatically be filtered for anny valid input
    ig. the written out words will be filtered first
        if that doesnt yield a valid input it will check for the starting letters of the words
        rock will be prioritized over paper over scissors.
The Ai choses at full random and has no bias.
After one game is over you can imediatly start the next without anny delay.
'''
'''
v1.1
Added the options to see ones over all wins, losses and ties.
as well as ones win streaks.
Also added the feture to play with the same pick by leaving the input blank.
'''
'''
v1.2
added bias to allow the player to use some degree of stratagie.
'''
'''
v1.2.1
added a voice agent that tels you the result.
'''

