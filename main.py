import random
user_guess = input("Guess a number between 1 and 10 (Inclusive) \n —>")
random_number = random.randint(1,10)
user_score = 0

# MAIN PROGRAM
def game():
  if random_number == user_guess:
    user_score += 1
    print(f"You guessed correctly! 😀 Your score is currently {user_score}")
  else:
    print("Unlucky")
