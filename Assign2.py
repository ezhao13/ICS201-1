#------------------------------------------------------
#Evan Zhao
#ICS201-2
#Assignment 2
#------------------------------------------------------

#Question 1
print("Question 1")
print()

#Asks user for a number between 1 and 10
userNumber = eval(input("Enter a number between 1 and 10 to be converted to roman numerals: "))
print()

#Checks the value inputted and uses that to print the roman numeral of that number
if userNumber == 1:
  print("The roman numeral of that number is I")
  
elif userNumber == 2:
  print("The roman numeral of that number is II")
  
elif userNumber == 3:
  print("The roman numeral of that number is III")
  
elif userNumber == 4:
  print("The roman numeral of that number is IV")
  
elif userNumber == 5:
  print("The roman numeral of that number is V") 
  
elif userNumber == 6:
  print("The roman numeral of that number is VI") 
  
elif userNumber == 7:
  print("The roman numeral of that number is VII")
  
elif userNumber == 8:
  print("The roman numeral of that number is VIII")
  
elif userNumber == 9:
  print("The roman numeral of that number is IX")  
  
elif userNumber == 10:
  print("The roman numeral of that number is X")  
  
else:
  print("Enter a whole number between 1 and 10.")
  
#Question 2
print("\nQuestion 2")
print()

#Asks user for the numeric form of a month, date and the last two digits of the year (it keeps the leading zeroes of the year as it is stored as a string)
month = eval(input("Enter a month in numeric form: "))
date = eval(input("Enter a date: "))
year = input("Enter a two-digit year: ")
print()

#Checks if month * date is equal to the year (converted to integer) and prints magic if it is true and not magic if false 
if month * date == int(year):
  print(f"The date {month}/{date}/{year} is magic.")
  
else:
  print(f"The date {month}/{date}/{year} is not magic.")

#Question 3
print("\nQuestion 3")
print()

#Asks user for length and width of a rectangle
length1 = eval(input("Enter length of the first rectangle: "))
width1 = eval(input("Enter width of the first rectangle: "))
print()
length2 = eval(input("Enter length of the second rectangle: "))
width2 = eval(input("Enter width of the second rectangle: "))
print()

#Calculates area
area1 = length1 * width1
area2 = length2 * width2

#Checks which area is bigger and prints the results
if area1 > area2:
  print("The first rectangle has the bigger area.")
  
elif area1 < area2:
  print("The second rectangle has the bigger area.")
  
else:
  print("The area of both the rectangles are the same.")

#Question 4
print("\nQuestion 4")
print()

#Asks user for weight and height
personWeight = eval(input("Enter weight in pounds: "))
personHeight = eval(input("Enter height in inches: "))
print()

#Calculates body mass index
bodyMassIndex = personWeight * 703 / personHeight ** 2

#Checks if the body mass index is underweight, overweight or optimal weight and prints it
if bodyMassIndex < 18.5:
  print("The person is underweight.")
  
elif bodyMassIndex > 25:
  print("The person is overweight.")
  
else:
  print("The person is optimal weight.")

#Question 5
print("\nQuestion 5")
print()

#Asks user for the number of seconds
time = eval(input("Enter the number of seconds: "))
print()

#Checks if the number of seconds is at least one day, hour or minute and prints it to the largest unit with the remaining seconds
if time >= 86400:
  days = time // 86400
  seconds = time % 86400
  print(f"The number of days in {time} seconds is {days} days and {seconds} seconds.")

elif time >= 3600:
  hours = time // 3600
  seconds = time % 3600
  print(f"The number of hours in {time} seconds is {hours} hours and {seconds} seconds.")

elif time >= 60:
  minutes = time // 60
  seconds = time % 60
  print(f"The number of hours in {time} seconds is {minutes} minutes and {seconds} seconds.")
  
else:
  print(f"The number of seconds is {time}.")

#Question 6
print("\nQuestion 6")

#Asks user for the number of pennies, nickels, dimes and quarters
pennies = eval(input("Enter the number of pennies: "))
nickels = eval(input("Enter the number of nickels: "))
dimes = eval(input("Enter the number of dimes: "))
quarters = eval(input("Enter the number of quarters: "))
print()

#Calculates the total change 
totalChange = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25

#Checks if the total change was greater, less than or equal to $1.00 and prints it 
if totalChange > 1:
  print(f"The value of the coins were ${totalChange-1:.2f} too much.")
  
elif totalChange < 1:
    print(f"The value of the coins were ${1-totalChange:.2f} too little.")
  
else:
  print("Congratulations! The value of the coins were exactly $1.00.")

#Question 7
print("\nQuestion 7")
print()

