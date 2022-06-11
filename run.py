"""Import external libraries"""
import gspread
from google.oauth2.service_account import Credentials

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

print("""                                 WELCOME TO
████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██
   ██    ██ ██     █████   ██    ███████ ██      █████  ██    ██    ██ █████
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██
   ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████
   """)
