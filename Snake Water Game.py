import random

# Winning combinations
wins = {
    "s": "w",  # Snake beats Water
    "w": "g",  # Water beats Gun
    "g": "s"   # Gun beats Snake
}

def game_win(user, computer):
    if user == computer:
        return None
    return wins[user] == computer

user_score = 0
computer_score = 0
rounds = 3

choices = ["s", "w", "g"]

print("=== Snake Water Gun ===")

for round_no in range(1, rounds + 1):
    print(f"\n----- Round {round_no} -----")

    computer = random.choice(choices)

    user = input("Enter Snake(s), Water(w), Gun(g): ").lower()

    if user not in choices:
        print("Invalid Choice! Round Skipped.")
        continue

    result = game_win(user, computer)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if result is None:
        print("Round Draw!")
    elif result:
        print("You Win This Round!")
        user_score += 1
    else:
        print("Computer Wins This Round!")
        computer_score += 1

# Final Result
print("\n===== FINAL SCORE =====")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("🎉 Congratulations! You Won The Game!")
elif computer_score > user_score:
    print("💻 Computer Won The Game!")
else:
    print("🤝 Match Draw!")
