num = eval(input("Enter an integer: "))
if num % 2 == 0:
  print("The integer", num, "is even.")
else:
  print("The integer", num, "is odd.")

hours = eval(input("Enter the number of hours worked: "))
pay = eval(input("Enter the hourly pay rate: "))
if hours > 40:
  print(f"The gross pay is ${hours*pay*1.5:,.2f}")
else:
  print(f"The gross pay is ${hours*pay:,.2f}")