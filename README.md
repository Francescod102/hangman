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
