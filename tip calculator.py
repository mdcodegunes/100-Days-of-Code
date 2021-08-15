print("Welcome to the tip calculator.")
bill=input("What was the total bill?$")
percentage=input("What percentage tip would you like to give?10,12 or 15?")
people=input("How many people to split the bill?")

x=float(bill)*int(percentage)/100+float(bill)
y= x/int(people)
z=round(y,2)

print(f"Each person should pay:{z}")
