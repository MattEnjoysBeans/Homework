# Lesson 9
from random import choice
# input
player_choice = ""
# make sure input is valid
while True:
    player_choice = input("Enter 'Rock' 'Paper' or 'Scissors': ")
    player_choice = player_choice.lower()
    if player_choice in {"rock", "paper", "scissors"}:
        break

cpu_choice = choice(["rock", "paper", "scissors"])
print(f"CPU Chose: {cpu_choice}")

if player_choice == cpu_choice:
    print("Tie")
else:
    match player_choice:
        case "rock":
            if cpu_choice == "paper":
                print("CPU wins")
            else:
                print("Player wins")
        case "paper":
            if cpu_choice == "scissors":
                print("CPU wins")
            else:
                print("Player wins")
        case _:
            if cpu_choice == "rock":
                print("CPU wins")
            else:
                print("Player wins")

