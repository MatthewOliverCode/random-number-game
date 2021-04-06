import random
from VividHues import Clr
user_score = 0
lower_bound = int(input(f"Enter the {Clr.BOLD}lowest{Clr.RESET} number that you want to guess \n\t—> "))
upper_bound = int(input(f"Enter the {Clr.BOLD}highest{Clr.RESET} number that you want to guess \n\t—> "))
question_amount = int(input(f"How many {Clr.BOLD}questions{Clr.RESET} would you like to do? \n\t—> "))

# MAIN PROGRAM
def game(user_score,lower,upper,num_questions):

  for _ in range(num_questions):
    rand_num = str(random.randint(lower,upper))
    user_guess = input(f"Guess a number between {Clr.BOLD}{lower}{Clr.RESET} and {Clr.BOLD}{upper}{Clr.RESET} \n\t—> ")

    if rand_num == user_guess:
      user_score += 1
      print(f"You guessed correctly! :D Your score is currently {Clr.BOLD}{user_score}{Clr.RESET}")
    else:
      print("Unlucky")
  print(f"Your score is {Clr.BOLD}{user_score}{Clr.RESET} / {Clr.BOLD}{num_questions}")

game(user_score,lower_bound,upper_bound,question_amount)