
name = input("Enter a name: ")
space = 1
for char in range(len(name)):
  first = name[0]
  if name[char] == ' ' and space == 1:
    middle = name[char+1]
    space += 1
  elif name[char] == ' ' and space == 2:
    last = name[char+1]
print(f"{first.upper()}. {middle.upper()}. {last.upper()}")

number = input("Enter a series of single-digit numbers: ")
sum = 0
for char in range(len(number)):
  sum += eval(number[char])
print(sum)

import calendar
date = input("Enter a date (mm/dd/yyyy): ")
if date[0] == "0":
  print(f"{calendar.month_name[eval(date[1])]} {date[3]}{date[4]}, {date[6]}{date[7]}{date[8]}{date[9]}")
elif date[0] == "1":
  print(f"{calendar.month_name[10+eval(date[1])]} {date[3]}{date[4]}, {date[6]}{date[7]}{date[8]}{date[9]}")

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}