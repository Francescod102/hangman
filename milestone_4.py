import random

class Hangman():

    def __init__(self, word_list, num_lives=5):   #constructor
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choices(self.word_list)
        self.word_guessed = ["_"]* len(self.word)
        self.num_letters  = len(set(self.word))
        self.list_letter= []  


    def check_letter(self, letter): #class methods
        
        if letter.lower() in self.word:
            for i, character in enumerate(len(self.word)):
                if character == letter:
                    self.word_guessed[i] = letter
            print(f'Yes! {letter} is in the word, guess another.')
            print(self.word_guessed)

            self.list_letter.append(letter)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"sorry, {letter} is not in the world.")
            print(f"You have {self.num_lives} lives left.") 
    
    def ask_letter(self):

            letter = input('Please guess a letter. ')
            if len(letter) != 1:
                 print('Please enter just one charachter. ')
            else:
                 self.check_letter(letter)
                 
