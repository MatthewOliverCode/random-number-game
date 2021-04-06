import random
user_score = 0
lower_bound = int(input("Enter the lowest number that you want to guess \n\t—> "))
upper_bound = int(input("Enter the highest number that you want to guess \n\t—> "))
question_amount = int(input("How many questions would you like to do? \n\t—> "))

# MAIN PROGRAM
def game(user_score,lower,upper,num_questions):

  for _ in range(num_questions):
    rand_num = str(random.randint(lower,upper))
    user_guess = input(f"Guess a number between {lower} and {upper} \n\t—> ")

    if rand_num == user_guess:
      user_score += 1
      print(f"You guessed correctly! :D Your score is currently {user_score}")
    else:
      print("Unlucky")
  print(f"Your score is {user_score} / {num_questions}")

game(user_score,lower_bound,upper_bound,question_amount)