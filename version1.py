import random

magic_number = random.randint (1, 10)
print(magic_number)

user_number = int(input("Guess a number between 1 and 10: "))

if magic_number == user_number:
  print("You win!")
else:
  print("You lose!")
