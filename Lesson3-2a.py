import random
num1 = random.randrange(0,9)
num2 = random.randrange(0,9)
if num1 < num2:
  num1, num2 = num2, num1
i = True
while i == True:
  userGuess = eval(input(f"What is {num1} - {num2}: "))
  if userGuess == num1 - num2:
    print("You got it!")
    i = False
  else:
    print("Wrong answer. Try again.")