#Asks user for the month and year
month2 = eval(input("Enter a month (1-12): "))
year2 = eval(input("Enter a year: "))
print()

#Checks if it a month with 31 days, 30 days or February
if month2 == 1 or month2 == 3 or month2 == 5 or month2 == 7 or month2 == 8 or month2 == 10 or month2 == 12:
  print("31 days")
  
elif month2 == 4 or month2 == 6 or month2 == 9 or month2 == 11:
  print("30 days")
  
elif month2 == 2:
  
#Checks if the year is a leap year and prints the number of days in that February
  if year2 % 100 == 0 and year2 % 400 != 0:
    print("28 days")
    
  elif year2 % 4 == 0:
    print("29 days") 
    
  else:
    print("28 days")
    
else:
  print("Enter a valid month between 1-12.")

#Question 8
print("\nQuestion 8")
print()

#Asks user for the weight of package in kilograms and miles shipped
kilograms = eval(input("Enter the weight of package in kilograms: "))
miles = eval(input("Enter the number of miles shipped: "))
print()

#Checks if the distance is within parameters
if miles > 10 and miles < 3000:

#Checks the weight of package, calculate the shipping charge and print it
  if kilograms <= 2:
    print(f"The shipping charge is ${1.1 * miles/500:.2f}.") 
    
  elif kilograms > 2 and kilograms <= 6:
    print(f"The shipping charge is ${2.2 * miles/500:.2f}.")
    
  elif kilograms > 6 and kilograms <= 10:
    print(f"The shipping charge is ${3.7 * miles/500:.2f}.")
    
  elif kilograms > 10 and kilograms <= 20:
    print(f"The shipping charge is ${4.8 * miles/500:.2f}.")
    
  else:
    print("Enter a weight in kilograms more than zero and less than 20.")
    
else:
  print("Enter a distance in miles more than 10 and less than 3,000.")

#Question 9
print("\nQuestion 9")
print()

#Asks user for the number of calories and fat grams in a food
calories = eval(input("Enter the number of calories in the food: "))
fat = eval(input("Enter the number of fat grams in the food: "))
print()

#Calculates total calories
totalCalories = calories + fat * 9

#Calculates the percentage of calories from fat by dividing the calories from fat by the total calories
fatCalories = fat * 9 / totalCalories * 100

#Checks that the calories and fat are not smaller than 0
if calories >= 0 and fat >= 0:

#Checks if the percentage of calories from fat is low or if the fat and calories were incorrectly entered, prints percentage of calories from fat
  if fatCalories < 30:
    print(f"The calories from fat is {round(fatCalories,2)}% of the total calories.")
    print("The food is low in fat.")
    
  elif fatCalories >= 30 and fatCalories < 100:
    print(f"The calories from fat is {round(fatCalories,2)}% of the total calories.")
    
  else:
    print("The calories or the fat grams were incorrectly entered.")
    print("Please make sure the calories from fat is less than the total calories.")
    
else:
  print("Please make sure the calories and fat grams are not less than 0.")

#Question 10
print("\nQuestion 10")
print()

#Displays the choices of the calculator
print("1. Calculate the Area of a Circle")
print("2. Calculate the Area of a Rectangle")
print("3. Calculate the Area of a Triangle")
print("4. Quit")
print()

#Asks user for their choice
choice = int(input("Enter your choice (1-4): "))
print()

#Checks the inputted choice and asks the user for the needed dimensions, calculates the area of the shape and prints it out
if choice == 1:
  radius = eval(input("Enter the radius of the circle: "))

#Checks if the radius is non negative and prints out the area
  if radius >= 0:
    print(f"The area of the circle is {round(radius**2*3.14159,2)} units²")
    
  else:
    print("Enter a non negative number for the radius.")
    
elif choice == 2:
  length = eval(input("Enter the length of the rectangle: "))
  width = eval(input("Enter the width of the rectangle: "))

#Checks if the length and width is non negative and prints out the area
  if length >= 0 and width >= 0:
    print(f"The area of the rectangle is {round(length*width,2)} units²")
    
  else:
    print("Enter a non negative number for the length and width.")
    
elif choice == 3:
  base = eval(input("Enter the base of the triangle: "))
  height = eval(input("Enter the height of the triangle: "))

#Checks if the base and height is non negative and prints out the area
  if base >= 0 and height >= 0:
    print(f"The area of the triangle is {round(base*height/2,2)} units²")
    
  else:
    print("Enter a non negative number for the base and height.")
    
elif choice == 4:
  print("Thanks for using geometry calculator!")
  exit()
  
else:
  print("Please enter a valid number!")