import random
# 1. give instructions

print("You are about to play a game of rock paper scissors. \nThe rules are simple.\n\npaper beats rock;\nrock beats scissors;\nscissors beats paper.\n")

# 2. generate player input

def getPlayerPick():
    playerPick = str(input("Pleas input 'r' for rock, 'p' for paper or 's' for scissors:: "))
    playerPick = playerPick.lower().strip()
    if playerPick.__contains__("b") or playerPick.__contains__("stop"):
        return "b"
    
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

def game():
    playerPick = getPlayerPick()
    if playerPick == "b": return


    computerChoice = random.choice(["r", "p", "s"])

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
            print("Its a tie!")
        elif computerChoice == "p":
            print("You lose. :(")
        elif computerChoice == "s":
            print("You win! :)")
    elif playerPick == "p":
        if computerChoice == "r":
            print("You won! :)")
        elif computerChoice == "p":
            print("Its a tie!")
        elif computerChoice == "s":
            print("You lose. :(")
    elif playerPick == "s":
        if computerChoice == "r":
            print("You lose. :(")
        elif computerChoice == "p":
            print("You win! :)")
        elif computerChoice == "s":
            print("Its a tie!")

    print("\nIf you want to play again just enter your next choice.\nTo stop playing enter 'b' or 'stop'.\n")
    game()

game()

