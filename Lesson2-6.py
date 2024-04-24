"""
a, b, c = eval(input("Enter value for a, b, c: "))
pos = ((0-b)+(b**2-4*a*c)**(1/2))/(2*a)
neg = ((0-b)-(b**2-4*a*c)**(1/2))/(2*a)
root = (b**2-4*a*c)
if root > 0:
  print(f"The roots are {round(pos,2)} and {round(neg,2)}")
elif root < 0:
  print("There are no real roots")
else:
  print(f"The root is {round(pos,2)}")

a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
if a*d-b*c == 0:
  print("The equation has no solution:")
else:
  print(f"x is {(e*d-b*f)/(a*d-b*c)} and y is {(a*f-e*c)/(a*d-b*c)}")

today = int(input("Enter today's day: "))
elapse = int(input("Enter the number of days elapsed since today: "))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"Today is {days[today]} and the future day is {days[today+elapse]}.")
"""
num1, num2, num3 = eval(input("Enter three integers: "))
array = [num1, num2, num3]
for i in array:
  