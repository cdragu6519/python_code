import random
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


turns = 0
pPoints = 0
cPoints = 0


# def evaluate(choicePlayer, choiceComputer):


while turns < 3:
    player = input("Choose Rock, Paper, or Scissors: ")

    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    print(f"Computers choice: {computer}")

    # "Rock", "Paper", "Scissors" = [1, 2, 3]

    decision = {("R", "R")}

    if player < computer:
        print(f"{computer} beats {player}, Computer wins this round!")
        cPoints += 1
    if player == computer:
        print(f"{player} equals {computer}, Tie!")
        cPoints += 1
        pPoints += 1
    if player > computer:
        print(f"{player} beats {computer}, You win this round!")
        pPoints += 1

    turns += 1

if turns == 3:
    print(f"The final scores are... Player:{pPoints} and Computer:{cPoints}")
    if pPoints > cPoints:
        print("Player wins!!!")
    if cPoints > pPoints:
        print("Computer wins!!!")
    elif cPoints == pPoints:
        print("It was a tie!!!")
