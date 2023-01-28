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
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.") 
        
        self.list_of_guesses.append(guess)
        print(self.word_guessed)
    
    def ask_for_input(self):
        while True:
            guess = input('Please guess a letter. ')
            if not guess.isalpha() and len(guess) != 1:
                 print('Invalid letter. Please, enter a single alphabetical character.')

            elif guess in self.list_of_guesses:
                 print('You already tried that letter!')

            else:
                 self.check_guess(guess)
                 break
                 



def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while True:
        if  game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
             game.ask_for_input()

        elif game.num_lives != 0 and game.num_letters < 1:
            print("Congratulation! You won the game!")
            break
        
if __name__ == '__main__':
    word_list = ["bluberry", "oranges" , "banana" , "apple" , "pineapple","mango", "pear", "watermelon", "lemon"]
    play_game(word_list)
