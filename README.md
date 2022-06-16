# Tic-Tac-Toe

Tic-Tac-Toe is a Python terminal game, which runs in the Code Institute mock terminal on Heroku. 

Users can play tic-tac-toe against a computer. The objective of the game is to place 3 Xs or 3 Os in a row on a 3x3 grid. Every time a new game starts, the first player is randomly determined (either the human user or the computer).

Users can also view a high score board to see how they compare to other players. Each win counts as one point on the score board. 

## Flowchart
I created a flowchart to determine the logic of the game before starting to code. This allowed me to visualize the steps the user and computer each need to complete as they progress through the game.

This also helped with planning input validation, and the options presented to the user when the program is initalized (play game, view instructions, and view the high score board).
![Flowchart](assets/images/README/tictactoe_flowchart.png)

## User Stories

  -   #### First Time Visitor Goals

      1. As a First Time Visitor, I want to understand how to play Tic-Tac-Toe.
      2. As a First Time Visitor, I want to understand how to navigate the program to find the instructions, the high score board, and how to start a new game.
      3. As a First Time Visitor, I want to understand why I receive error messages and how to resolve them.
      4. As a First Time Visitor, I want to easily start a new game and play Tic-Tac-Toe against the computer.

  -   #### Returning Visitor Goals

      1. As a Returning Visitor, I want to view the high score board to see what has changed since I last played.
      2. As a Returning Visitor, I want to start a new round of Tic-Tac-Toe games against the computer, so I can update my own high score.
      3. As a Returning Visitor, I want my high scores to be associated with the same username. 

  -   #### Frequent User Goals
      1. As a Frequent User, I want to see my previous scores on the high score board. 

## Features 

### Existing Features

### Data Structures

  - A class for the game board:
  ```
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
  ```

  The Board class serves two major functions: 
  - 1) to display the game board, with a value assigned to each bank cell in the board. 
  - 2) to update the game board every time the computer or player makes a move, using a function that changes the value of the chosen cell. This cross-references the cell number that the player chose, and updates it with the symbol (X or O) that has been assigned to that player.

  - A class for the player:
  ```
  class Player():
    """
    Player class. This determines whether the player or computer is playing
    Xs or Os.
    """

    def __init__(self, playing_as):
        self.playing_as = playing_as
  ```

  This allows the program to randomly assign "X" or "O" to either the human player or the computer player, both instances of the player class. 

### Features Left to Implement

  - The option to play against another human opponent in person. Right now, the only option is to play against the computer, and the program will randomly decide who goes first. In the future there will be the option for two players to play against each other, with the option to choose who goes first.

## Testing 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 


### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 
- [Tech with Tim](https://www.youtube.com/watch?v=u51Zjlnui4Y)'s Colorama tutorial was used to install & use Colorama, to change text colour in the terminal.
- [This article](https://www.uxmatters.com/mt/archives/2007/01/applying-color-theory-to-digital-displays.php) on UX Matters was used to confirm which colours are best for accessibility on a black background. This helped me choose a bright cyan as my welcome message colour and yellow for my error messages.
- The Tabulate library was used to display the high score board data in a table. [DelftStack](https://www.delftstack.com/howto/python/data-in-table-format-python/) introduced me to the tabulate library, and I used [PyPi](https://pypi.org/project/tabulate/) for help on how to install it.
- [This page](https://www.extendoffice.com/documents/excel/5170-google-sheets-automatically-sort-alphabetically.html) on ExtendOffice was used to look up how to sort a Google Sheet automatically (when new scores are added to the sheet, this automatically sorts them from highest to lowest).
- I used [this page](https://www.guru99.com/python-time-sleep-delay.html) on Guru99 for instructions on how to import and use the time module.
- [TokyoEdtech's Tic-Tac-Toe Tutorial](https://www.youtube.com/watch?v=7Djh-Cbgi0E) on Youtube helped give me ideas for how to display the Board class (in Part 1 of the video series) and how to determine a winner (Part 3 of the video series). Code from these videos was used and modified in the Board class and in the `check_result` function.
- [This question on StackOverflow](https://stackoverflow.com/questions/41906978/python-randomly-choose-a-spot-on-a-tic-tac-toe-board) helped me understand how to use the random method to assign X or O to the player randomly, and select a random cell for the computer to play each turn.
- I used [this question on StackOverflow](https://stackoverflow.com/questions/48266880/python-generate-random-integer-that-is-not-in-a-list) to have the computer only guess a cell that had not already been guessed (and would therefore be present in the 'guesses' list).

### Media
- [Patorjk.com](https://patorjk.com/) was used to create the "Tic-Tac-Toe" ASCII lettering in the welcome message.

Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 