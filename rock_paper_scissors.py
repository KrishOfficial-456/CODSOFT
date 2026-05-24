import random

print("----- ROCK PAPER SCISSORS GAME -----")
print("Instructions to play : Type rock, paper, or scissors to play.\n")

x = 0   # user score
y = 0   # computer score

while True:

    user = input("Enter your choice (rock/paper/scissors): ").lower()

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.\n")
        continue

    choices = ["rock", "paper", "scissors"]
    comp = random.choice(choices)

    print("\nYou chose:", user)
    print("Computer chose:", comp)

    # Game logic
    if user == comp:
        print("Result: It's a Tie!")

    elif ((user == "rock" and comp == "scissors") or
          (user == "scissors" and comp == "paper") or
          (user == "paper" and comp == "rock")):

        print("Result: You Win!")
        x += 1

    else:
        print("Result: Computer Wins!")
        y += 1

    # Display scores
    print("\nScores:")
    print("Your Score:", x)
    print("Computer Score:", y)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        break

    print("\n - - - - NEW ROUND - - - -\n")