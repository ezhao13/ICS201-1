x=-10
print(f"{'x':>2s}{'y':>7s}")
print("-"*13)
while x <= 12:
  print(f"{x:3d} |{2*x**3-11*x**2+3:7d}")
  x += 2

i = 1
while i == 1:
  dependents = eval(input("Input number of dependents (-1 to quit): "))
  if dependents == -1:
    print("Good day")
    exit()
  income = eval(input("Input annual income (-1 to quit): "))
  if dependents == 0:
    print("Tax Rate: 30.00%")
    print(f"Tax Amount: ${income * 0.3:.2f}")
  elif dependents == 1: 
    print("Tax Rate: 25.00%")
    print(f"Tax Amount: ${income * 0.25:.2f}")
  elif dependents == 2: 
    print("Tax Rate: 18.00%")
    print(f"Tax Amount: ${income * 0.18:.2f}")
  elif dependents == 3: 
    print("Tax Rate: 10.00%")
    print(f"Tax Amount: ${income * 0.1:.2f}")
  elif income == -1:
    print("Good day")
    exit()
  else:
    print("Please enter a valid number!")

for i in range(5):
  password = input("Enter a password: ")
  if password == "earl haig":
    print("Access Granted")
    exit()
  else:
    print(f"Invalid Password Attempt #{i+1}")
    if i == 4:
      print("You are locked out")