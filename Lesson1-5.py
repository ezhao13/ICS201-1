
amount = eval(input("Enter the amount of meal: "))
tip = eval(input("Enter the tip as a percentage: "))
tax = eval(input("Enter the tax as a percentage: "))
print ("{:<20} {:<9} {:<9} {:<9}".format('Amount of meal','Tip','Tax','Total'))
print ("{:<20} {:<9} {:<9} {:<9}".format(amount, round(tip*amount/100,2), round(tax*amount/100,2), round(amount+tip*amount/100+tax*amount/100,2)))


name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
pay = eval(input("Enter hourly pay rate: "))
tax = eval(input("Enter federal tax withholding rate: "))
statetax = eval(input("Enter state tax withholding rate: "))
print("")
print("Employee's name:", name)
print("Hours Worked:", hours)
print("Pay Rate: ${}".format(pay))
print("Gross Pay: ${}".format(hours*pay))
print("Deductions:")
print("  Federal Withholding ({}%): ${}".format(tax*100,round(hours*pay*tax,2)))
print("  State Withholding ({}%): ${}".format(statetax*100,round(hours*pay*statetax,2)))
print("Net Pay: ${}".format(round(hours*pay-hours*pay*tax-hours*pay*statetax,2)))