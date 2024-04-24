def hypotenuse(a, b):
  return (a**2 + b**2)**(1/2)
a = eval(input("Enter side a: "))
b = eval(input("Enter side b: "))
print(f"The hypotenuse is {hypotenuse(a, b)}")

print()



print()

def shipping(items):
  if items == 1:
    return 10.95
  else:
    return 2.95 * (items - 1) + 10.95
items = eval(input("Enter the # of items shipped: "))
print(f"The shipping cost is ${shipping(items):.2f}")