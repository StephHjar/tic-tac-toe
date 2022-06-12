"""Import external libraries"""
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


def show_welcome_message():
    """Displays the welcome message at the top of the screen."""
    print(f"""{Fore.CYAN}{Style.BRIGHT}                                 WELCOME TO
 ████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████
    ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██
    ██    ██ ██     █████   ██    ███████ ██      █████  ██    ██    ██ █████
    ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██
    ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████
   """)


def get_username():
    """Ask the player to provide a username,
    and check whether the input is valid"""
    while True:
        username = input("Please enter a username between 3 and 8 letters:\n")
        if validate_username(username):
            print("\nWelcome, " + str(username) + "! Let's get started!")
            display_main_menu()
            break

    return username


def validate_username(username):
    """Check the chosen username to make sure it meets all criteria:
    8 characters or less, using only letters."""
    try:
        if username.isalpha() is False:
            raise ValueError(
                f"""The username '{username}' contains characters that are not letters.
                Please only use letters between A - Z."""
            )
        if len(username) > 8 or len(username) < 3:
            raise ValueError(
                f"""This username is {len(username)} characters long.
                Please use between 3 and 8 letters."""
            )

    except ValueError as error:
        print(f"Invalid username: {error}\n")
        return False

    return True


def display_main_menu():
    """Display the menu options to the player after they enter a username.
    They can choose to read the instructions, start a new game, or view the
    high score board."""
    print("""\nWhat would you like to do now?\n
    1 - Read Instructions
    2 - Start a New Game
    3 - View High Scores\n""")
    menu_choice = input("Enter a number:\n")
    choose_menu_option(menu_choice)


def choose_menu_option(entry):
    """Respond to the player's choice in the welcome menu. Validate that the
    input is one of the available options, and call the correct function based
    on the user's choice."""
    while True:
        if validate_num(entry):
            if int(entry) == 1:
                show_instructions()
                break
            if int(entry) == 2:
                print("let's start a game!")
                break
            if int(entry) == 3:
                show_high_scores()
                break
            print("\nInvalid entry: Please enter a number between 1 - 3.")
        display_main_menu()
        break


def validate_num(num):
    """Check that a user's numerical entry is a valid number. Return relevant
    error messages if not."""
    try:
        if num.isdigit() is False:
            raise TypeError("Please enter a valid number.")
    except TypeError as error:
        print(f"\nInvalid entry: {error}\n")
        return False

    return True


def show_instructions():
    """Display instructions showing how to play tic-tac-toe, and give the user
    the option to exit the instructions when they are finished."""
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


def exit_option():
    """Shows the user the option to exit the current page and return to the
    main menu"""
    while True:
        exit_choice = input(str("Exit to main menu? Y/N\n"))
        if exit_choice.lower() == "y":
            print("Okay! Exiting to the main menu...")
            display_main_menu()
            break
        if exit_choice.lower() == "n":
            print("Okay! Let me know when you are ready to exit.")
            continue
        validate_exit(exit_choice)

    return exit_choice


def validate_exit(choice):
    """Validate a user's entry when they are given the option to exit and
    return to a previous screen (from the instructions and high score pages).
    Display an error message if anything other than Y or N is entered."""
    try:
        if choice.lower() != "y" or choice.lower() != "n":
            raise ValueError(f"""You entered '{choice}'. Please enter either Y
            (for yes) or N (for no).""")
    except ValueError as error:
        print(f"Invalid entry: {error}")
        return False
    return True


def show_high_scores():
    """Displays the high score board to the user, and gives them the option to
    exit to the main menu."""
    print("Here are the high scores!")
    exit_option()


def run():
    """Run functions needed to start the program."""
    show_welcome_message()
    get_username()


run()
