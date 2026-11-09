# Rock Paper Scissors Game (Command Line)

# ORGANIZATIONAL STRUCTURE OF OUR PYTHON FILE

# 1. IMPORTS AT THE TOP
import random

# 2. FOLLOWED BY ANY CONSTANTS
VALID_OPTIONS = ["rock", "paper", "scissors"]

# 3. FUNCTIONS OR CLASSES

def determine_winner(u, c):
    if u == "rock" and c == "rock":
        # print("TIE GAME")
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        # print("COMPUTER WINS")
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        # print("USER WINS")
        return "USER WINS"
    elif u == "paper" and c == "rock":
        # print("USER WINS") 
        return "USER WINS"
    elif u == "paper" and c == "paper":
        #print("TIE GAME")
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        # print("COMPUTER WINS") 
        return "COMPUTER WINS"
    elif u == "scissors" and c == "rock":
        # print("COMPUTER WINS")
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        # print("USER WINS")
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        # print("TIE GAME")
        return "TIE GAME"

# 4. MAIN CONDITIONAL

if __name__ == "__main__":
    # ONLY RUN THE CODE BELOW
    # IF WE EXECUTE THIS FILE FROM THE COMMAND LINE
    # BUT NOT IF WE IMPORT FROM THIS FILE

    # ASK USER FOR AN INPUT (R/P/S)

    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    print("USER:", user_choice)

    # VALIDATIONS

    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        # exit()
        quit()

    # GENERATE RANDOM COMPUTER CHOICE

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMP:", computer_choice)

    # DETERMINE THE WINNER

    winner = determine_winner(u=user_choice, c=computer_choice)
    print(winner)