
marks = eval(input("Enter the first grade (0 to end process): "))
while marks == 0:
  print("Zero cannot be initial value.")
  marks = eval(input("Enter the first grade (0 to end process): "))
counter = 0
calculate = 0
while marks != 0:
  counter += 1
  calculate = (calculate + marks)
  average = calculate/counter
  marks = eval(input("Enter the first grade (0 to end process): "))
print(f"The average is {round(average,2)}")
print()

i = 0
print(f"{'Original price':<17}{'Percentage off':<17}{'New price'}")
while i < 5:
  value = 14.95 + i * 5
  print(f"{value:<17}{'60%':<17}{value*0.4:.2f}")
  i+=1