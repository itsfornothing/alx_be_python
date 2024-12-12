income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses: ")
saving = int(income) - int(expenses)
annual_saving  = (12 * saving) + (12 * saving * 0.05)

print(f"Your monthly savings are ${saving}.")
print(f"Projected savings after one year, with interest, is: ${int(annual_saving)}.")
