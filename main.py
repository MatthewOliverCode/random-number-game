import random
user_score = 0
lower_bound = int(input("Enter the lowest number that you want to guess \n\t—> "))
upper_bound = int(input("Enter the highest number that you want to guess \n\t—> "))

# MAIN PROGRAM
def game(user_score,lower,upper):
  
  for _ in range(0,5):
    rand_num = str(random.randint(lower,upper))
    user_guess = input(f"Guess a number between {lower} and {upper} \n\t—> ")

    if rand_num == user_guess:
      user_score += 1
      print(f"You guessed correctly! :D Your score is currently {user_score}")
    else:
      print("Unlucky")
  print(f"Your score was {user_score}")
game(user_score,lower_bound,upper_bound)