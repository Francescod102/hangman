
import random

word_list = ["bluberry", "oranges" , "banana" , "apple" , "pineapple"]
print('word_list')


word = random.choice(word_list)

print(word)

guess = input("Enter a sigle letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("wrong guess ! that is not a valid input.")

    