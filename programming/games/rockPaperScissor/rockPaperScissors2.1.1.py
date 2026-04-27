import tkinter as tk
import random
# 1. give instructions
playerChoice = ""
computerChoice = ""
result = ""

wins = 0
ties = 0
losses = 0
streak = 0
maxStreak = 0


def getComputerChoice():
    global computerChoice
    computerChoice = random.choice(["rock", "paper", "scissors"])
    

def choiceDisplay():
    global playerChoice, computerChoice
    playerChoiceDisplay.config(text=f"Youre choice is:: {playerChoice}.")
    computerChoiceDisplay.config(text=f"Computer choice is:: {computerChoice}.")
    stats.config(text=f"wins:: {wins}; losses:: {losses}; ties:: {ties}.")
    streaks.config(text=f"current streak:: {streak}; max streak;; {maxStreak}")

    
    rules.pack_forget()
    rpsBFrame.pack_forget()
    choiceWinDisplay.pack(pady=30)
    

def win():
    global result, wins, streak, maxStreak
    result = "win"
    wins+=1
    streak+=1
    if streak > maxStreak: maxStreak = streak
    
def loss():
    global result, losses, streak
    result = "loss"
    losses+=1
    streak = 0
    
def tie():
    global result, ties
    result = "tie"
    ties+=1    

def getResult():
    global result
    
    if playerChoice == "rock":
        if computerChoice == "rock": tie()
        elif computerChoice == "paper": loss()
        elif computerChoice == "scissors": win()
    elif playerChoice == "paper":
        if computerChoice == "rock": win()
        elif computerChoice == "paper": tie()
        elif computerChoice == "scissors": loss()
    elif playerChoice == "scissors":
        if computerChoice == "rock": loss()
        elif computerChoice == "paper": win()
        elif computerChoice == "scissors": tie()
        

def displayResult():
    global playerChoice, computerChoice, result
    
    getResult()
    if result =="tie": resultDisplay.config(text="Its a tie!")
    elif result == "loss": resultDisplay.config(text="You lost!")
    elif result == "win": resultDisplay.config(text="You win!")


def run():
    getComputerChoice()
    displayResult()
    
    choiceDisplay()
    againBtn.pack(pady=(0,5))
    resetBtn.pack(pady=(0,30))
    
    


def rock(event=None):
    global playerChoice
    playerChoice = "rock"
    run()

def paper(event=None):
    global playerChoice
    playerChoice = "paper"
    run()
    
def scissors(event=None):
    global playerChoice
    playerChoice = "scissors"
    run()

def again():
    againBtn.pack_forget()
    choiceWinDisplay.pack_forget()
    statsDisplay.pack_forget()
    resetBtn.pack_forget()
    
    rules.pack()
    statsDisplay.pack(pady=(15,0))
    rpsBFrame.pack(pady=30)
    
def reset(event=None):
    global wins, losses, ties, streak, maxStreak
    wins, losses, ties, streak, maxStreak = 0, 0, 0, 0, 0
    stats.config(text=f"wins:: {wins}; losses:: {losses}; ties:: {ties}.")
    streaks.config(text=f"current streak:: {streak}; max streak;; {maxStreak}")
    
    again()


root = tk.Tk()
root.title("My App")
root.minsize(250, 275)
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissores")
title.pack(pady=15)

rules = tk.Label(root, text="rock beats scissores\nscissores beats paper\npaper beats rock")
rules.pack()


statsDisplay = tk.Frame(root)
statsDisplay.pack(pady=(15,0))

stats = tk.Label(statsDisplay, text = f"wins:: {wins}; losses:: {losses}; ties:: {ties}.")
stats.pack()

streaks = tk.Label(statsDisplay, text=f"current streak:: {streak}; max streak;; {maxStreak}")
streaks.pack()


rpsBFrame = tk.Frame(root)
rpsBFrame.pack(pady=30)

instructions = tk.Label(rpsBFrame, text="pleas choose youre next move")
instructions.pack(pady=(0, 5))

rockBtn = tk.Button(rpsBFrame, text="rock", command=rock)
rockBtn.pack(side="left", padx=5)

paperBtn = tk.Button(rpsBFrame, text="paper", command=paper)
paperBtn.pack(side="left", padx=5)

scissorsBtn = tk.Button(rpsBFrame, text="scissores", command=scissors)
scissorsBtn.pack(padx=5)


choiceWinDisplay = tk.Frame(root)

playerChoiceDisplay = tk.Label(choiceWinDisplay, text="")
playerChoiceDisplay.pack(pady=(5,0))

computerChoiceDisplay = tk.Label(choiceWinDisplay, text="")
computerChoiceDisplay.pack(pady=(0, 10))

resultDisplay = tk.Label(choiceWinDisplay, text="")
resultDisplay.pack()

againBtn = tk.Button(root, text="play again", command=again)
resetBtn = tk.Button(root, text="reses stats", command=reset)

root.bind("<r>", rock)
root.bind("<p>", paper)
root.bind("<s>", scissors)

root.bind("<Control-r>", reset)

root.mainloop()


'''
2.0
Previous RPS game but now you can play it inside a dedicated window instead of the console.
'''
'''
2.1
your stats now get saved and displayed :)
'''
'''
2.1.1
you can now enter your inputs using key binds
'''