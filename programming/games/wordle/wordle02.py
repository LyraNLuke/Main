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
    "udder", "vault", "whirl", "exact", "yodel"
]

# Word definitions/hints — revealed progressively
HINTS = {
    "APPLE": ["A common fruit", "It grows on trees", "Often red, green, or yellow"],
    "BRAVE": ["An adjective describing courage", "Not afraid to face danger", "Synonyms: bold, daring"],
    "CRANE": ["It can be a bird or a machine", "Used on construction sites to lift heavy things", "The bird is known for its long neck"],
    "DRIFT": ["To move slowly and aimlessly", "Snow can do this in the wind", "A car technique used in motorsport"],
    "EAGLE": ["A large bird of prey", "National symbol of the USA", "Known for its sharp vision"],
    "FABLE": ["A short story with a moral", "Often features talking animals", "Aesop wrote many of these"],
    "GRACE": ["Elegance of movement", "Can also be a name", "Said before meals as a prayer of thanks"],
    "HASTE": ["Doing something too quickly", "'Make ___' means hurry up", "'___ makes waste' is a common proverb"],
    "IVORY": ["A creamy white colour", "Material from elephant tusks", "Heavily associated with the piano keys"],
    "JOKER": ["Someone who tells jokes", "A playing card with no suit", "Famous Batman villain"],
    "KNEEL": ["To go down on one knee", "A sign of respect or prayer", "Knights do this when being knighted"],
    "LEMON": ["A sour yellow citrus fruit", "Slang for a defective product", "Used to make a popular summer drink"],
    "MAPLE": ["A type of tree", "Canada is famous for its syrup", "Its leaf is on the Canadian flag"],
    "NOBLE": ["Of high moral character", "A member of the aristocracy", "Synonyms: honourable, distinguished"],
    "ORBIT": ["The path a planet takes around a star", "Also used for satellites around Earth", "To revolve around something"],
    "PLUME": ["A large feather", "A column of smoke rising upward", "Worn decoratively on helmets"],
    "QUEST": ["A long search or journey", "Common in fantasy stories and RPG games", "Knights went on these for holy relics"],
    "RAVEN": ["A large black bird", "Edgar Allan Poe wrote a famous poem about one", "Associated with mystery and darkness"],
    "STONE": ["A small rock", "A unit of weight used in the UK (14 lbs)", "Used to build castles and walls"],
    "TIGER": ["A large striped big cat", "Native to Asia", "The largest wild cat species"],
    "ULTRA": ["A prefix meaning extreme or beyond", "Used in 'ultraviolet' and 'ultrasound'", "Synonyms: extreme, maximum"],
    "VIGOR": ["Physical or mental strength", "Doing something with enthusiasm and energy", "Synonyms: vitality, energy"],
    "WALTZ": ["A type of ballroom dance", "Has a 3/4 time signature", "Originated in Austria and Germany"],
    "XENON": ["A chemical element", "A noble gas with symbol Xe", "Used in flash lamps and arc lamps"],
    "YACHT": ["A type of watercraft", "Associated with luxury and sailing", "Used for racing or leisure at sea"],
    "ZEBRA": ["A black and white striped animal", "Native to Africa", "Related to horses and donkeys"],
    "ALARM": ["A warning signal or device", "You set one to wake up in the morning", "Can be triggered by smoke or intruders"],
    "BLEND": ["To mix things together smoothly", "What a blender does to fruit", "A smooth combination of elements"],
    "CHEST": ["Part of your upper body", "A box used to store treasure", "Pirates are famous for burying these"],
    "DAISY": ["A small white flower", "A common name for a cow or a girl", "Often used in 'she loves me, she loves me not'"],
    "EIGHT": ["A number", "One more than seven", "An octopus has this many arms"],
    "FLINT": ["A hard type of rock", "Used to start fires by striking", "Also a city in Michigan, USA"],
    "GIANT": ["Something very large", "A mythical creature of enormous size", "'Jack and the Beanstalk' features one"],
    "HEART": ["The organ that pumps blood", "A symbol of love", "Located in the centre of your chest"],
    "INLET": ["A narrow body of water", "A small bay or indentation on a coastline", "Water flows into the land here"],
    "JUMBO": ["Meaning very large in size", "A famous elephant's name", "Used to describe oversized items like jets"],
    "KNACK": ["A special skill or talent", "A natural ability to do something well", "'He has a ___ for it' is a common phrase"],
    "LIGHT": ["The opposite of dark", "Also the opposite of heavy", "Travels at 299,792,458 metres per second"],
    "MANGO": ["A tropical fruit", "Orange and sweet inside", "Very popular in South and Southeast Asia"],
    "NIGHT": ["The opposite of day", "When the sun is below the horizon", "Stars are visible during this time"],
    "ONSET": ["The beginning of something", "Often used with illness or events", "'The ___ of winter' is a common phrase"],
    "PIANO": ["A musical instrument", "Has black and white keys", "One of the largest instruments you can play"],
    "QUEEN": ["A female monarch", "The most powerful piece in chess", "Also a famous British rock band"],
    "RIVER": ["A large natural stream of water", "Flows into a sea, lake, or ocean", "The Amazon is the world's largest by volume"],
    "SWIFT": ["Moving or happening quickly", "Also a type of bird", "Taylor ___ is a famous pop star"],
    "THORN": ["A sharp pointed growth on a plant", "Found on rose stems", "'No rose without a ___' is a proverb"],
    "UPSET": ["To feel unhappy or disturbed", "To overturn or knock over something", "A surprising defeat of a favourite in sport"],
    "VENOM": ["Poison produced by animals", "Injected by snakes and spiders", "Also a Marvel comic book character"],
    "WITCH": ["A person who practices magic", "Traditionally rides a broomstick", "Featured heavily in Halloween imagery"],
    "YEARN": ["To have a strong desire for something", "A deep longing or craving", "Synonyms: long, crave, pine"],
    "ZONAL": ["Relating to a zone or area", "Divided into distinct regions", "Used in geography and planning"],
    "ABIDE": ["To tolerate or accept", "To continue or remain", "'I cannot ___ rudeness' is an example use"],
    "BLOOM": ["A flower or to flower", "The period when flowers are open", "Also means to flourish or thrive"],
    "CLASP": ["To hold tightly", "A fastening device on jewellery or bags", "To grasp something firmly in your hand"],
    "DENSE": ["Closely packed together", "Also means slow to understand (informal)", "A ___ forest has very many trees"],
    "EJECT": ["To throw or push out forcefully", "A pilot does this from a plane in an emergency", "To remove a disc from a drive"],
    "FEAST": ["A large elaborate meal", "A celebration involving lots of food", "To eat a large amount with great enjoyment"],
    "GLOOM": ["Darkness or dim light", "A feeling of sadness or depression", "Synonyms: darkness, despair, melancholy"],
    "HAVEN": ["A safe place or refuge", "A harbour or port", "Synonyms: sanctuary, shelter, retreat"],
    "IRONY": ["When the opposite of what's expected happens", "A literary device used for humour or effect", "Saying 'great weather' during a storm is an example"],
    "JEWEL": ["A precious stone or gem", "A person or thing that is greatly valued", "Diamonds, rubies, and emeralds are examples"],
    "KNAVE": ["A dishonest or unscrupulous man", "An old-fashioned word for a rogue", "Also the Jack card in a deck of playing cards"],
    "LEAPT": ["Past tense of leap", "Jumped or sprang suddenly", "'She ___ over the puddle' is an example"],
    "MOOSE": ["The largest member of the deer family", "Native to North America and northern Europe", "Known for its large flat antlers"],
    "NAIVE": ["Lacking experience or judgement", "Too trusting or innocent", "Synonyms: gullible, innocent, unsophisticated"],
    "OCEAN": ["A vast body of salt water", "Covers over 70% of Earth's surface", "The Pacific is the largest of these"],
    "PLANK": ["A long flat piece of wood", "Used in construction and flooring", "Pirates made people 'walk the ___'"],
    "QUIRK": ["A strange habit or behaviour", "An unusual feature or characteristic", "Everyone has their own little ___s"],
    "ROBIN": ["A small bird with a red breast", "Common in European gardens", "Also a famous sidekick to Batman"],
    "SNARE": ["A trap for catching animals", "A type of drum", "To catch or trap something"],
    "TROUT": ["A freshwater fish", "Popular with anglers", "Often found in cold, clean rivers and lakes"],
    "UNITY": ["The state of being united", "Working together as one", "Synonyms: harmony, solidarity, togetherness"],
    "VIVID": ["Producing powerful feelings or images", "Intensely bright or strong in colour", "A ___ dream feels very real"],
    "WASTE": ["To use carelessly or inefficiently", "Unwanted material or rubbish", "'Haste makes ___' is a common proverb"],
    "EXPEL": ["To force someone to leave", "To push or drive out", "A student can be ___ from school for bad behaviour"],
    "YOUNG": ["Not old; early in life", "The opposite of old", "Children and babies are described as this"],
    "BLAZE": ["A large or fiercely burning fire", "To burn fiercely and brightly", "Also means to move very fast"],
    "CRISP": ["Firm and fresh, making a sharp sound", "A thin fried slice of potato (British English)", "A ___ autumn morning is cool and clear"],
    "DEPOT": ["A place for storing goods or vehicles", "A bus or train station", "A warehouse or storage facility"],
    "EMBER": ["A glowing piece of coal or wood in a dying fire", "Found in the remains of a campfire", "Plural: the smouldering remains of a fire"],
    "FROTH": ["A mass of small bubbles", "Found on top of a cappuccino", "To foam or produce bubbles"],
    "GLIDE": ["To move smoothly and effortlessly", "What birds and planes do without flapping or engines", "Synonyms: float, sail, drift"],
    "HERON": ["A large wading bird", "Often seen standing still at the edge of a river", "Has long legs and a long beak for catching fish"],
    "ICING": ["A sweet coating on a cake", "In hockey, shooting the puck across two lines", "Also called frosting in American English"],
    "JAZZY": ["Bright, colourful, and showy", "Relating to jazz music", "A ___ outfit stands out in a crowd"],
    "KARMA": ["The idea that good deeds lead to good outcomes", "A concept from Buddhism and Hinduism", "'What goes around comes around' captures this idea"],
    "LATCH": ["A fastening for a gate or door", "To fasten or close with a catch", "To ___ onto something means to grab and hold it"],
    "MERCY": ["Compassion shown to someone in your power", "Forgiveness rather than punishment", "'Have ___ on me' is a plea for forgiveness"],
    "NUDGE": ["A gentle push with the elbow", "To encourage someone subtly", "A ___ in the right direction is a gentle prompt"],
    "OLIVE": ["A small oval fruit, green or black", "Used to make a popular cooking oil", "Also a shade of yellow-green colour"],
    "PINCH": ["To squeeze tightly between fingers", "A very small amount of something", "'A ___ of salt' is a common cooking measurement"],
    "QUOTA": ["A fixed share or limit", "A target amount to be achieved", "Used in business, politics, and trade"],
    "REALM": ["A kingdom or domain", "A field or area of activity", "'In the ___ of possibility' is a common phrase"],
    "SCALP": ["The skin on the top of your head", "Where your hair grows from", "To ___ tickets means to resell them at inflated prices"],
    "THYME": ["A small herb used in cooking", "Commonly used in Mediterranean cuisine", "Sounds exactly like 'time'"],
    "UDDER": ["The milk-producing organ of a cow", "A bag-like organ found on female livestock", "Cows, goats, and sheep all have one"],
    "VAULT": ["A secure room for storing valuables", "An arched structure in architecture", "To jump over something using your hands or a pole"],
    "WHIRL": ["To spin or rotate rapidly", "A rapid spinning movement", "'Give it a ___' means to try something"],
    "EXACT": ["Perfectly accurate and correct", "Without any error or approximation", "Synonyms: precise, accurate, correct"],
    "YODEL": ["A style of singing with rapid changes in pitch", "Associated with Alpine regions like Switzerland", "Involves switching quickly between chest and head voice"],
}

