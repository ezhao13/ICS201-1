print("1. Calculate the Area of a Circle\n2. Calculate the Area of a Rectangle\n3. Calculate the Area of a Triangle\n4. Quit")
choice = int(input("Enter your choice(1-4): "))
if choice == 1:
  radius = eval(input("Enter the radius of the circle: "))
  print(f"The area of the circle is {radius**2*3.14159}")
elif choice == 2:
  length = eval(input("Enter the length of the rectangle: "))
  width = eval(input("Enter the width of the rectangle: "))
  print(f"The area of the rectangle is {length*width}")
elif choice == 3:
  base = eval(input("Enter the base of the triangle: "))
  height = eval(input("Enter the height of the triangle: "))
elif choice == 4:
  print("Thanks for using geometry calculator!")
  exit()
else:
  print("Please enter a valid number!")

print("You may buy up to 3 items costing no more than $100.")
item1 = eval(input("Enter price of item #1: $"))
if item1 == 100:
  print("You may buy this item.")
  print("You spent $100 so far.")
  print("You are out of money.")
  print("You spent $100, and are done shopping.")
  exit()
elif item1 < 100:
  print("You may buy this item.")
  item2 = eval(input("Enter price of item #2: $"))
  if item1 + item2 == 100:
    print("You may buy this item.")
    print("You spent $100 so far.")
    print("You are out of money.")
    print("You spent $100, and are done shopping.")
    exit()
  elif item1 + item2 < 100:
    print("You may buy this item.")
    item3 = eval(input("Enter price of item #3: $"))
  else:
    print("You may not buy this item.")
    if item1 + item2 + item3 == 100:
      print("You may buy this item.")
      print("You spent $100 so far.")
      print("You are out of money.")
      print("You spent $100, and are done shopping.")
      exit()
    elif item1 + item2 + item3 < 100:
      print("You may buy this item.")
      print("You bought 3 items so far, and are done shopping.")
      exit()
    else:
      print("You may not buy this item.")
else:
  print("You may not buy this item.")