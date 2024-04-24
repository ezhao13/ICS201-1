num = eval(input("Enter an integer: "))
if num % 2 == 0:
  print(f"{num} is an even integer.")
else:
  print(f"{num} is an odd integer.")

letter = input("Enter a letter: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
  print(f"{letter} is a vowel.")
elif letter == "y":
  print(f"Sometimes {letter} is a vowel, and sometimes {letter} is a consonant.")
else:
  print(f"{letter} is a consonant.")

sides = eval(input("Enter the number of sides: "))
if sides == 3:
  print(f"Closed shapes with {sides} sides is a triangle.")
elif sides == 4:
  print(f"Closed shapes with {sides} sides is a quadrilateral.")
elif sides == 5:
  print(f"Closed shapes with {sides} sides is a pentagon.")
elif sides == 6:
  print(f"Closed shapes with {sides} sides is a hexagon.")
elif sides == 7:
  print(f"Closed shapes with {sides} sides is a heptagon.")
elif sides == 8:
  print(f"Closed shapes with {sides} sides is a octagon.")
elif sides == 9:
  print(f"Closed shapes with {sides} sides is a nonagon.")
elif sides == 4:
  print(f"Closed shapes with {sides} sides is a decagon.")
elif sides > 10 or sides < 3:
  print("The amount of sides is too big or too small.")
else:
  print("That shape doesn't exist!")

length1 = eval(input("Enter first side: "))
length2 = eval(input("Enter second side: "))
length3 = eval(input("Enter third side: "))
if length1 == length2 and length2 == length3:
  print(f"Triangle with side lengths {length1}, {length2}, and {length3} is equilateral.")
elif length1 != length2 and length2 != length3 and length3 != length1:
  print(f"Triangle with side lengths {length1}, {length2}, and {length3} is scalene.")
else:
  print(f"Triangle with side lengths {length1}, {length2}, and {length3} is isosceles.")