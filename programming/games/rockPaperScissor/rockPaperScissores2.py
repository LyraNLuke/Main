import tkinter as tk
import random
# 1. give instructions
playerChoice = ""
computerChoice = ""
result = ""

def getComputerChoice():
    global computerChoice
    computerChoice = random.choice(["rock", "paper", "scissors"])
    

def choiceDisplay():
    global playerChoice, computerChoice
    playerChoiceDisplay.config(text=f"Youre choice is:: {playerChoice}.")
    computerChoiceDisplay.config(text=f"Computer choice is:: {computerChoice}.")
    
    rules.pack_forget()
    rpsBFrame.pack_forget()
    choiceWinDisplay.pack(pady=30)
    
    
def getResult():
    global result
    
    if playerChoice == "rock":
        if computerChoice == "rock": result = "tie"
        elif computerChoice == "paper": result = "loss"
        elif computerChoice == "scissores": result = "win"
    elif playerChoice == "paper":
        if computerChoice == "rock": result = "win"
        elif computerChoice == "paper": result = "tie"
        elif computerChoice == "scissors": result = "loss"
    elif playerChoice == "scissors":
        if computerChoice == "rock": result = "loss"
        elif computerChoice == "paper": result = "win"
        elif computerChoice == "scissors": result = "tie"
        

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
    againBtn.pack(pady=(0,30))
    


def rock():
    global playerChoice
    playerChoice = "rock"
    run()

def paper():
    global playerChoice
    playerChoice = "paper"
    run()
    
def scissors():
    global playerChoice
    playerChoice = "scissors"
    run()

def again():
    againBtn.pack_forget()
    choiceWinDisplay.pack_forget()
    
    rules.pack()
    rpsBFrame.pack(pady=30)


root = tk.Tk()
root.title("My App")
root.minsize(250, 275)
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissores")
title.pack(pady=15)

rules = tk.Label(root, text="rock beats scissores\nscissores beats paper\npaper beats rock")
rules.pack()


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

againBtn = tk.Button(root, text="reset", command=again)

root.mainloop()


'''
2.0
Previous RPS game but now you can play it inside a dedicated window instead of the console.
'''
