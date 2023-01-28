import random


class Hangman():

    def __init__(self, word_list, num_lives=5):   #constructor
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"]* len(self.word)
        self.num_letters  = len(set(self.word))
        self.list_of_guesses = []  


    def check_guess(self, guess): #class methods
    
        if guess.lower() in self.word:
            print(f'Good guess! {guess} is in the word.')
        
            for i, character in enumerate(self.word):
                if character == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"sorry, {guess} is not in the world.")
            print(f"You have {self.num_lives} lives left.") 
        
        self.list_of_guess.append(guess)
        print(self.word_guessed)
    
    def ask_for_input(self):
        while True:
            guess = input('Please guess a letter. ')
            if not guess.isalpha() and len(guess) != 1:
                 print('Invalid letter. Please, enter a single alphabetical character.')

            elif guess in self.list_of_guess:
                 print('You already tried that letter!')

            else:
                 self.check_guess(guess)
                 break
                 
