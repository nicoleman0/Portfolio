# rock paper scissors against computer
from random import randint

print("Rock...") # 0
print("Paper...") # 1
print("Scissors...") # 2
player = input("Make your choice: ").lower()

rand_num = randint(0, 2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer plays {computer}")

if player == computer:
	print("Tie game.")
elif player == "rock" and computer == "scissors":
	print("You win.")
elif player == "paper" and computer == "rock":
	print("You win.")
elif player == "scissors" and computer == "paper":
	print("You win.")
else:
	print("You lost to the computer.")
