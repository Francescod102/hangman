import random


class Hangman():

    def __init__(self, word_list, num_lives=5):   #constructor
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choices(self.word_list)
        self.word_guessed = ["_"]* len(self.word)
        self.num_letters  = len(set(self.word))
        self.list_of_guess= []  


    def check_guess(self, guess): #class methods
        self.guess = guess
        self.guess.lower()
        print(self.word)
        if self.guess in self.word:
            for i, character in enumerate(self.word):
                if character == self.guess:
                    self.word_guessed[i] = self.guess
            print(f'Yes! {self.guess} is in the word, guess another.')
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"sorry, {self.guess} is not in the world.")
            print(f"You have {self.num_lives} lives left.") 
        
        self.list_of_guess.append(self.guess)
    
    def ask_for_input(self):
        while True:
            self.guess = input('Please guess a letter. ')
            if not self.guess.isalpha() and len(self.guess) != 1:
                 print('Invalid letter. Please, enter a single alphabetical character.')

            elif self.guess in self.list_of_guess:
                 print('You already tried that letter!')

            else:
                 self.check_guess(self.guess)
                 
