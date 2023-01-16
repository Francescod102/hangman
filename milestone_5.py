from milestone_4 import Hangman


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while True:
        game.ask_for_input()
        if game.num_lives == 0:
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
