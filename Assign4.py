#----------------------
#Evan Zhao
#ICS2O1-2
#Assignment 5
#----------------------
    
# This function prints the roof of the house
def Roof():
  print()
  print("  /\\")
  print(" /  \\")
  print("/____\\")

# This function prints the base of the house
def Base():
  print("|    |")
  print("|____|")

# This function prints the walkway
def Walk():
  print("  **")
  print("  **********")
  print()

# This function prints a rectangle with the parameters m and n as rows and columns respectively
def printRectangle(m, n):
  print()
 
  # Loops the amount of rows there are
  for rows in range(m):  
    # Uses a nested loop to loop how many columns in each row and print '*' character
    for columns in range(n):
      print("*", end = " ")
    # Prints a new row
    print()
  print()

# This function finds the greatest common factor from its parameter num1 and num2 
def GCF(num1, num2):
  print()
  
  # Uses if statement to make sure num1 is the smallest integer 
  if num1 > num2:
    num1, num2 = num2, num1
    
  # Loops from 1 to the smallest number 
  for factor in range(1, num1 + 1):
    # Uses if statement to check if the factor is divisible by both numbers and assigns the greatestFactor to it
    if num1 % factor == 0 and num2 % factor == 0:
      greatestFactor = factor
  
  # Returns the GCF value
  return greatestFactor

# This function uses the parameters a, b, and c to compute the value of x in a quadratic equation
def quadraticSolver(a, b, c):
  print()
  
  # Calculates the two potential roots
  pos = ((0-b)+(b**2-4*a*c)**(1/2))/(2*a)
  neg = ((0-b)-(b**2-4*a*c)**(1/2))/(2*a)
  # Calculates the root of the equation
  root = (b**2-4*a*c)
  
  # Uses if-elif-else statement to check is root is positive (2 roots), negative (no roots), or zero (one root)
  if root > 0:
    print(f"The roots of the equation are {round(neg,2)} and {round(pos,2)}.")
  elif root < 0:
    print("There are no real roots for this equation.")
  else:
    print(f"The root of the equation is {round(pos,2)}.")
  print()

# This function uses the parameters number and checks if it is prime
def isPrime(number):
  print()
  
  # Loops from 2 to number - 1
  for factor in range(2, number):
    # Uses if statement to check if number is composite and returns it
    if number % factor == 0:
      return f"The number {number} is not prime."
  
  # If the parameter was not composite it returns prime
  return f"The number {number} is prime."

# Imports random library to use for this question
import random

# This function plays a dicegame with the user
def diceGame():
  print()
  
  # Assigns initial points value to 1000
  points = 1000
  # Uses an infinite while loop
  
  while True:
    
    # Prints the current amount of points
    print(f"You have {points} points.")
    # Asks user how much they want to risk
    risk = eval(input("Points to risk: "))
    # Rolls the dice and assign the values
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    # Prints the roll value
    print(f"Roll is {roll1} and {roll2}")
    
    # Uses if-else statement to check if it is even or odd
    if (roll1 + roll2) % 2 == 0:
      # Tells the user they lost if it is even, subtracts the points accordingly
      print("You lose.")
      points -= risk
      
    else:
      # Tells the user they won if it is odd, adds the points accordingly
      print("You win.")
      points += risk * 2

    # Asks user if they want to play again
    again = input("Play Again? ")
    
    # Uses if-elif statement to see if the user wants to play again or not
    if again == "Y":
      print()
      # Continues the loop 
      continue
      
    elif again == "N":
      # Returns the points and ends the function
      return points

# This function displays the menu and asks the user for input, then calls the corresponding function 
def menu():

  # Uses an infinite while loop
  while True:
    
    # Prints the menu options
    print("1. House Function")
    print("2. Printing Pattern")
    print("3. GCF Function")
    print("4. Quadratic Solver")
    print("5. Prime Checker")
    print("6. Dice Game")
    print("7. Quit")
    # Asks user for their selection
    userChoice = eval(input("Enter your selection: "))
    
    # Uses if-elif-else statement to check user's selection
    if userChoice == 1:
      
      # Calls the Roof(), Base(), Walk() functions to display the house 
      Roof()
      Base()
      Walk()
      
    elif userChoice == 2:
      print()

      # Asks user for parameter argument m and n
      m = eval(input("Enter the number of rows: "))
      n = eval(input("Enter the number of columns: "))
      
      # Calls the printRectangle() function with parameter argument m and n 
      printRectangle(m, n)
      
    elif userChoice == 3:
      print()

      # Asks user for parameter argument num1 and num2
      num1 = eval(input("Enter the first number: "))
      num2 = eval(input("Enter the second number: "))
      
      # Calls and prints the GCF() with parameter argument num1 and num2
      print(f"The greatest common factor is {GCF(num1, num2)}")
      print()
      
    elif userChoice == 4:
      print()

      # Asks user for parameter argument a, b, and c
      a = eval(input("Enter the value for a: "))
      b = eval(input("Enter the value for b: "))
      c = eval(input("Enter the value for c: "))
  
      # Calls the quadraticSolver() with parameter argument a, b, and c
      quadraticSolver(a, b, c)
      
    elif userChoice == 5:
      print()

      # Asks user for parameter argument number
      number = eval(input("Enter the number to be checked: "))
  
      # Calls the isPrime() function and prints whether the number is prime with parameter argument number
      print(isPrime(number))
      print()
      
    elif userChoice == 6:
      
      # Calls and prints the returned final score of the dice game
      print(f"Final Score: {diceGame()}")
      print()
      
    elif userChoice == 7:
      # Prints goodbye and leaves the loop
      print()
      print("Goodbye!")
      break
      
    else: 
      # Displays error message, loop continues afterwards
      print("Enter a valid choice.")
    
# Calls the menu() function 
menu()
