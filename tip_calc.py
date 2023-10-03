print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

tip = float(input("What percentage tip would you like to give? "))
table_size = int(input("How many people will split the bill? "))
total_bill = bill * (tip/100) + bill
final_bill = round((total_bill / table_size), 2)
final_bill = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${final_bill}")
