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
            display_welcome_menu()
            break

    return username


def validate_username(username):
    """Check the chosen username to make sure it meets all criteria:
    8 characters or less, using only letters."""
    try:
        if len(username) > 8 or len(username) < 3:
            raise ValueError(
                f"""This username is {len(username)} characters long.
                Please use 8 characters or less."""
            )
        if username.isalpha() is False:
            raise ValueError(
                """This username contains characters that are not letters in
                the English alphabet."""
            )
    except ValueError as error:
        print(f"Invalid username: {error}\n")
        return False

    return True


def display_welcome_menu():
    """Display the menu options to the player after they enter a username.
    They can choose to read the instructions, start a new game, or view the
    high score board."""
    print("""\nWhat would you like to do first?\n
    1 - Read Instructions
    2 - Start a New Game
    3 - View High Scores\n""")
    menu_choice = int(input("Enter a number:\n"))
    choose_menu_option(menu_choice)


def choose_menu_option(entry):
    """Respond to the player's choice in the welcome menu. Validate that the
    input is one of the available options, and call the correct function based
    on the user's choice."""
    if entry == 1:
        print("here are the instructions")
    elif entry == 2:
        print("let's start a game!")
    elif entry == 3:
        print("here is the high score board!")
    display_welcome_menu()
    

get_username()
