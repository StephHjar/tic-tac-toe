## Testing 

### Manual Testing
The program was tested manually by going through all possible error validation messages, all possible game results (player win, computer win, draw), and the functionality of writing to the high score board. See the results below:

| Test Case | Pass? | Screenshot |
|-----------|-------|------------|
|Main menu options: enter a space|Yes|![Successful error message](documentation/testing/main_menu_space.png)|
|Main menu options: enter a letter|Yes|![Successful error message](documentation/testing/main_menu_letter.png)|
|Main menu options: enter a special character|Yes|![Successful error message](documentation/testing/main_menu_special_character.png)|
|Main menu options: enter a number not between 1-3|Yes|![Successful error message](documentation/testing/main_menu_number.png)|
|Exit options: enter a space|Yes|![Successful error message](documentation/testing/exit_space.png)|
|Exit options: enter a letter other than Y or N|Yes|![Successful error message](documentation/testing/exit_letter.png)|
|Exit options: enter a special character|Yes|![Successful error message](documentation/testing/exit_special_character.png)|
|Exit options: enter a number|Yes|![Successful error message](documentation/testing/exit_number.png)|
|Gameplay options: enter a space|Yes|![Successful error message](documentation/testing/gameplay_space.png)|
|Gameplay options: enter a letter|Yes|![Successful error message](documentation/testing/gameplay_letter.png)|
|Gameplay options: enter a special character|Yes|![Successful error message](documentation/testing/gameplay_special_character.png)|
|Gameplay options: enter a number not between 1-9|Yes|![Successful error message](documentation/testing/gameplay_number.png)|
|Gameplay options: enter a number of an occupied cell|Yes|![Successful error message](documentation/testing/gameplay_occupied.png)|
|Gameplay: computer win|Yes|![Computer win](documentation/testing/computer_win.png)
|Gameplay: player win|Yes|![Player win](documentation/testing/player_win.png)
|Gameplay: draw|Yes|![Draw](documentation/testing/draw.png)
|New game options: enter a space|Yes|![Successful error message](documentation/testing/new_game_space.png)|
|New game options: enter a letter other than Y or N|Yes|![Successful error message](documentation/testing/new_game_letter.png)|
|New game options: enter a special character|Yes|![Successful error message](documentation/testing/new_game_special_character.png)|
|New game options: enter a number|Yes|![Successful error message](documentation/testing/new_game_number.png)|
|High score options: enter a space|Yes|![Successful error message](documentation/testing/high_score_space.png)|
|High score options: enter a letter other than Y or N|Yes|![Successful error message](documentation/testing/high_score_letter.png)|
|High score options: enter a special character|Yes|![Successful error message](documentation/testing/high_score_special_character.png)|
|High score options: enter a number|Yes|![Successful error message](documentation/testing/high_score_number.png)|
|Username entry: enter a space|Yes|![Successful error message](documentation/testing/username_space.png)|
|Username entry: enter a special character|Yes|![Successful error message](documentation/testing/username_special_character.png)|
|Username entry: enter a number|Yes|![Successful error message](documentation/testing/username_number.png)|
|Username entry: less than 3 letters|Yes|![Successful error message](documentation/testing/username_letter3.png)|
|Username entry: more than 8 letters|Yes|![Successful error message](documentation/testing/username_letter8.png)|
|Confirm writing to high score board|Yes|![High score confirmation message](documentation/testing/high_score_confirmation.png)|
|Update Google Sheet|Yes|![Updated spreadsheet](documentation/testing/high_score_sheet.png)

Please see the [Closed Issues tab on GitHub](https://github.com/StephHjar/tic-tac-toe/issues?q=is%3Aissue+is%3Aclosed) for a list of all resolved bugs.

### Validator Testing 
Code was passed through the [PEP8 online linter](http://pep8online.com/). On the initial run, one issue was found, a line break before a binary operator:

![PEP8 results 1](documentation/testing/pep8_result1.png)

I adjusted the line spacing in the function, and no errors were found on a second pass:

![PEP8 results 2](documentation/testing/pep8_result2.png)

After making some changes to the code (spacing/indentation), a third pass also came back with no issues:
![PEP8 results 3](documentation/testing/pep8_result3.png)


### Unfixed Bugs

- Due to limitations in Code Institute's Heroku template, which was used for deployment, this site is *not* fully responsive. The terminal cannot receive input from a mobile keyboard, and does not resize based on window size. Making the application fully responsive was beyond the scope of this project. This shows responsiveness during various stages of gameplay: 

![Am I Responsive screenshot](documentation/testing/amiresponsive.png)


- Similarly, due to limitations in the Heroku template, the `clear()` function only clears the visible part of the terminal. 
This is not disruptive to the player, as the visible area is always cleared. Everything the user needs to interact with is contained on one screen, so the user has no reason to scroll up within the terminal. 
However, if they do scroll up after having navigated through different screens, they will see the parts of the previous screen that were not cleared (i.e. anything that was outside the visible section of the terminal when the `clear()` function was called). Because this is only a limitation in the deployed terminal, and not an issue when the program is run in the command line, this remains unresolved at this time. See an example below: 

![Uncleared screen](documentation/testing/clear_screen.png)