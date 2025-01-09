print("🏁🏁 WELCOME TO TIP CALCULATOR 🏁🏁")

totalBill = float(input("What was the Total Bill? $ "))
peopleSplit = int(input("No of People to Split? "))
tipPercentage = int(input("What percentage of tip would you like to give? \n10, 12, 15 \n"))

# Calcuate Tip payable
tipPercentageofTotalBill = totalBill * (tipPercentage / 100)
# Add tip to Total Bill
Actual_Bill = tipPercentageofTotalBill + totalBill
# Split Total Bill accroding to user input
payableForEach = Actual_Bill / peopleSplit

print(f"Each person should pay: $ {payableForEach:.2f}")