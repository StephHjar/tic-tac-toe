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
        username = input("Please enter a username of 8 letters or less:\n")
        if validate_username(username):
            print("\nWelcome, " + str(username) + "! Let's get started!")
            display_welcome_menu()
            break

    return username


def validate_username(username):
    """Check the chosen username to make sure it meets all criteria:
    8 characters or less, using only letters."""
    try:
        if len(username) > 8:
            raise ValueError(
                f"""This username is {len(username)} characters long.
                Please use 8 characters or less."""
            )
        if username.isalpha() is False:
            raise ValueError(
                """This username contains characters that are not letters in
                the English alphabet."""
            )
    except ValueError as e:
        print(f"Invalid username: {e}\n")
        return False

    return True


def display_welcome_menu():
    """Display the menu options to the player after they enter a username.
    They can choose to read the instructions, start a new game, or view the
    high score board."""
    print("""\nWhat would you like to do first?\n
    1 - Read Instructions
    2 - Start a New Game
    3 - View High Scores""")


get_username()


menu_choice = input("Enter a number:\n")
if str(menu_choice) == "1":
    print("here are the instructions")
