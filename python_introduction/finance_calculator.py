monthly_income = int(input("Enter your monthly income: ")) #monthly income
monthly_expenses = int(input("Enter your total monthly expenses: ")) #monthly expences
monthly_savings = monthly_income - monthly_expenses #calculating monthly savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) #calculating projected savings
print ("Your monthly savings are $", monthly_savings)
print ("Projected savings after one year, with interest is: $", projected_savings)