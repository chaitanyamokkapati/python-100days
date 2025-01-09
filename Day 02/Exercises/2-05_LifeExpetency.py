# Considering a Person can live 90 Years. Ignore leap Year
# Year = 365 Days
# Year = 52 Weeks
# Year = 12 Months

age = int(input("What is your age: "))
yearsRemaining = 90 - age
daysRemaining = yearsRemaining * 365
weeksRemaining = yearsRemaining * 52
monthsRemaining = yearsRemaining * 12

print(f"You have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left.")