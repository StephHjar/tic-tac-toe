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

high_scores = SHEET.worksheet("high_scores")

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
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} \n")

    def update_cell(self, cell_no, player):
        """
        Updates a cell in the board with the player or computer's move (X or
        O).
        """
        self.cells[cell_no] = player

    def is_winner(self, player):
        """
        Read the board to determine when there is a winner (3 of the same
        symbol in a row). Some code from GeeksforGeeks was used while
        refactoring this function, as well as code adapted from several
        answers in a thread on StackOverflow. Credits for both are in the
        README.
        """
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if (
                self.cells[win[0]] == player and
                self.cells[win[1]] == player and
                self.cells[win[2]] == player
            ):
                return True


board = Board()


class Player():
    """
    Player class. This determines whether the player or computer is playing
    Xs or Os.
    """

    def __init__(self, playing_as):
        self.playing_as = playing_as

    def take_human_turn(self, player):
        """
        Prompts the player to take their turn, by choosing a cell on the board
        to place their X or O. Triggers validation workflow to ensure the
        entry is valid.
        """
        print("It's your turn!\n")
        while True:
            cell_choice = input("Where would you like to place your"
                                f" {player}?\n")
            if validate_num(cell_choice):
                if validate_move(cell_choice):
                    guesses.append(int(cell_choice))
                    update_board(cell_choice, player)
                    print(f"Okay! You have chosen cell {cell_choice}."
                          "\nPlease wait...\n")
                    time.sleep(2)
                    if len(guesses) >= 5:
                        winner = "You"
                        check_result(player, winner)
                    if player == "X":
                        self.take_computer_turn("O")
                    else:
                        self.take_computer_turn("X")

    def take_computer_turn(self, player):
        """
        Makes the computer take its turn, by placing an X or O in a random free
        cell on the board.
        """
        while True:
            cell_choice = random.randint(1, 9)
            while cell_choice in guesses and len(guesses) < 9:
                cell_choice = random.randint(1, 9)
            if validate_move(cell_choice):
                guesses.append(int(cell_choice))
                update_board(cell_choice, player)
                print(f"Computer has chosen to place their {player} in cell"
                      f" {cell_choice}."
                      "\nPlease wait...\n")
                time.sleep(1)
                if len(guesses) >= 5:
                    winner = "The computer"
                    check_result(player, winner)
                if player == "X":
                    self.take_human_turn("O")
                else:
                    self.take_human_turn("X")


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy. Code
    from StackOverflow (credit in README).
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


