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

lastInput = ""
didPlayerWin = None


def getComputerChoice():
    global computerChoice, lastInput, didPlayerWin

    bias = random.choice([True, False, True])

    if didPlayerWin == None:
        computerChoice = random.choice(["rock", "paper", "scissors"])
    elif bias:
        if didPlayerWin:
            if lastInput == "rock": computerChoice = "paper"
            elif lastInput == "paper": computerChoice = "scissors"
            elif  lastInput == "scissors": computerChoice = "rock"
        else:
            if lastInput == "rock": computerChoice = "rock"
            elif lastInput == "paper": computerChoice = "paper"
            elif lastInput == "scissors": computerChoice = "scissors"
    else:
        computerChoice = random.choice(["rock", "paper", "scissors"])
    

def choiceDisplay():
    global playerChoice, computerChoice
    playerChoiceDisplay.config(text=f"Your choice is:: {playerChoice}.")
    computerChoiceDisplay.config(text=f"Computer's choice is:: {computerChoice}.")
    stats.config(text=f"wins:: {wins}| losses:: {losses}| ties:: {ties}.")
    streaks.config(text=f"current streak:: {streak}| max streak:: {maxStreak}")

    
    rules.grid_forget()
    rpsBtnFrame.grid_forget()
    choiceWinDisplay.grid(row=4, column=0, pady=(20, 5))
    

def win():
    global result, wins, streak, maxStreak, didPlayerWin
    result = "win"
    didPlayerWin = True
    wins+=1
    streak+=1
    if streak > maxStreak: maxStreak = streak
    
def loss():
    global result, losses, streak, didPlayerWin
    result = "loss"
    didPlayerWin = False
    losses+=1
    streak = 0
    
def tie():
    global result, ties, didPlayerWin
    result = "tie"
    didPlayerWin = None
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
    global lastInput, playerChoice
    getComputerChoice()
    displayResult()
    lastInput = playerChoice
    
    choiceDisplay()
    againResetBtn.grid(row=5, column=0, pady=10)
    


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
    choiceWinDisplay.grid_forget()
    statsDisplay.grid_forget()
    againResetBtn.grid_forget()
    
    rules.grid(row=1, column=0, pady=6, sticky="ew")
    statsDisplay.grid(row=2, column=0, pady=10)
    rpsBtnFrame.grid(row=3, column=0, pady=20)
    
def reset(event=None):
    global wins, losses, ties, streak, maxStreak
    wins, losses, ties, streak, maxStreak = 0, 0, 0, 0, 0
    stats.config(text=f"wins:: {wins} | losses:: {losses} | ties:: {ties}.")
    streaks.config(text=f"current streak:: {streak} | max streak:: {maxStreak}")
    
    again()
    


FONT_TITLE  = ("Arial", 20, "bold")
FONT_NORMAL = ("Arial", 12)
FONT_BOLD   = ("Arial", 12, "bold")
FONT_SMALL  = ("Arial", 9)
FONT_BUTTON = ("Arial", 11, "bold")

COLOR_DEFAULT       = "#141472"
COLOR_BUTTON_HOVER  = "#e68e94"
COLOR_BUTTON        = "#79B1AD"
COLOR_BUTTON_TEXT   ="#110202"
COLOR_TEXT         = "#ECDCDC"


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("360x396")
root.minsize(300, 330)
root.resizable(True, True)
root.configure(bg=COLOR_DEFAULT)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

root.columnconfigure(0, weight=1)

title = tk.Label(
    root, 
    text="Rock Paper Scissors",
    font=FONT_TITLE,
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT
)
title.grid(row=0, column=0, pady=(20, 10), sticky="ew")

rules = tk.Label(  
    root, 
    text="rock beats scissors\nscissors beats paper\npaper beats rock",
    font=FONT_NORMAL,
    anchor="center",
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT
)
rules.grid(row=1, column=0, pady=6, sticky="ew")


statsDisplay = tk.Frame(root, bg=COLOR_DEFAULT)
statsDisplay.grid(row=2, column=0, pady=10)

stats = tk.Label(
    statsDisplay, 
    text = f"wins:: {wins} | losses:: {losses} | ties:: {ties}.",
    font=FONT_NORMAL,
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT
)
stats.pack()

streaks = tk.Label(
    statsDisplay, 
    text=f"current streak:: {streak} | max streak:: {maxStreak}",
    font=FONT_NORMAL,
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT
)
streaks.pack()


rpsBtnFrame = tk.Frame(root, bg=COLOR_DEFAULT)
rpsBtnFrame.grid(row=3, column=0, pady=20)

instructions = tk.Label(
    rpsBtnFrame, 
    text="please choose your next move",
    font=FONT_NORMAL,
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT
)
instructions.pack(pady=(0, 5))

tk.Button(  # rock btn
    rpsBtnFrame, 
    command=rock,
    text="rock", font=FONT_BUTTON,
    fg=COLOR_BUTTON_TEXT,
    bg=COLOR_BUTTON,
    activebackground=COLOR_BUTTON_HOVER,
    cursor="hand2", relief="flat",
    padx=12, pady= 6
).pack(side="left", padx=5)

tk.Button(  # paper btn
    rpsBtnFrame, 
    command=paper,
    text="paper", font=FONT_BUTTON,
    fg=COLOR_BUTTON_TEXT,
    bg=COLOR_BUTTON,
    activebackground=COLOR_BUTTON_HOVER,
    cursor="hand2", relief="flat",
    padx=12, pady=6
).pack(side="left", padx=5)

tk.Button(  # scissors btn
    rpsBtnFrame, 
    command=scissors,
    text="scissors", font=FONT_BUTTON,
    fg=COLOR_BUTTON_TEXT,
    bg=COLOR_BUTTON,
    activebackground=COLOR_BUTTON_HOVER,
    cursor="hand2", relief="flat",
    padx=12, pady=6
).pack(side="left", padx=5)


choiceWinDisplay = tk.Frame(root, bg=COLOR_DEFAULT)

playerChoiceDisplay = tk.Label(
    choiceWinDisplay, 
    text="", font=FONT_NORMAL,
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT
)
playerChoiceDisplay.pack(pady=(5,0))

computerChoiceDisplay = tk.Label(
    choiceWinDisplay, 
    text="", font=FONT_NORMAL,
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT
)
computerChoiceDisplay.pack(pady=(0, 10))

resultDisplay = tk.Label(
    choiceWinDisplay, 
    text="", font=FONT_BOLD,
    fg=COLOR_TEXT,
    bg=COLOR_DEFAULT
)
resultDisplay.pack()


againResetBtn = tk.Frame(root, bg=COLOR_DEFAULT)

tk.Button(  # again btn
    againResetBtn, 
    command=again,
    text="play again", font=FONT_BUTTON,
    fg=COLOR_BUTTON_TEXT,
    bg=COLOR_BUTTON,
    activebackground=COLOR_BUTTON_HOVER,
    cursor="hand2", relief="flat",
    padx=12, pady=6
).pack(side="left", padx=(10, 5), pady=6)
tk.Button(
    againResetBtn,
    command=reset,
    text="reset stats", font=FONT_BUTTON,
    fg=COLOR_BUTTON_TEXT,
    bg=COLOR_BUTTON,
    activebackground=COLOR_BUTTON_HOVER,
    cursor="hand2", relief="flat",
    padx=12, pady=6
).pack(side="left", padx=(5, 10), pady=6)

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
'''
2.2
implementet bias 
fixed some grammar-ish things within the code
'''
'''
2.2.1
made the windo resizable and the widgets to rescale them selves
'''

