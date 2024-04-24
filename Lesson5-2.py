#Question 1
marks = input("Enter scores: ").split()
for i in range(len(marks)):
  marks[i] = int(marks[i])
max = max(marks)

for i in range(len(marks)):
  if marks[i] >= max - 10:
    print(f"Student {i + 1} score is {marks[i]} and grade is A")
  elif marks[i] >= max - 20:
    print(f"Student {i + 1} score is {marks[i]} and grade is B")
  elif marks[i] >= max - 30:
    print(f"Student {i + 1} score is {marks[i]} and grade is C")
  elif marks[i] >= max - 40:
    print(f"Student {i + 1} score is {marks[i]} and grade is D")
  else:
    print(f"Student {i + 1} score is {marks[i]} and grade is F")
print()
    
#Question 2
numbers = input("Enter a sequence of numbers with a space in between each one: ")
numbList = numbers.split()
numbList.reverse()
      
for values in numbList:
  print(values, end = " ")
print("\n")
  
#Question 3
integers = input("Enter integers between 1 and 100: ")
intList = integers.split()

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
  
looping = True

for i in range (len(intList)):
  if countX(intList, intList[i]) == 1:
    print (f"{intList[i]} occurs {countX(intList, intList[i])} time")
    
  elif countX(intList, intList[i]) != 1:
    
    while(looping):
      print (f"{intList[i]} occurs {countX(intList, intList[i])} times")
      looping = False
      break
print()
  
#Question 4
scores = input("Enter scores: ")
scoreList = (scores.split())

for i in range (len(scoreList)):
  scoreList[i] = int(scoreList[i])
above = 0
lower = 0
equal = 0
avg = sum(scoreList)/len(scoreList)

for i in range (len(scoreList)):
  if scoreList[i]>avg:
    above +=1
  elif scoreList[i]<avg:
    lower +=1
  else:
    equal += 1
    
print (f"Numbers above average: {above}")
print (f"Numbers below average: {lower}")
print (f"Numbers equal to average: {equal}")
print()

# Question 5
list1 = []
list2 = []
tenNumbers = input("Enter ten numbers: ").split()

for num in tenNumbers:
  list1.append(num)
  
for values in list1:
  if values not in list2:
    list2.append(values)
    
for values in list2:
  print(values, end = " ")
print("\n")

#Question 6
import random
counter = []

for i in range(1000):
  number = counter.append(random.randint(0,9))
  
print(f"Zero: {counter.count(0)}")
print(f"One: {counter.count(1)}")
print(f"Two: {counter.count(2)}")
print(f"Three: {counter.count(3)}")
print(f"Four: {counter.count(4)}")
print(f"Five: {counter.count(5)}")
print(f"Six: {counter.count(6)}")
print(f"Seven: {counter.count(7)}")
print(f"Eight: {counter.count(8)}")
print(f"Nine: {counter.count(9)}")
print()

# Question 7
def reverseList(list):
  for value in range(len(list), 0, -1):
    print(list[value-1], end = " ")
    
userNumbers = input("Enter numbers to add to the list: ")
list = userNumbers.split()
reverseList(list)
print("\n")

# Question 8
def eliminateDuplicates(lst):
  nonduplicates = []
  
  for num in lst:
    if num not in nonduplicates:
      nonduplicates.append(num)
      
  for value in nonduplicates:
    print(value, end = " ")
    
tenNumbers = input("Enter ten numbers: ").split()
eliminateDuplicates(tenNumbers)
print("\n")

#Question 9 
def isAnagram(s1, s2):
  list1 = []
  list2 = []
  
  for char in s1:
    list1.append(char.lower())
  list1 = sorted(list1)
  
  for char in s2:
    list2.append(char.lower())
  list2 = sorted(list2)
  
  if list1 == list2:
    print("The words are an anagram.")
  else:
    print("The words are not an anagram.")
    
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
isAnagram(word1, word2)
