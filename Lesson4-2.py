import math


def whatToWear(temp):
  if temp <= 50:
    print("Wear a jacket")
  elif temp > 50 and temp < 70:
    print("Wear a sweater")
  else:
    print("Wear a t-shirt")
temp = eval(input("Enter the temperature: "))
whatToWear(temp)

print()


def circleArea(r):
  print(f"The area is {math.pi * r**2:.2f}")
r = eval(input("Enter the radius of the circle: "))
circleArea(r)

print()

def greetings(string, n):
  for i in range(n):
    print(string)
string = input("Enter the greeting message: ")
n = eval(input("Enter the number of greetings: "))
greetings(string, n)

print()

def toCelsius(f):
  print(f"The fahrenheit in celsius is {5/9*(f-32):.2f}")
toCelsius(32)
toCelsius(72)
toCelsius(98)
toCelsius(100)

print()

def largestNum(n1, n2, n3):
  mylist = [n1, n2, n3]
  max = n1
  for i in range(2):
    if mylist[i] < mylist[i + 1]:
      max = mylist[i + 1]
  print(max)
n1, n2, n3 = eval(input("Enter 3 numbers: "))
largestNum(n1, n2, n3)
