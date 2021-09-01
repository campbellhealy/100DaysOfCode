#### READ ME

**Higher or Lower**

I saw what the lesson required, to create a game that asked the user which of the two
celebs had the higher amount of follwers.

I took the game data and the header logo from lesson and created the rest of the game 
from scratch based on a screenshot of the game.

It is console based

**header()** - To clear the console and send the logo to the console

**random_choice()** - Used to select a dict from the list of dicts in the game data

**higher_lower()** - The main code. 
This twice actions random_choice() to build the comparison. It then directly extracts the items to ensure items
in each of the dicts are not in a random order.
The number of followers is compared between both. Where the values are the same, the code restarts as a simple
error management process.
The options are presented to the user and the users guess is compared to the answer.
If the user guess is correct or incorrect a message is presented to the user.

**again()** - Finally the user is asked if they want to restart the game. (Reusable code)