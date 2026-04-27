# Maze Game - Find the Exit!
# Navigate through the maze using W/A/S/D keys to find the exit (E)

import os
import sys
import random

# Maze layout:
# '#' = Wall
# ' ' = Open path
# 'P' = Player
# 'E' = Exit

def create_maze():
    """Create a predefined maze layout"""
    maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'P', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 'E', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    return maze

def find_position(maze, char):
    """Find the position of a character in the maze"""
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == char:
                return r, c
    return None

def display_maze(maze, moves):
    """Display the maze in the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 35)
    print("        🧩  MAZE GAME  🧩")
    print("=" * 35)
    print("  Find the Exit [E] from Start [P]")
    print("  Controls: W=Up  S=Down  A=Left  D=Right  R=Reset  Q=Quit")
    print("=" * 35)
    for row in maze:
        line = ""
        for cell in row:
            if cell == '#':
                line += "██"
            elif cell == 'P':
                line += "😊"
            elif cell == 'E':
                line += "🚪"
            else:
                line += "  "
        print(line)
    print("=" * 35)
    print(f"  Moves: {moves}")
    print("=" * 35)

def get_key():
    """Get a single keypress from the user (cross-platform)"""
    if os.name == 'nt':  # Windows
        import msvcrt
        return msvcrt.getwch().lower()
    else:  # Unix/macOS
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def move_player(maze, player_pos, direction):
    """Move the player in the given direction"""
    r, c = player_pos
    if direction == 'w':   # Up
        new_r, new_c = r - 1, c
    elif direction == 's': # Down
        new_r, new_c = r + 1, c
    elif direction == 'a': # Left
        new_r, new_c = r, c - 1
    elif direction == 'd': # Right
        new_r, new_c = r, c + 1
    else:
        return player_pos, False, False

    # Check boundaries
    if new_r < 0 or new_r >= len(maze) or new_c < 0 or new_c >= len(maze[0]):
        return player_pos, False, False

    cell = maze[new_r][new_c]

    if cell == '#':
        # Can't move into a wall
        return player_pos, False, False
    elif cell == 'E':
        # Player reached the exit!
        maze[r][c] = ' '
        maze[new_r][new_c] = 'P'
        return (new_r, new_c), True, True
    else:
        # Valid move
        maze[r][c] = ' '
        maze[new_r][new_c] = 'P'
        return (new_r, new_c), True, False

def show_winner(moves):
    """Display the winning screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 35)
    print("   🎉 CONGRATULATIONS! 🎉")
    print("=" * 35)
    print("   You found the exit!")
    print(f"   Total Moves: {moves}")
    if moves < 30:
        print("   Rating: ⭐⭐⭐ Amazing!")
    elif moves < 60:
        print("   Rating: ⭐⭐ Good Job!")
    else:
        print("   Rating: ⭐ You made it!")
    print("=" * 35)

def show_intro():
    """Show intro screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 35)
    print("        🧩  MAZE GAME  🧩")
    print("=" * 35)
    print()
    print("  Welcome to the Maze Game!")
    print()
    print("  Your goal is to navigate")
    print("  through the maze and find")
    print("  the EXIT door 🚪")
    print()
    print("  Controls:")
    print("    W = Move Up")
    print("    S = Move Down")
    print("    A = Move Left")
    print("    D = Move Right")
    print("    R = Reset / New Maze \n Q = Quit Game")
    print()
    print("  Legend:")
    print("    😊 = You (Player)")
    print("    🚪 = Exit")
    print("    ██ = Wall")
    print()
    print("  Press any key to START...")
    print("=" * 35)

def main():
    """Main game loop"""
    show_intro()
    get_key()  # Wait for keypress to start

    while True:  # Outer loop allows reset
        maze = create_maze()
        player_pos = find_position(maze, 'P')
        moves = 0
        won = False

        while True:
            display_maze(maze, moves)

            key = get_key().lower()

            if key == 'q':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Thanks for playing! Goodbye 👋")
                return

            if key == 'r':  # Reset: generate a new maze
                break

            if key in ('w', 'a', 's', 'd'):
                player_pos, moved, won = move_player(maze, player_pos, key)
                if moved:
                    moves += 1

            if won:
                display_maze(maze, moves)
                show_winner(moves)
                print("  Press R to play again or Q to quit...")
                while True:
                    key = get_key().lower()
                    if key == 'r':
                        break
                    elif key == 'q':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Thanks for playing! Goodbye 👋")
                        return
                break  # Break inner loop to reset

if __name__ == "__main__":
    main()