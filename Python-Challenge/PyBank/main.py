import csv 
import os

files_to_load=os.path.join("PyBank/Resources", "budget_data.csv")
files_to_output=os.path.join("analysis", "budget_analysis")

total_months=0
months_of_change= []
total_budget = 0
changes = []
dates = []


budgets_path = os.path.join("PyBank/Resources","budget_data.csv")
with open(budgets_path, "r") as budgets_csv:
    budgets = csv.reader(budgets_csv, delimiter= ",")

    header = next(budgets)
    print(header)
    
 
    first_row = next(budgets)
    total_months += 1
    total_budget = total_budget + int(first_row[1])
    compare = int(first_row[1])
 
    for row in budgets:

        
        total_months += 1

 
        total_budget = total_budget + int(row[1])

        dates.append(row[0])

   
        change = int(row[1]) - compare
 
        changes.append(change)

        compare = int(row[1])
    
max_increase = max(changes)

max_decrease = min(changes)

max_index = changes.index(max_increase)
max_month = dates[max_index]

min_index = changes.index(max_decrease)
min_month = dates[min_index]

total_changes = sum(changes)
avg_change = total_changes / len(changes)

print("Financial Analysis\n----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_budget}')
print(f'Average Change: ${round(avg_change)}')
print(f'Greatest Increase in Profits: {max_month}  ${max_increase}')
print(f'Greatest Decrease in Profits: {min_month}  ${max_decrease}')

output = os.path.join("Resources", "results.txt")
