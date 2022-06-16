## Testing 

### Manual Testing
The program was tested manually by going through all possible error validation messages, and all possible game results (player win, computer win, draw). See the results below:

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


### Validator Testing 


### Unfixed Bugs

- Due to limitations in Code Institute's Heroku template, which was used for deployment, this site is *not* fully responsive. This shows responsiveness during various stages of gameplay: 
![Am I Responsive screenshot](documentation/testing/amiresponsive.png)

The terminal cannot receive input from a mobile keyboard, and does not resize based on window size. Making the application fully responsive was beyond the scope of this project.
