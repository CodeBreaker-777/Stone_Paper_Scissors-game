import random

def print_rules():
    print("RULES of the game:")
    print("1. Stone crushes Scissors\n2. Paper covers Stone\n3. Scissors cut Paper")
    print("\nTUTORIAL:")
    print("If you select stone and the computer selects paper, the computer wins.")
    print("If you select scissors and the computer selects paper, you win.")
    print("If you select scissors and the computer selects stone, the computer wins.")

def play_game():
    game_objects = ["stone", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nUse 'exit' to end the game.")
        print("Available choices:", game_objects)
        player = input("Enter your object: ").lower()
        
        if player == "exit":
            print("Game Over!")
            print(f"Final Score - You: {user_score} | Computer: {computer_score}")
            break
        
        if player not in game_objects:
            print("Invalid choice, please try again.")
            continue
        
        computer = random.choice(game_objects)
        print("Computer chose:", computer)
        
        if player == computer:
            print("Match Draw")
        elif (player == "stone" and computer == "scissors") or \
             (player == "paper" and computer == "stone") or \
             (player == "scissors" and computer == "paper"):
            print("Congratulations! You win!")
            user_score += 1
        else:
            print("You lose! Computer wins.")
            computer_score += 1

if __name__ == "__main__":
    print_rules()
    play_game()
