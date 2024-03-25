# random word generated by the program itself using nltk module

import nltk
import random
nltk.download('words')
word_list=nltk.corpus.words.words()
chosen_word=random.choice(word_list)

remaining_attempts=5
while remaining_attempts>0:
    guess=input("Enter your guess:\n")
    if chosen_word == guess:
        print("Congratulations, you won! ")
        break
    else:
        remaining_attempts-=1
        print("Incorrect guess\nremaining attempts: ",remaining_attempts)
if remaining_attempts==0:
    print("Sorry, you ran out of attempts. The correct answer was",chosen_word)