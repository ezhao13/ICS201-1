a = eval(input("Enter value for a: "))
b = eval(input("Enter value for b: "))
c = eval(input("Enter value for c: "))
pos = ((0-b)+(b**2-4*a*c)**(1/2))/(2*a)
neg = ((0-b)-(b**2-4*a*c)**(1/2))/(2*a)
root = (b**2-4*a*c)
if root > 0:
  print(f"The roots are {round(pos,2)} and {round(neg,2)}")
elif root < 0:
  print("There are no real roots")
else:
  print(f"The root is {round(pos,2)}")