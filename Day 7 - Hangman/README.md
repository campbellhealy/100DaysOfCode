# Hangman

### Generate the Random word
Use a list of words and select on of the words from the list.

### Underlines for Random word
Print a number of underlines, one for each letter of the word selected.
### User Guess & error Management
Ask the user to input a guess.
    This should be a single letter, put in error management for:
        more than one letter
        An integer
        Anything that is not a single letter

### Is the Guess in the Answer
create a set of the letters from the word.
    iterate through the set comparing the user's guess with the set

### Results
#### Comparision correct  
Replace underlines for the correct answer  
    Are all the letters added?  
        Yes - Win  
        No - Ask User again  
    
#### Comparison Incorrect  
Lose a life  
    Add a marker to the hangman  
    Has the hangman hung?  
        Yes - Lose  
        No - Ask the User Again  