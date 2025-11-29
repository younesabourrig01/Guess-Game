# word list
words = ["apple", "green", "proud", "black", "hello"]

# import random library
import random

def solo_mode():
    # select random word
    secret_word = random.choice(words)
    
    # player display board
    board = ["*"] * len(secret_word)
    
    # initialize variables
    max_attempts = 5
    attempts = 0

    print("Enjoy the solo mode!")
    player_name = input("Enter your preferred name: ")

    while attempts < max_attempts:
        print(" ".join(board))

        # ask player for word with validation
        player_guess = input("Enter a 5-letter word: ").lower().strip()
        if len(player_guess) != len(secret_word):
            print("The word must contain exactly 5 letters!")
            continue

        # test player's word
        for i, letter in enumerate(player_guess):
            if letter in secret_word:
                if letter == secret_word[i]:
                    board[i] = letter
                else:
                    print(f"The letter '{letter}' is in the word but not in the correct position.")

        if "".join(board) == secret_word:
            print(f"Congratulations {player_name}! You guessed the word '{secret_word}' in {attempts + 1} attempts.")
            return

        attempts += 1

    print(f"Game over {player_name}!")
    print(f"The word was: '{secret_word}'")

def two_player_mode():
    scores = {"Player 1": 0, "Player 2": 0}

    print("Enjoy the multiplayer mode!")
    for round in range(2):
        current_player = "Player 1" if round % 2 == 0 else "Player 2"
        opponent = "Player 2" if current_player == "Player 1" else "Player 1"

        print(f"{current_player}, enter a 5-letter word: ")
        while True:
            secret_word = input().lower()
            if len(secret_word) == 5 and secret_word.isalpha():
                break
            print("The word must contain exactly 5 letters!")

        # Clear screen to hide the word
        print("\033c", end="")  
        board = ["*"] * len(secret_word)
        max_attempts = 5
        attempts = 0

        print(f"{opponent}, it's your turn to guess the word!")

        while attempts < max_attempts:
            print("\n" + " ".join(board))
            player_guess = input("Enter a 5-letter word: ").lower().strip()

            if len(player_guess) != len(secret_word):
                print("The word must contain exactly 5 letters!")
                continue

            for i, letter in enumerate(player_guess):
                if letter in secret_word:
                    if letter == secret_word[i]:
                        board[i] = letter
                    else:
                        print(f"The letter '{letter}' is in the word but not in the correct position.")

            if "".join(board) == secret_word:
                print(f"\nCongratulations {opponent}! You guessed the word '{secret_word}' in {attempts + 1} attempts.")
                scores[opponent] += 1
                break

            attempts += 1

        if attempts == max_attempts:
            print(f"\nSorry {opponent}, you didn't guess the word. The word was '{secret_word}'.")

    print("Final scores:")
    for player, score in scores.items():
        print(f"{player}: {score} point(s)")

    winner = max(scores, key=scores.get)
    print(f"Congratulations {winner}, you won!")

# Main menu to choose game mode
if __name__ == "__main__":
    print("=== WORD GUESSING GAME ===")
    print("1. Solo Mode")
    print("2. Two Player Mode")
    
    choice = input("Choose game mode (1 or 2): ").strip()
    
    if choice == "1":
        solo_mode()
    elif choice == "2":
        two_player_mode()
    else:
        print("Invalid choice. Please restart the program.")