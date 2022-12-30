import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}

    return choices
    
def check_win(player, computer):
    print("You chose " + player + ", computer chose " + computer + ".")
    print(f"You chose {player} and computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "paper") or (player == "scissors" and computer == "rock") or (player == "paper" and computer == "scissors"):
        return "You lost :("
    else:
        return "You won :)"
    return [player, computer]


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

# def greeting():
#     return "Hi"

# response = greeting()
# print(response)