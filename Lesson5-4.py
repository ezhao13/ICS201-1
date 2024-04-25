coffeeWrite = open("coffee.txt", "w")
while True:
  description = input("Description: ")
  quantity = input("Quantity (in pounds): ")
  coffeeWrite.write(description+" "+quantity+"\n")
  again = input("Do you want to enter another record? Y = yes, anything else = no; ")
  if again == "y" or again == "Y":
    continue
  else:
    break
coffeeWrite.close()
print("Data appended to coffee.txt.")
print()

coffeeRead = open("coffee.txt", "r")
for coffee in coffeeRead:
  coffee.strip()
  coffee.split()
  print(f"Description: {coffee[0]}")
  print(f"Quantity: {coffee[1]}")

if True:
  hi = 'hello'
print(hi)