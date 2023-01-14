from milestone_4 import Hangman


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while True:
        game.ask_letter()
        if game.num_lives == 0:
            print("you lost")
            break

        elif game.num_letters > 0:
            game.check_guess("a")
            print("Congratulation")
            break
        
if __name__ == '__main__':
    word_list = ["bluberry", "oranges" , "banana" , "apple" , "pineapple"]
    play_game(word_list)
