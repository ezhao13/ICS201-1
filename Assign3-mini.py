# ------------------------------
# Evan Zhao
# ICS2O1-2
# Mini Assignment - Calculator
# ------------------------------

# imports the random module to use its functions
import random

# loops the program infinitely
while True:

  # displays the selection menu 
  print("Main menu")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")

  # asks user for a choice from the above menu
  userChoice = eval(input("Enter a choice: "))

  # generates the random numbers later used in the questions
  num1 = random.randint(0,9)
  num2 = random.randint(0,9)

  # enters this statement if the user entered 1
  if userChoice == 1:
    # prints out the addition question
    userAnswer = eval(input(f"What is {num1} + {num2}? "))
    # calculates the answer to the question
    answer = num1 + num2
    
    # displays to the user if their answer were correct or not
    if userAnswer == answer:
      print("Correct\n")    
    else:
      print(f"Your answer is wrong. The correct answer is {answer}\n")

  # enters this statement if the user entered 2
  elif userChoice == 2:

    # makes sure that the first number is always bigger so the answer is not negative
    if num2 > num1:
      num1, num2 = num2, num1

    # prints out the subtraction question
    userAnswer = eval(input(f"What is {num1} - {num2}? "))
    # calculates the answer to the question
    answer = num1 - num2

    # displays to the user if their answer were correct or not
    if userAnswer == answer:
      print("Correct\n")
    else:
      print(f"Your answer is wrong. The correct answer is {answer}\n")

  # enters this statement if the user entered 3
  elif userChoice == 3:

    # prints out the multiplication question
    userAnswer = eval(input(f"What is {num1} x {num2}? "))
    # calculates the answer to the question
    answer = num1 * num2

    # displays to the user if their answer were correct or not
    if userAnswer == answer:
      print("Correct\n")
    else:
      print(f"Your answer is wrong. The correct answer is {answer}\n")

  # enters this statement if the user entered 4
  elif userChoice == 4:

    # makes sure that the second number is not 0
    num2 = random.randint(1,9)
    # prints out the division question
    userAnswer = eval(input(f"What is {num1} / {num2}? "))
    # calculates and rounds the answer to the question
    answer = num1 // num2

    # displays to the user if their answer were correct or not
    if userAnswer == answer:
      print("Correct\n")
    else:
      print(f"Your answer is wrong. The correct answer is {answer}\n")

  # enters this statement if the user entered 5 and ends the loop 
  elif userChoice == 5:
    print("Thank you for using the calculator application! ")
    break

  # enters this statement if the user did not enter a number from 1 - 5 and displays
  else:
    print("Enter a valid number!\n")