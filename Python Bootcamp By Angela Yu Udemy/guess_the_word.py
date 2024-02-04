# using random module
import random
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
# print(chosen_word)
remaining_attempts=5
while remaining_attempts>0:
    guess=input()
    if chosen_word==guess:
        print("Congratulations, you guessed the word correctly!")
        break
    else:
        remaining_attempts=remaining_attempts-1
        print("Incorrect guess\nremaining attempts: ",remaining_attempts)
if remaining_attempts==0:
    print("Sorry, you ran out of attempts. The correct answer was",chosen_word)



# without using random module
chosen_word = input("Enter a word for the game: ")
# print(chosen_word)
remaining_attempts = 5
while remaining_attempts > 0:
    guess = input("Enter your guess: ")
    if chosen_word == guess:
        print("Congratulations, you guessed the word correctly!")
        break
    else:
        remaining_attempts -= 1
        print(f"Wrong guess! Remaining attempts: {remaining_attempts}")
if remaining_attempts == 0:
    print("Sorry, you ran out of attempts. The correct answer was", chosen_word)



    