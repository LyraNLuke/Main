import random
import os

# Word list for the game
WORDS = [
    "apple", "brave", "crane", "drift", "eagle", "fable", "grace", "haste",
    "ivory", "joker", "kneel", "lemon", "maple", "noble", "orbit", "plume",
    "quest", "raven", "stone", "tiger", "ultra", "vigor", "waltz", "xenon",
    "yacht", "zebra", "alarm", "blend", "chest", "daisy", "eight", "flint",
    "giant", "heart", "inlet", "jumbo", "knack", "light", "mango", "night",
    "onset", "piano", "queen", "river", "swift", "thorn", "upset", "venom",
    "witch", "yearn", "zonal", "abide", "bloom", "clasp", "dense", "eject",
    "feast", "gloom", "haven", "irony", "jewel", "knave", "leapt", "moose",
    "naive", "ocean", "plank", "quirk", "robin", "snare", "trout", "unity",
    "vivid", "waste", "expel", "young", "zesty", "blaze", "crisp", "depot",
    "ember", "froth", "glide", "heron", "icing", "jazzy", "karma", "latch",
    "mercy", "nudge", "olive", "pinch", "quota", "realm", "scalp", "thyme",
    "udder", "vault", "whirl", "exact", "yodel", "zircon"[:-2]
]

# Colors for terminal output using ANSI codes
GREEN  = "\033[92m"   # Correct letter, correct position
YELLOW = "\033[93m"   # Correct letter, wrong position
GRAY   = "\033[90m"   # Letter not in word
RESET  = "\033[0m"
BOLD   = "\033[1m"

MAX_GUESSES = 6
WORD_LENGTH = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pick_word():
    return random.choice(WORDS).upper()

def display_header(score, streak):
    print(BOLD + "=" * 40 + RESET)
    print(BOLD + "        ♟  INFINITE WORDLE  ♟" + RESET)
    print(BOLD + "=" * 40 + RESET)
    print(f"  🏆 Score: {score}   🔥 Streak: {streak}")
    print("-" * 40)

def evaluate_guess(guess, target):
    """
    Returns a list of (letter, color) tuples for the guess.
    Green = correct position, Yellow = wrong position, Gray = not in word.
    """
    result = []
    target_list = list(target)
    guess_list  = list(guess)
    colors = [""] * WORD_LENGTH

    # First pass: find greens
    for i in range(WORD_LENGTH):
        if guess_list[i] == target_list[i]:
            colors[i] = GREEN
            target_list[i] = None  # Mark as used
            guess_list[i]  = None

    # Second pass: find yellows
    for i in range(WORD_LENGTH):
        if guess_list[i] is not None:
            if guess_list[i] in target_list:
                colors[i] = YELLOW
                target_list[target_list.index(guess_list[i])] = None
            else:
                colors[i] = GRAY

    for i in range(WORD_LENGTH):
        result.append((guess[i], colors[i]))

    return result

def display_board(guesses_results, current_round):
    print(f"\n  Round {current_round}")
    print()
    for result in guesses_results:
        row = "  "
        for letter, color in result:
            row += color + BOLD + f"[ {letter} ]" + RESET
        print(row)

    # Print empty rows for remaining guesses
    empty_rows = MAX_GUESSES - len(guesses_results)
    for _ in range(empty_rows):
        print("  " + "[ _ ]" * WORD_LENGTH)
    print()

def display_keyboard(used_letters):
    """Show a simple keyboard with color-coded used letters."""
    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    print("  Keyboard:")
    for row in rows:
        line = "  "
        for ch in row:
            if ch in used_letters:
                line += used_letters[ch] + BOLD + ch + RESET + " "
            else:
                line += ch + " "
        print(line)
    print()

def get_guess(attempt_num, used_letters, guesses_results, score, streak, current_round):
    while True:
        clear_screen()
        display_header(score, streak)
        display_board(guesses_results, current_round)
        display_keyboard(used_letters)
        print(f"  Attempt {attempt_num} of {MAX_GUESSES}")
        guess = input("  Enter your 5-letter guess: ").strip().upper()

        if len(guess) != WORD_LENGTH:
            print(f"  ⚠  Please enter exactly {WORD_LENGTH} letters.")
            input("  Press Enter to try again...")
        elif not guess.isalpha():
            print("  ⚠  Only alphabetical characters allowed.")
            input("  Press Enter to try again...")
        else:
            return guess

def play_round(score, streak, current_round):
    target      = pick_word()
    guesses_results = []
    used_letters    = {}
    won             = False

    for attempt in range(1, MAX_GUESSES + 1):
        guess = get_guess(attempt, used_letters, guesses_results, score, streak, current_round)
        result = evaluate_guess(guess, target)
        guesses_results.append(result)

        # Update used letters for keyboard display
        for letter, color in result:
            # Prioritise green > yellow > gray
            existing = used_letters.get(letter, GRAY)
            if color == GREEN:
                used_letters[letter] = GREEN
            elif color == YELLOW and existing != GREEN:
                used_letters[letter] = YELLOW
            elif color == GRAY and letter not in used_letters:
                used_letters[letter] = GRAY

        if guess == target:
            won = True
            clear_screen()
            display_header(score, streak)
            display_board(guesses_results, current_round)
            print(GREEN + BOLD + f"  🎉 Brilliant! You guessed '{target}' in {attempt} attempt(s)!" + RESET)
            score  += (MAX_GUESSES - attempt + 1) * 10  # Bonus for fewer attempts
            streak += 1
            print(f"  +{(MAX_GUESSES - attempt + 1) * 10} points!  🔥 Streak: {streak}")
            break

    if not won:
        clear_screen()
        display_header(score, streak)
        display_board(guesses_results, current_round)
        print(GRAY + BOLD + f"  💀 Out of guesses! The word was: {target}" + RESET)
        streak = 0  # Reset streak on loss

    input("\n  Press Enter to play the next word...")
    return score, streak

def main():
    score         = 0
    streak        = 0
    current_round = 1

    clear_screen()
    print(BOLD + "=" * 40 + RESET)
    print(BOLD + "     Welcome to INFINITE WORDLE!" + RESET)
    print(BOLD + "=" * 40 + RESET)
    print("""
  HOW TO PLAY:
  • Guess the 5-letter word in 6 tries.
  • After each guess, letters are coloured:
    """ + GREEN + BOLD + "GREEN" + RESET + """  = right letter, right place
    """ + YELLOW + BOLD + "YELLOW" + RESET + """ = right letter, wrong place
    """ + GRAY + BOLD + "GRAY" + RESET + """   = letter not in the word
  • Guess correctly to earn points!
  • The game never ends — keep playing!
    """)
    input("  Press Enter to start...")

    # Infinite game loop — a new word is drawn after each round
    while True:
        score, streak = play_round(score, streak, current_round)
        current_round += 1

main()