DEFAULT_HINTS = [
    "It's a 5-letter English word",
    "Try common vowels: A, E, I, O, U",
    "Try common consonants: R, S, T, L, N"
]

# Colors for terminal output using ANSI codes
GREEN  = "\033[92m"   # Correct letter, correct position
YELLOW = "\033[93m"   # Correct letter, wrong position
GRAY   = "\033[90m"   # Letter not in word
CYAN   = "\033[96m"   # Hint colour
RESET  = "\033[0m"
BOLD   = "\033[1m"

MAX_GUESSES = 6
WORD_LENGTH = 5
MAX_HINTS   = 3  # Maximum hints per round

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pick_word():
    return random.choice(WORDS).upper()

def get_hints(word):
    """Return the list of hints for the given word."""
    return HINTS.get(word, DEFAULT_HINTS)

def display_header(score, streak, hints_used, hints_available):
    print(BOLD + "=" * 40 + RESET)
    print(BOLD + "        ♟  INFINITE WORDLE  ♟" + RESET)
    print(BOLD + "=" * 40 + RESET)
    print(f"  🏆 Score: {score}   🔥 Streak: {streak}")
    remaining_hints = hints_available - hints_used
    hint_display = CYAN + f"💡 Hints remaining: {remaining_hints}/{hints_available}" + RESET
    print(f"  {hint_display}")
    print("-" * 40)

