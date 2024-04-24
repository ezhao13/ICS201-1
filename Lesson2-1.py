sales = eval(input("Enter sales: "))
if sales >= 10000:
  commissionRate = 0.2

y = eval(input("Enter value of y: "))
if y == 20:
  x = 0

celsius = eval(input("Enter temperature in celsius: "))
if celsius < -10:
  print("You should wear a coat, gloves, and socks")

test1 = eval(input("Enter score for test 1: "))
test2 = eval(input("Enter score for test 2: "))
test3 = eval(input("Enter score for test 3: "))
average = (test1+test2+test3)/3
print(f"The average score is {round(average,2)}")
if average > 95:
  print("Congratulations!\nThat is a great score.")