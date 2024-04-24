#----------------------
#Evan Zhao
#ICS2O1-2
#Assignment 3
#----------------------

#Question 1
print("Question 1\n")

# asks user for an initial value 
userValues = eval(input("Enter value #1 (0 to end process): "))

# makes sure that initial value is not zero and displays error
if userValues == 0:
  print("Zero cannot be the initial value.")

else:

  # sets an initial value for counter and calculate
  counter = 0
  calculate = 0

  # uses a while loop to loop until sentinel value 0 is detected  
  while userValues != 0:

    # increases counter by 1, increases calculate by the user value, and finds the average by dividing calculate (sum) by counter (total numbers)
    counter += 1
    calculate += userValues
    average = calculate/counter

    # asks user for a value again for the loop
    userValues = eval(input(f"Enter value #{counter+1} (0 to end process): "))

  # prints the average after exiting the loop
  print()
  print(f"The average is {round(average,2)}")

#Question 2
print("\nQuestion 2\n")

# prints the heading of the table
print(f"{'Degrees Celsius':<17}{'Degrees Fahrenheit'}")
print("------------------------------------")

# sets an initial vaue for celsius
celsius = 0

# uses a while loop to print the table and make sure celsius is limited to 100 degrees
while celsius <= 100:

  # calculates celsius to fahrenheit
  fahrenheit = celsius * 9 / 5 + 32

  # prints and formats the table values
  print(f"{celsius:<17}{fahrenheit}")

  # increase celsius by 5 for the loop
  celsius += 5
  
#Question 3
print("\nQuestion 3\n")

# prints the heading of the table
print(f"{'Year':<7}{'Tuition($)'}")
print("------------------")

# sets an initial value for year and total tuition 
year = 0
totalTuition = 0

# uses while loop to make sure the table does not go past year 14
while year <= 14:

  # calculates tuition based on the year
  tuition = 10000 * 1.05 ** year
  # prints and formats the table values
  print(f"{year:<7}{tuition:.2f}")

  # adds together the tuition when the year is between 11 and 14
  if year >= 11:
    totalTuition += tuition

  # increases the year by 1 for the loop
  year += 1
  
print("***************************************************")
print(f"* Total Tuition for the last 4 years is ${totalTuition:.2f} *")
print("***************************************************")

#Question 4
print("\nQuestion 4\n")

# asks user for number of students
students = eval(input("Enter the number of students: "))

# uses while loop makes sure that there is at least 2 students 
while students < 2:
  # reprompts the user to enter number of students
  print("The number of students must be 2 at least")
  students = eval(input("Enter the number of students: "))

# asks user for the initial 2 students and their scores
student1 = input("Enter a student name: ")
score1 = eval(input("Enter a student score: "))
student2 = input("Enter a student name: ")
score2 = eval(input("Enter a student score: "))

# makes sure that student1 is assigned the better score and the student
if score1 < score2:
  student1, score1, student2, score2 = student2, score2, student1, score1

# sets an initial value for i to use for a loop
i = 0

# uses while loop so it loops the number of students - 2 
while i < students - 2:

  # asks user for more students and their scores
  name = input("Enter a student name: ")
  score = eval(input("Enter a student score: "))

  # replaces current student1 and/or student2 with a higher score and student appropriately
  if score1 < score:    
    student2, score2 = student1, score1
    student1, score1 = name, score

  elif score2 < score:  
    student2 = name
    score2 = score

  # increases i by 1 for the loop
  i += 1

# prints the top two students and their score
print("Top two students:")
print(f"{student1}'s score is {score1}")
print(f"{student2}'s score is {score2}")

#Question 5
print("\nQuestion 5\n")

# asks user for the first point of polygon
xFirst = eval(input("Enter the x-coordinate of the point: "))
yFirst = eval(input("Enter the y-coordinate of the point: "))

# asks user for an initial last point of polygon 
xLast = eval(input("Enter the x-coordinate or blank to finish: "))
yLast = eval(input("Enter the y-coordinate or blank to finish: "))

# sets an initial value for the perimeter by using pythagorean theorem to find the distance between the points
perimeter = ((xFirst - xLast)**2 + ((yFirst - yLast)**2))**(1 / 2)

# uses while loop to repeat the program
while True:

  # asks user for the x-coordinate of a point
  xValue = input("Enter the x-coordinate or blank to finish: ")

  # checks if a blank was entered
  if xValue == "":
    break

  # converts x-coordinate into a numberic value if it is not a blank
  xValue = eval(xValue)

  # asks user for the x-coordinate of a point
  yValue = input("Enter the y-coordinate or blank to finish: ")

  # checks if a blank was entered
  if yValue == "":
    break

  # converts y-coordinate into a numberic value if it is not a blank
  yValue = eval(yValue)

  # calculates the distance from the previous point to current point
  perimeter += ((xValue - xLast)**2 + ((yValue - yLast)**2))**(1 / 2)
  # sets the current point to previous point 
  xLast = xValue
  yLast = yValue

# calculates the closing side of the polygon
perimeter += ((xLast - xFirst)**2 + ((yLast - yFirst)**2))**(1 / 2)

# prints perimeter of the polygon
print()
print(f"The perimeter of the polygon is {round(perimeter,2)}.")

#Question 6
print("\nQuestion 6\n")

# sets an initial value for admission ticket
admission = 0

# uses while loop to repeatly run the program 
while True:

  # asks user for the age of guest
  age = input("Enter the age of the guest: ")

  # checks if blank is inputted and exits the loop
  if age == "":
    break

  # converts age into a numberic value if it is not a blank
  age = eval(age)

  # checks the age using if elif statement and increases admission by appropriate price
  if age >= 3 and age <= 12:
    admission += 14

  elif age >= 65:
    admission += 18

  elif age > 12 and age < 65:
    admission += 23

# prints admission cost with 2 decimal places
print()
print(f"The admission cost for the group is ${admission:.2f}")