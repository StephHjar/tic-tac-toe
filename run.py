"""Import external libraries"""
import os
import time
import random
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tic_tac_toe_scores')

high_scores = SHEET.worksheet('high_scores')

high_score_data = high_scores.get_all_values()

scores = {"computer": 0, "player": 0}
guesses = []


class Board():
    """
    Main game board class. This sets the board size, and has methods for
    adding guesses and printing the board. Some of the code used here was
    modified from TokyoEdtech's Youtube tutorial (credit in README).
    """

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        """
        Displays the game board, with numbers in each cell so the
        player knows which cell corresponds to which number when making
        guesses.
        """
        print("Here is the active game board:\n")
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print(" ---------")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print(" ---------")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")

    def update_cell(self, cell_no, player):
        """
        Updates a cell in the board with the player or computer's move (X or
        O).
        """
        self.cells[cell_no] = player
        return self.cells


board = Board()


class Player():
    """
    Player class. This determines whether the player or computer is playing
    Xs or Os.
    """

    def __init__(self, playing_as):
        self.playing_as = playing_as


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def display_header():
    """Displays the welcome message at the top of the screen."""
    print(f"""{Fore.CYAN}{Style.BRIGHT}                                  WELCOME TO
 ████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████
    ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██
    ██    ██ ██     █████   ██    ███████ ██      █████  ██    ██    ██ █████
    ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██
    ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████
   """)


def get_username():
    """
    Ask the player to provide a username, and check whether the input is valid.
    """
    while True:
        username = input("Please enter a username between 3 and 8 letters:\n")
        if validate_username(username):
            clear()
            print("\nHello, " + str(username) + "! Let's get ready to play!\n")
            break

    return username


def validate_username(username):
    """
    Check the chosen username to make sure it meets all criteria: 8 characters
    or less, using only letters.
    """
    try:
        if username.isalpha() is False:
            raise ValueError(
                f"""\nThe username '{username}' contains characters that are not letters.
Please only use letters between A - Z."""
            )
        if len(username) > 8 or len(username) < 3:
            raise ValueError(
                f"""\nThis username is {len(username)} characters long.
Please use between 3 and 8 letters."""
            )

    except ValueError as error:
        print(f"\nInvalid username: {error}\n")
        return False

    return True


def display_main_menu():
    """
    Display the menu options to the player after they enter a username.
    They can choose to read the instructions, start a new game, or view the
    high score board.
    """
    print("""\nWhat would you like to do now?\n
    1 - Read Instructions
    2 - Start a New Game
    3 - View High Scores\n""")
    menu_choice = input("Enter a number:\n")
    choose_menu_option(menu_choice)


def choose_menu_option(entry):
    """
    Respond to the player's choice in the welcome menu. Validate that the
    input is one of the available options, and call the correct function based
    on the user's choice.
    """
    while True:
        if validate_num(entry):
            if int(entry) == 1:
                new_screen()
                show_instructions()
                break
            if int(entry) == 2:
                new_screen()
                start_new_game()
                break
            if int(entry) == 3:
                new_screen()
                show_high_scores()
                break
            print("\nInvalid entry: Please enter a number between 1 - 3.")
        display_main_menu()
        break


def validate_num(num):
    """
    Check that a user's numerical entry is a valid number. Return relevant
    error messages if not.
    """
    try:
        if num.isdigit() is False:
            raise TypeError(f"""You entered '{num}'.
Please enter a valid number.""")
    except TypeError as error:
        print(f"\nInvalid entry: {error}")
        return False

    return True


def show_instructions():
    """
    Display instructions showing how to play tic-tac-toe, and give the user
    the option to exit the instructions when they are finished.
    """
    print("""INSTRUCTIONS:\n
    The objective of the game is to get 3 Xs or 3 Os in a row, on a 3x3
    grid.\n
    Here is what to expect when you start a new game of Tic-Tac- Toe:\n
    1) Either you or the computer will be randomly chosen to make the
    first move. If you go first, you will be assigned the letter X. If you
    go second, you will be assigned the letter O.\n
    2) A 3 x 3 grid will be displayed, with each cell assigned a number
    from 1 to 9.\n
    3) Whoever goes first will pick a cell to place their X. The next
    player will then select a cell to place their O.\n
    4) The game will continue alternating turns until either you or the
    computer has 3 Xs or Os in a row on the board. Then, a winner will be
    declared. You will have the option to play again, or log your high
    score.\n
    Have fun!\n""")
    exit_option()


def show_high_scores():
    """
    Display the high score board to the user, and gives them the option to
    exit to the main menu.
    """
    print("\nHIGH SCORES\n")
    print(tabulate(high_score_data[0:6:1], headers=["Username", "Score"]))
    exit_option()


