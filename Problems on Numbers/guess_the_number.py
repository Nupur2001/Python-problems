# # # without using random module
num=int(input())

remaining_attempts=5
while remaining_attempts>0:
    guess=int(input("Enter your guess: "))
    if num==guess:
        print("Congratulations! You got it right.")
        break
    elif abs(guess-num)<=5:    # Check if guess is within 5 of the secret number
        remaining_attempts-=1
        print("Close! Try again \nremaining attempts: ", remaining_attempts)
    elif num>guess:
        remaining_attempts-=1
        print("Too high\nremaining attempts: ", remaining_attempts)
    else:
        remaining_attempts-=1
        print("Too low\nremaining attempts: ", remaining_attempts)
if remaining_attempts==0:
    print("You have used up all of your attempts. The number was", num)

# # using random module
import random
chosen_numbers = list(range(1, 101))  
random_number = random.choice(chosen_numbers)
print(random_number)
remaining_attempts = 5
while remaining_attempts > 0:
    guess = int(input("Enter your guess(1, 100): "))
    if guess == random_number:
        print("Congratulations! You guessed the number.")
        break
    elif abs(guess-random_number)<=5:
        remaining_attempts-=1
        print("Close! Try again \nremaining attempts: ", remaining_attempts)
    elif guess > random_number:
        remaining_attempts-=1
        print("Too high \nRemaining attempts:", remaining_attempts)
    else:
        remaining_attempts -= 1
        print("Too low \nRemaining attempts:", remaining_attempts)
if remaining_attempts == 0:
    print("Sorry, you ran out of attempts. The correct answer was", random_number)