def evaluate_guess(guess, target):
    result = []
    target_list = list(target)
    guess_list  = list(guess)
    colors = [""] * WORD_LENGTH

    for i in range(WORD_LENGTH):
        if guess_list[i] == target_list[i]:
            colors[i] = GREEN
            target_list[i] = None
            guess_list[i]  = None

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

    empty_rows = MAX_GUESSES - len(guesses_results)
    for _ in range(empty_rows):
        print("  " + "[   ]" * WORD_LENGTH)
    print()

def display_used_letters(used_letters):
    rows = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]
    print("  Keyboard:")
    for row in rows:
        line = "  "
        for letter in row:
            if letter in used_letters:
                color, _ = used_letters[letter]
                line += color + BOLD + f"[{letter}]" + RESET
            else:
                line += f"[{letter}]"
        print(line)
    print()

def display_hint(hints, hint_index):
    print()
    print(CYAN + BOLD + f"  💡 Hint {hint_index + 1}: " + RESET + CYAN + hints[hint_index] + RESET)
    print()

def play_round(round_num, score, streak):
    target = pick_word()
    hints  = get_hints(target)
    guesses_results = []
    used_letters    = {}
    hints_used      = 0
    won             = False

    while len(guesses_results) < MAX_GUESSES:
        clear_screen()
        display_header(score, streak, hints_used, MAX_HINTS)
        display_board(guesses_results, round_num)
        display_used_letters(used_letters)

        # Show all hints revealed so far
        for i in range(hints_used):
            display_hint(hints, i)

        guesses_left = MAX_GUESSES - len(guesses_results)
        hints_left   = MAX_HINTS - hints_used
        print(f"  Guesses left: {guesses_left}")

        if hints_left > 0:
            print(f"  Type 'hint' for a clue ({hints_left} remaining), or enter your guess:")
        else:
            print("  Enter your guess:")

        user_input = input("  > ").strip().upper()

        if user_input == "HINT":
            if hints_used < MAX_HINTS:
                hints_used += 1
                input(CYAN + f"  💡 Hint {hints_used}: {hints[hints_used - 1]}" + RESET + "\n  (Press Enter to continue...)")
            else:
                input("  No hints remaining! Press Enter to continue...")
            continue

        if len(user_input) != WORD_LENGTH or not user_input.isalpha():
            input(f"  ⚠  Please enter a valid {WORD_LENGTH}-letter word. Press Enter to continue...")
            continue

        result = evaluate_guess(user_input, target)
        guesses_results.append(result)

        # Track best colour per letter for the keyboard display
        priority = {GREEN: 3, YELLOW: 2, GRAY: 1}
        for letter, color in result:
            if letter not in used_letters or priority[color] > priority[used_letters[letter][0]]:
                used_letters[letter] = (color, letter)

        if user_input == target:
            won = True
            break

    # Final screen
    clear_screen()
    display_header(score, streak, hints_used, MAX_HINTS)
    display_board(guesses_results, round_num)
    display_used_letters(used_letters)

    if won:
        guesses_taken = len(guesses_results)
        points = max(1, MAX_GUESSES - guesses_taken + 1)  # Fewer guesses = more points
        # Deduct a point per hint used
        points = max(1, points - hints_used)
        new_score  = score + points
        new_streak = streak + 1
        print(GREEN + BOLD + f"  🎉 Correct! The word was {target}." + RESET)
        print(f"  +{points} points (hint penalty: -{hints_used})  |  Streak: {new_streak}")
    else:
        new_score  = score
        new_streak = 0
        print(GRAY + BOLD + f"  ❌ Out of guesses! The word was: {target}" + RESET)
        print("  Streak reset to 0.")

    print()
    input("  Press Enter for the next word...")
    return new_score, new_streak

def main():
    score  = 0
    streak = 0
    round_num = 1

    clear_screen()
    print(BOLD + "=" * 40 + RESET)
    print(BOLD + "        ♟  INFINITE WORDLE  ♟" + RESET)
    print(BOLD + "=" * 40 + RESET)
    print()
    print("  Guess the 5-letter word in 6 tries.")
    print(f"  Type 'hint' to reveal a clue (max {MAX_HINTS} per round).")
    print("  Hints reduce your score for that round.")
    print()
    print("  " + GREEN + BOLD + "[G]" + RESET + " = Right letter, right spot")
    print("  " + YELLOW + BOLD + "[Y]" + RESET + " = Right letter, wrong spot")
    print("  " + GRAY + BOLD + "[X]" + RESET + " = Letter not in word")
    print()
    input("  Press Enter to start...")

    while True:
        score, streak = play_round(round_num, score, streak)
        round_num += 1

if __name__ == "__main__":
    main()
