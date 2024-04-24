
numStudents = int(input("How many students do you have? "))

# determine each student average test score
students = 0
tests = 0
while students < numStudents:

  # initialize an accumulator test scores
  total = 0

  print(f"Student number {students + 1}")
  print("---------------")
  numTests = int(input(f"How many test scores for student {students + 1}? "))
  # Get a student test scores
  while tests < numTests:

    score = eval(input(f"Test {tests + 1} score (0-100) : "))

    #check for valid score (1 - 100)
    while score < 0 or score > 100:
      score = eval(input(f"Test {tests + 1} score (0-100) : "))

    # add the scores to the accumulator
    total += score
    tests += 1

  #Calculate the average test score for this student
  average = total/numTests

  #Display the average
  print(f"The average for student number {students + 1} is: {average}")
  print()
  students += 1
  tests = 0