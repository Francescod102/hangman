# Hangman
 Hangman is a classic word game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
## Milestone 2
**Task 1**

In this task I have create a file named milestone_2.py. This file will contain different types of codes.
I first create a list of words and I assign a variable called word_list. In Python, List are used to store multiple data in a single variable. Below are the following steps.  
- Create a list of 5 different types of fruit.
- Assign this list to a variable called 'word_list'.
- Print out the new created list.

**Task 2** <br>

In this task I am going to choose a random word from the list. To accomplish this task, I will be using 'random module'. The random module is one of Python's built-in modules. It has a choice method which returns a random item from a given sequence.

Step 1. Go to the first line of your file.
Step 2. Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
Step 3: Create the random.choice method and pass the word_list variable into the choice method.
Step 4: Assign the randomly generated word to a variable called word.
Step 5: Print out word to the standard output. Run the code several times and observe the words printed out after each run.

**Task 3** <br>

In this task, we are required to take user input. The print() function in Python displays output on the screen. Conversely, Python has an input() function that takes input from the screen. Note that the input function returns the user input in form of a string.
Step 1. Using the input function, ask the user to enter a single letter.
Step 2. Assign the input to a variable called guess.

**Task 4** <br>

Usually, when taking input from users, it is best to validate that the input makes sense. For example, we may want to ensure that only a single letter is entered and that only alphabetical characters are provided by the user. To do this, I created a conditional checks that must be passed before the input can be accepted.

Step 1. Create an if statement that checks if the length of the input is equal to 1 and the input is an alphabet.
Step 2: In the body of the if statement, print a message that says "Good guess!".
Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

## Milestone 3
**Task 1**

Create a new script called milestone_3.py. This file will contain the code for this milestone.
Step 1. Create a while loop and set the condition to True. Setting the condition to True ensures that the code run continuously.
In the body of the loop, write the code required for the following steps.
Step 2: Ask the user to guess a letter and assign this to a variable called guess.
Step 3. Check that the guess is a single, alphabetical character.
Step 4. If the guess passes the checks, break out of the loop.
Step 5: If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."

**Task 2**

Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer. For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".
Step 1. Create an if statement that checks if the guess is in the word.
Step 2. In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.
Step 3. Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

**Task 3**

Create functions to run the checks
Create 2 functions, check_guess and ask_for_input functions which contain the code for those two things.
The check_guess function will take the guessed letter as an argument and check if the letter is in the word.
Step 1: Define a function called check_guess. pass in the guess as a parameter for the function. Write the code for the following steps in the body of this function.
Step 2: Convert the guess into lower case.
Step 3. Move the code that you wrote to check if the guess is in the word into this function block.
The ask_for_input function.
Step 1. Define a function called ask_for_input.
Step 2. Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.
Step 3. Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.
Step 4. Outside the function, call the ask_for_input function to test your code.

## Milestone 4
**Task 1**

Create a new script called milestone_4.py. This file will contain the code for the third milestone.
Define the __init__ method of the Hangman class.
Step 1. Create a class called Hangman.
Step 2. Inside the class, create an __init__ method to initialise the attributes of the class. Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.
Step 3. Initialise the following attributes:
word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.
word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].
num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
num_lives: int - The number of lives the player has at the start of the game.
word_list: list - A list of words.
list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.

**Task 2**
In this task, you will create a method that will ask the user to guess a letter and another method that will check if the guess is in the word.
Remember that a method is a function that is defined inside a class.
Let's create the check_guess method.
Step 1: Define a method called check_guess. Pass the guess to the method as a parameter. In the body of the method, write the code for the following steps:
Convert the guessed letter to lower case
Create an if statement that checks if the guess is in the word
In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
You will continue with the logic of the check_guess method in the next task. For now, let's create the ask_for_input method.
Step 1. define a method called ask_for_input. In the body of the method, do the following:
Create a while loop and set the condition to True.
Ask the user to guess a letter and assign this to a variable called guess.
Create an if statement that runs if the guess is NOT a single alphabetical character.
In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
Create an elif statement that checks if the guess is already in the list_of_guesses.
In the body of the elif statement, print a message saying "You already tried that letter!".
If the guess is a single alphabetical character and it's not already in the list_of_guesses:
Create an else block and call the check_guess method. Remember to pass the guess as an argument to this method.
Step 2. Call the ask_for_input method to test your code.

**Task 3**

Return to your check_guess method and extend it to replace the underscore(s) in the word_guessed with the letter guessed by the user.
In the if block of your check_guess method, after your print statement, do the following:
Create a for-loop that will loop through each letter in the word.
Within the for-loop, do the following:
Create an if statement that checks if the letter is equal to the guess.
In the if block, replace the corresponding "_" in the word_guessed with the guess. HINT: You can index the word_guessed at the position of the letter and assign it to the letter.
Outside the for-loop, reduce the variable num_letters by 1.

**Task 4**

Define what happens if the guess is not in the word you are trying to guess.
Step 1. In the check_guess method, Create an else statement.
Step 2: Within the else block:
Reduce `num_lives' by 1.
print a message saying "Sorry, {letter} is not in the word."
print another message saying "You have {num_lives} lives left."
Step 3. Lastly, append the guess to the list_of_guesses. Ensure you do this outside the else block so that the letter can be appended to the list_of_guesses in both conditions.

## Milestone 5
**Task 1**

Create a function that will run all the code to run the game as expected. You should begin by creating a new script called milestone_5.py. Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.
Step 1. Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps
Step 1. Create a variable called num_lives and assign it to 5.
Step 2. Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game.
Step 3. Pass word_list and num_lives as arguments to the game object.
Step 4. Create a while loop and set the condition to True. In the body of the loop, do the following:
1. Check if the `num_lives` is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'.
2. Next, check if the `num_letters` is greater than 0. In this case, you would want to continue the game, so you need to call the `ask_for_input` method. 
3. If the `num_lives` is not 0 and the `num_letters` is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'.
Step 2. Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.

