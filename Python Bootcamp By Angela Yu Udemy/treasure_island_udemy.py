# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# choice=input("Where you want to go? \n Left or Right\n")
# if choice=="Right":
#     print("You fall into a hole.\n  Game Over")
# elif choice=="Left":
#     print("Step 1 completed.")
# else:
#     print("You are dead. Game Over")
# choice2=input("Do you want to Swim or Wait?\n Swim or Wait \n")
# if choice2=="Swim":
#     print("Attacked by trout.\n Game Over.")
# elif choice2=="Wait":
#     print("Step 2 completed.")
# else:
#     print("You are dead. Game Over")
# door=input("Which door do you want to enter?\n Blue\n Yellow\n Red \n")
# if door=="Blue":
#     print("Eaten by beasts.\n Game Over.")
# elif door=="Red":
#     print("Burned by fire.\n Game Over.")
# elif door=="Yellow":
#     print("Congratulations, You win")
# else:
#     print("You are dead. Game Over")


# import sys
# def game():
#     print("Welcome to Treasure Island.")
#     print("Your mission is to find the treasure.") 
#     choice = input("Where you want to go? \n Left or Right\n")

#     if choice == "Right":   
#         print("You fall into a hole.\nGame Over")
#         sys.exit()
#     elif choice == "Left":  
#         print("Step 1 completed.")
#     else:   
#         print("You are dead. Game Over")
#         sys.exit()

#     choice2 = input("Do you want to Swim or Wait?\n Swim or Wait \n")
#     if choice2 == "Swim":
#         print("Attacked by trout.\n Game Over.")
#         sys.exit()
#     elif choice2 == "Wait":
#         print("Step 2 completed.")
#     else:
#         print("You are dead. Game Over")
#         sys.exit()

#     door = input("Which door do you want to enter?\n Blue\n Yellow\n Red \n")
#     if door == "Blue":
#         print("Eaten by beasts.\n Game Over.")
#         sys.exit()
#     elif door == "Red":
#         print("Burned by fire.\n Game Over.")
#         sys.exit()
#     elif door == "Yellow":
#         print("Congratulations, You win")
#     else:
#         print("You are dead. Game Over")
#         sys.exit()

# def play_again():   
#     while True:
#         play_again=input("You wanna play again:\n If yes type Y if no type N\n")
#         if play_again=='Y':
#             game()
#         elif play_again=='N':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid input. Please enter Yes or No.")

# if __name__ == "__main__":
#     game()
#     # print("GAME OVER")
#     play_again()



import sys

def game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 
    choice = input("Where you want to go? \n Left or Right\n")

    if choice == "Right":   
        print("You fall into a hole.\nGame Over")
        return
    elif choice == "Left":  
        print("Step 1 completed.")
    else:   
        print("You are dead. Game Over")
        return

    choice2 = input("Do you want to Swim or Wait?\n Swim or Wait \n")
    if choice2 == "Swim":
        print("Attacked by trout.\n Game Over.")
        return
    elif choice2 == "Wait":
        print("Step 2 completed.")
    else:
        print("You are dead. Game Over")
        return

    door = input("Which door do you want to enter?\n Blue\n Yellow\n Red \n")
    if door == "Blue":
        print("Eaten by beasts.\n Game Over.")
        return
    elif door == "Red":
        print("Burned by fire.\n Game Over.")
        return
    elif door == "Yellow":
        print("Congratulations, You win")
    else:
        print("You are dead. Game Over")
        return

def play_again():   
    while True:
        play_again_input = input("Do you want to play again? If yes, type 'Y'. If no, type 'N'\n")
        if play_again_input == 'Y':
            game()
        elif play_again_input == 'N':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    game()
    play_again()
