import random

for i in range(10):
  for j in range(10):
    print(j, end = " ")
  print()
print()

for i in range(10):
  for j in range(10):
    print(i, end = " ")
  print()
print()

for i in range(11):
  for j in range(i):
    print(j, end = " ")
  print()
print()

for i in range(10):
  for j in range(i):
    print(" ", end = " ")
  for k in range(10-i):
    print(k, end = " ")
  print()
print()

for i in range(1, 10):
  for j in range(1, 10):
    print(f"{j * i:4d}", end = "")
  print()
print()

face1 = 0
face2 = 0
face3 = 0
face4 = 0
face5 = 0
face6 = 0
for i in range(60):
  roll = random.randint(1,6)
  if roll == 1:
    face1 += 1
  elif roll == 2:
    face2 += 1
  elif roll == 3:
    face3 += 1
  elif roll == 4:
    face4 += 1
  elif roll == 5:
    face5 += 1
  else:
    face6 += 1
print(f"{'Face1':10}{'Face2':10}{'Face3':10}{'Face4':10}{'Face5':10}{'Face6'}")
print(f"{face1:<10}{face2:<10}{face3:<10}{face4:<10}{face5:<10}{face6}")
print(" **************** Statistical Analysis ****************")
array = [face1, face2, face3, face4, face5, face6]
min = array[0]
max = array[0]
for j in range(6):
  if min > array[j]:
    min = array[j]
  elif max < array[j]:
    max = array[j]
print(f"min = {min}, max = {max}, range = {max-min}")
print(f"Range as a percent = {round((max-min)/6000000*100,6)}%")
print()

sum = eval(input("Enter desired dice sum: "))
if sum < 2 or sum > 12:
  print("It must be able to be rolled with 2 dice!")
while True:
  roll1 = random.randint(0,6)
  roll2 = random.randint(0,6)
  print(f"{roll1} + {roll2} = {roll1 + roll2}")
  if roll1 + roll2 == sum:
    break
print()

print("Let's roll some dice!")
row = 0
while True:
  roll = random.randint(0,6)
  print(f"You rolled a {roll}")
  if roll % 2 == 1:
    row += 1
  else:
    row = 0
  if row == 3:
    break