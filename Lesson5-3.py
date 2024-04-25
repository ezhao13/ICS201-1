poem = open("poem.txt", "r")
for line in poem:
  line = line.strip()
  line = line.upper()
  print(line)
employeeHours = open("employeeHours.txt", "r")
print()

for employee in employeeHours:
  employee = employee.strip()
  employee = employee.split()
  total = 0
  for hours in range(1, len(employee)):
    total += eval(employee[hours])
  print(f"Total hours worked by {employee[0]}: {total}")
print()

hours = open("hours.txt", "r")
for employee in hours:
  employee = employee.strip()
  employee = employee.split()
  total = 0
  for hours in range(2, len(employee)):
    total += eval(employee[hours])
  print(f"Total hours worked by {employee[1]} (id#{employee[0]}) = {total}")