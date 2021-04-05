import random
user_guess = input("Guess a number between 1 and 10 (Inclusive) \n\t—> ")
random_number = random.randint(1,10)
user_score = 0

# MAIN PROGRAM
def game(rand_num,user_guess,user_score):
  if rand_num == user_guess:
    user_score += 1
    print(f"You guessed correctly! :D Your score is currently {user_score}")
  else:
    print(f"Unlucky. The randomly generated number was {rand_num}")
game(random_number,user_guess,user_score)