def exit_option():
    """
    Shows the user the option to exit the current page and return to the
    main menu.
    """
    while True:
        exit_choice = input(str("\nExit to main menu? Y/N\n"))
        if exit_choice.lower() == "y":
            print("Okay! Exiting to the main menu...")
            time.sleep(1)
            new_screen()
            display_main_menu()
            break
        if exit_choice.lower() == "n":
            print("Okay! Let me know when you are ready to exit.")
            continue
        validate_exit(exit_choice)

    return exit_choice


def validate_exit(choice):
    """
    Validate a user's entry when they are given the option to exit and
    return to a previous screen (from the instructions and high score pages).
    Display an error message if anything other than Y or N is entered.
    """
    try:
        if choice.lower() != "y" or choice.lower() != "n":
            raise ValueError(f"""\nYou entered '{choice}'. Please enter either Y
(for yes) or N (for no).""")
    except ValueError as error:
        print(f"\nInvalid entry: {error}")
        return False
    return True


def new_screen():
    """
    Clear the screen and display the header whenever a player loads a new
    screen in the terminal (i.e. instructions page, high score board, starting
    a new game).
    """
    clear()
    display_header()


def start_new_game():
    """
    Starts a new game of tic-tac-toe. Resets the player and computer scores
    to 0 and displays a new game board.
    """
    new_screen()
    display_board_guide()
    new_board = Board()
    new_board.display()
    choose_player()
    exit_option()


def choose_player():
    """
    Randomly assigns X or O to the player or the computer when a new game
    is run.
    """
    player_human = Player(random.choice(["X", "O"]))
    if player_human.playing_as == "X":
        player_computer = Player("O")
    else:
        player_computer = Player("X")
    print(f"""\nYou will play as {player_human.playing_as}! The computer will play
as {player_computer.playing_as}. X goes first.""")
    time.sleep(2)
    if player_human.playing_as == "X":
        take_human_turn(player_human.playing_as)
    if player_human.playing_as == "O":
        take_computer_turn(player_computer.playing_as)


def take_human_turn(player):
    """
    Prompts the player to take their turn, by choosing a cell on the board
    to place their X or O. Triggers validation workflow to ensure the entry is
    valid.
    """
    check_result()
    print("\nIt's your turn!")
    while True:
        cell_choice = input(f"""\nWhere would you like to place your
{player}?\n""")
        if validate_num(cell_choice):
            if validate_move(cell_choice):
                guesses.append(int(cell_choice))
                update_board(cell_choice, player)
                print(f"""\nOkay! You have chosen cell {cell_choice}.\n
Please wait...""")
                time.sleep(2)
                if player == "X":
                    take_computer_turn("O")
                else:
                    take_computer_turn("X")


def take_computer_turn(player):
    """
    Makes the computer take its turn, by placing an X or O in a random free
    cell on the board.
    """
    check_result()
    while True:
        cell_choice = random.randint(1, 9)
        while cell_choice in guesses and len(guesses) < 9:
            cell_choice = random.randint(1, 9)
        if validate_move(cell_choice):
            guesses.append(int(cell_choice))
            update_board(cell_choice, player)
            print(f"""\nComputer has chosen to place their {player} in cell
{cell_choice}.\n
Please wait...""")
            time.sleep(1)
            if player == "X":
                take_human_turn("O")
            else:
                take_human_turn("X")


def check_result():
    """
    Checks for a win, loss, or draw before starting a new move.
    """
    if len(guesses) >= 9:
        declare_draw()


def validate_move(cell):
    """
    Checks to make sure the player or computer is making a valid move: i.e.
    placing their X or O in an empty square.
    """
    try:
        if int(cell) < 1 or int(cell) > 9:
            raise ValueError(f"""\nYou entered {cell}. Please enter a number
between 1 - 9.""")
        if int(cell) in guesses:
            raise ValueError("""This cell is already occupied. Please enter
another number.""")
    except ValueError as error:
        print(f"\nInvalid entry: {error}")
        return False
    return True


def update_board(num, symbol):
    """
    Passes the player or computer's move to the board and updates it.
    """
    clear()
    display_header()
    display_board_guide()
    board.update_cell(int(num) - 1, symbol)
    board.display()


def declare_draw():
    """
    Declares a draw if all cells on the board are filled without declaring a
    winner.
    """
    print("""The game has ended in a draw! No points will be awarded. Play
again?""")
    exit_option()


def display_board_guide():
    """
    Displays a sample board with numbered cells, so the user knows which
    number to input for each cell.
    """
    print("""\nUse this board as a guide when making guesses. Each number
corresponds to a cell on the board.\n""")
    print(" 1 | 2 | 3 ")
    print(" ---------")
    print(" 4 | 5 | 6 ")
    print(" ---------")
    print(" 7 | 8 | 9 \n")


def main():
    """
    Run functions needed to start the program.
    """
    display_header()
    get_username()
    display_header()
    display_main_menu()


main()
