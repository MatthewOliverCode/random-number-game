import random


user_score = 0

# MAIN PROGRAM
def game(user_score):
  rand_num = str(random.randint(1,10))

  for _ in range(0,5):
    user_guess = input("Guess a number between 1 and 10 (Inclusive) \n\t—> ")

    if rand_num == user_guess:
      user_score += 1
      print(f"You guessed correctly! :D Your score is currently {user_score}")
    else:
      print("Unlucky")
game(user_score)