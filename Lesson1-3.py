
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))
print("The average of", num1, num2, num3, "is", (num1+num2+num3)/3)

celsius = eval(input("Enter temperature in Celsius scale: "))
print(celsius, "degrees Celsius =", celsius * 9/5 + 32)

length = eval(input("Enter length: "))
width = eval(input("Enter width: "))
print("The area is:", length * width)
print("The perimeter is:", 2 * (length+width))

print("a     b     a ** b")
print("1     2     1")
print("2     3     8")
print("3     4     81")
print("4     5     1024")
print("5     6     15625")

side = eval(input("Enter the side: "))
print("The area of the hexagon is", round(3 * 3 ** (1/2) / 2 * side ** 2, 2))

amount = eval(input("Enter investment amount: "))
interest = eval(input("Enter annual interest rate: "))
years = eval(input("Enter number of years: "))
print("Accumulated value is", round(amount * (1 + interest/12/100) ** (years * 12), 2))