def display_main_menu():
    """
    Display the menu options to the player after they enter a username.
    They can choose to read the instructions, start a new game, or view the
    high score board.
    """
    print("""What would you like to do now?\n
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
            print(f"{Fore.YELLOW}{Style.BRIGHT}\nInvalid entry: Please enter a"
                  " number between 1 - 3.\n")
        display_main_menu()
        break


def validate_num(num):
    """
    Check that a user's numerical entry is a valid number. Return relevant
    error messages if not.
    """
    try:
        if num.isdigit() is False:
            raise TypeError(f"You entered '{num}'."
                            " Please enter a valid number.\n")
    except TypeError as error:
        print(f"{Fore.YELLOW}{Style.BRIGHT}\nInvalid entry: {error}")
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
    Here is what to expect when you start a new game of Tic-Tac- Toe:\n""")
    input("Press enter to continue...\n")
    print("""STEPS:\n
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


def sort_key(score):
    """
    Retrieves the column of numerical scores from the Google Sheet containing
    the high score data. This code was adapted from PythonTutorial.net (credit
    in README).
    """
    return int(score[1])


def show_high_scores():
    """
    Display the high score board to the user, and gives them the option to
    exit to the main menu. The 'sort' code was adapted from PythonTutorial.net
    (credit in README).
    """
    print("\nHIGH SCORES\n")
    high_score_data.sort(key=sort_key, reverse=True)
    print(tabulate(high_score_data[0:5:1], headers=["Username", "Score"]))
    print(" ")
    exit_option()


def exit_option():
    """
    Shows the user the option to exit the current page and return to the
    main menu.
    """
    while True:
        exit_choice = input(str("Exit to main menu? Y/N\n"))
        if exit_choice.lower() == "y":
            print("\nOkay! Exiting to the main menu...")
            time.sleep(1)
            new_screen()
            display_main_menu()
            break
        if exit_choice.lower() == "n":
            print("\nOkay! Let me know when you are ready to exit.\n")
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
            raise ValueError(f"\nYou entered '{choice}'. Please enter either Y"
                             " (for yes) or N (for no).\n")
    except ValueError as error:
        print(f"{Fore.YELLOW}{Style.BRIGHT}\nInvalid entry: {error}")
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
    guesses.clear()
    display_board_guide()
    clear_board()
    board.display()
    choose_player()


def clear_board():
    """
    Clears the cells in the Board class when starting a new game.
    """
    for i in range(len(board.cells)):
        board.update_cell(i, " ")


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
    print(f"You will play as {player_human.playing_as}! The computer will play"
          f" as {player_computer.playing_as}. X goes first.\n")
    input("Press enter to start the game...\n")
    if player_human.playing_as == "X":
        player_human.take_human_turn(player_human.playing_as)
    if player_human.playing_as == "O":
        player_computer.take_computer_turn(player_computer.playing_as)


def check_result(playing_as, winner):
    """
    Checks for a win, loss, or draw before starting a new move. The
    board.is_winner code was adapted from TokyoEdtech's YouTube tutorial
    (credit in README).
    """

    if board.is_winner(playing_as):
        print(f"{winner} won!\n")
        update_score(winner)
        new_game_option()

    if len(guesses) >= 9:
        declare_draw()


def update_score(winner):
    """
    Increment the score by one for whoever has won the game (human player or
    computer).
    """
    if winner == "You":
        scores['player'] += 1
    else:
        scores['computer'] += 1
    display_score()


def display_score():
    """
    Displays the overall score for the player and the computer after each
    round of tic-tac-toe.
    """
    print("You have won " + str(scores['player']) + " game(s). The computer"
          " has won " + str(scores['computer']) + " game(s).\n")


def validate_move(cell):
    """
    Checks to make sure the player or computer is making a valid move: i.e.
    placing their X or O in an empty square.
    """
    try:
        if int(cell) < 1 or int(cell) > 9:
            raise ValueError(f"\nYou entered {cell}. Please enter a number"
                             " between 1 - 9.\n")
        if int(cell) in guesses:
            raise ValueError("\nThis cell is already occupied. Please enter"
                             " another number.\n")
    except ValueError as error:
        display_board_guide()
        board.display()
        print(f"{Fore.YELLOW}{Style.BRIGHT}\nInvalid entry: {error}")

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
    print("""The game has ended in a draw! No points will be awarded.\n""")
    display_score()
    new_game_option()


def new_game_option():
    """
    Gives the player the option to start a new game, after a win, loss, or
    draw.
    """
    while True:
        new_game_choice = input(str("Start a new game? Y/N\n"))
        if new_game_choice.lower() == "y":
            print("Okay! Starting a new game...")
            start_new_game()
            break
        if new_game_choice.lower() == "n":
            high_score_option()
        validate_exit(new_game_choice)

    return new_game_choice


def high_score_option():
    """
    Gives the player the option to save their score to the high score board
    when they are finished playing.
    """
    while True:
        high_score_choice = input(str("\nOkay! Would you like to save your"
                                      " score to the high score board? Y/N\n"))
        if high_score_choice.lower() == "y":
            save_high_score()
        if high_score_choice.lower() == "n":
            print("\nOkay! Your score will not be recorded.\n")
            end_game()
        validate_exit(high_score_choice)

    return high_score_choice


def save_high_score():
    """
    Saves the player's high score to the 'tic_tac_toe_scores' Google Sheet. If
    their score is in the top 5 highest scores, it will be displayed on the
    high score screen accessible from the main menu.
    """
    while True:
        high_scores.append_row([str(get_username().upper()),
                                int(scores['player'])])
        print("\nOkay! Updating high score board...\n")
        time.sleep(2)
        end_game()


def get_username():
    """
    Ask the player to provide a username, and check whether the input is valid.
    """
    while True:
        username = input("\nPlease enter a username between 3 and 8"
                         " letters:\n")
        if validate_username(username):
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
                f"\nThe username '{username}' contains characters that are not"
                " letters.\nPlease only use letters between A - Z."
            )
        if len(username) > 8 or len(username) < 3:
            raise ValueError(
                f"\nThis username is {len(username)} characters long."
                " Please use between 3 and 8 letters."""
            )

    except ValueError as error:
        print(f"{Fore.YELLOW}{Style.BRIGHT}\nInvalid username: {error}")
        return False

    return True


def end_game():
    """
    Ends gameplay with instructions on how to restart the program, and the
    option to return to the main menu.
    """
    print("I hope you enjoyed playing Tic-Tac-Toe! Press the orange 'Run\n"
          "Program' button above if you would like to start the program"
          " over\nand reset all scores to '0'. Otherwise:\n")
    exit_option()


def display_board_guide():
    """
    Displays a sample board with numbered cells, so the user knows which
    number to input for each cell.
    """
    print("\nUse this board as a guide when making guesses. Each number"
          " corresponds to a cell on the board.\n")
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
    display_main_menu()


main()
