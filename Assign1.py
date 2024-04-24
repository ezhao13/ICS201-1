#Evan Zhao ICS201-2

#Question 1
print("Question 1")
price = eval(input("Enter price of item: "))
print(f"You brought an item for {price} cents and gave me a dollar, so your change is:")

#Calculates number of quarters, dimes and nickels
quarters = (100-price)//25
dimes = (100-price)%25//10
nickels = (100-price)%25%10//5
#Prints code
print(f"{quarters} quarters")
print(f"{dimes} dimes")
print(f"{nickels} nickels")

#Question 2
print("\nQuestion 2")

#Asks user for input
print("----------------------------------")
item1 = input("Input name of item 1: ")
quantity1 = eval(input("Input quantity of item 1: "))
price1 = eval(input("Input price of item 1: "))
print("----------------------------------")
item2 = input("Input name of item 2: ")
quantity2 = eval(input("Input quantity of item 2: "))
price2 = eval(input("Input price of item 2: "))
print("----------------------------------")
item3 = input("Input name of item 3: ")
quantity3 = eval(input("Input quantity of item 3: "))
price3 = eval(input("Input price of item 3: "))
print()

#Calculates subtotal
subtotal = quantity1*price1+quantity2*price2+quantity3*price3

#Prints out, calculates, formats and rounds total bill
print("Your bill:")
print(f"{subtotal*1.0625:35.2f}")
print()

#Stores user inputted variables and/or strings into another variable to help format later
r1 = f"{item1} {quantity1} @ ${price1:.2f} each"
r2 = f"{item2} {quantity2} @ ${price2:.2f} each"
r3 = f"{item3} {quantity3} @ ${price3:.2f} each"
sub = "subtotal"
tax = "6.25% sales tax"
tot1 = "Total"

#Prints out formatted item prices, subtotal, tax and total bill
print(f"{r1:<40}{quantity1*price1:.2f}")
print(f"{r2:<40}{quantity2*price2:.2f}")
print(f"{r3:<40}{quantity3*price3:.2f}")
print(f"{sub:<40}{subtotal:.2f}")
print(f"{tax:<40}{0.0625*subtotal:.2f}")
print(f"{tot1:<40}{1.0625*subtotal:.2f}")

#Question 3
print("\nQuestion 3")

#Asks user for input
name1 = input("Name of Assessment 1: ")
score1 = eval(input(f"Score received for {name1}: "))
points1 = eval(input(f"Total points possible for {name1}: "))
name2 = input("Name of Assessment 2: ")
score2 = eval(input(f"Score received for {name2}: "))
points2 = eval(input(f"Total points possible for {name2}: "))
name3 = input("Name of Assessment 3: ")
score3 = eval(input(f"Score received for {name3}: "))
points3 = eval(input(f"Total points possible for {name3}: "))
print()

#Stores user inputted variables and/or string into another variable to help format later
n1 = f"{name1}:"
n2 = f"{name2}:"
n3 = f"{name3}:"
tot2 = "Total:"

#Prints out formatted scores
print(f"{n1:<30}{score1} out of {points1}")
print(f"{n2:<30}{score2} out of {points2}")
print(f"{n3:<30}{score3} out of {points3}")

#Prints out, calculates and formatted total scores and rounded total percentage
print(f"{tot2:<30}{score1+score2+score3} out of {points1+points2+points3}")
print(f"Your total is {score1+score2+score3} out of {points1+points2+points3} or {round((score1+score2+score3)/(points1+points2+points3)*100,2)}%.")

#Question 4
print("\nQuestion 4")

#Asks for user input
print("Please enter your test grades.")
test1 = int(input("Test 1: "))
test2 = int(input("Test 2: "))
print()

print("Please enter your quiz grades.")
quiz1 = int(input("Quiz 1: "))
quiz2 = int(input("Quiz 2: "))
quiz3 = int(input("Quiz 3: "))
print()

print("Please enter your homework average.")
homework = eval(input("Homework: "))
print()

#Calculates test average and quiz average
testaverage = (test1+test2)/2
quizaverage = (quiz1+quiz2+quiz3)/3

#Stores strings into a variable to help format later
test = "Test Average:"
quiz = "Quiz Average:"
final = "Final Grade:"

#Prints out formatted and rounded grade
print(f"{test:<14}{round(testaverage,2)}")
print(f"{quiz:<14}{round(quizaverage,2)}")
print(f"{final:<14}{round(testaverage*0.5+quizaverage*0.3+homework*0.2,2)}")
