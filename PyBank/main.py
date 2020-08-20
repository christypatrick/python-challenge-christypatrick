# import OS module
import os

# import CSV module
import csv

# set file path
csv_path = os.path.join('Resources', 'budget_data.csv')

### Variables
# Used to calculate number of months
num_months = 0
# Used to calculate the total profit or loss
total_profit = 0
# Used when calculating the monthly change in profit or loss
previous_revenue = 0
monthly_change = 0
# Calculates average change
average_change = 0
#Used when identifying the month with the highest change month to month
greatest_increase = 0
greatest_inc_month = 0
#Used when identifying the month with the lowest change month to month
greatest_decrease = 0
greatest_dec_month = 0

#List to hold month to month changes in profit
profit_changes = []

# Read using CSV module

with open(csv_path, 'r') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    #print(csv_reader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csv_reader:
        #print(row) 

    for row in csv_reader:

        #months in data - count months in the list 
        num_months = num_months + 1    
      
        # net total amount of profit/losses
        total_profit = total_profit + int(row[1])
        
    # average of changes in profits/losses
        #current month - previous month
        monthly_change = int(row[1]) - previous_revenue

        #reset the previous month's revenue to the row just above
        previous_revenue = int(row[1])

        #store monthly changes in a list to be summed up to 196785
        profit_changes.append(monthly_change)
        print(profit_changes)

        # calculate the sum(profit_changes)/number of profit_changes
        average_change = int(sum(profit_changes)/len(profit_changes))
        print(f"{average_change}")

        # month with the greatest increase (include amount)
        if (monthly_change > greatest_increase):
            greatest_increase = monthly_change
            greatest_inc_month = (row[0])

        #month with the greatest decrease (include amount)
        if (monthly_change < greatest_decrease):
            greatest_decrease = monthly_change
            greatest_dec_month = (row[0])

    # Analysis Header
    print("")
    print("Financial Analysis")
    print("-"*30)   

    #print analysis
    print(f"Total Months: {num_months}")  
    print(f"Total: $ {total_profit}")
    print(f"Average Change: $ {average_change}")
    print(f"Greatest Increase in Profits: {greatest_inc_month}($ {greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_dec_month}($ {greatest_decrease})")