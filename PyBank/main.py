# import OS module
import os

# import CSV module
import csv

# set file path
csv_path = os.path.join('Resources', 'budget_data.csv')

# Variables
num_months = 0
total_profit = 0
previous_revenue = 0
monthly_change = 0
average_change = 0
# greatest_increase = 0
# greatest_inc_month = 0
# greatest_decrease = 0
# greatest_dec_month = 0

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

    #print(mydict)


    for row in csv_reader:
        
    # months in data - count months in the list 
        num_months = num_months + 1
      
    # net total amount of profit/losses
        total_profit = total_profit + int(row[1])
        
# average of changes in profits/losses

        #current month - previous month
        monthly_change = int(row[1]) - previous_revenue

        #reset the previous month's revenue to the row just above
        #previous_revenue = int(row[1])

        #store monthly changes in a list to be summed up to 196785
        #profit_changes.append()
    print(monthly_change)

    ##calculate the sum(profit_changes)/number of profit_changes
    #average_change = str(sum(profit_changes)/len(profit_changes))


##month with the greatest increase (include amount)
# If monthly_change > greatest_increase then:
#   greatest_increase = monthly_change
#   greatest_inc_month = (row[0])


##month with the greatest decrease (include amount)
# If monthly_change < greatest_decrease then:
#   greatest_decrease = monthly_change
#   greatest_dec_month = (row[0])


    # Analysis Header
    print("")
    print("Financial Analysis")
    print("-"*30)   

    #print analysis
    print(f"Total Months: {num_months}")  
    print(f"Total: $ {total_profit}")
    #print(f"Average Change: $ {average_change}")
    #print(f"Greatest Increase in Profits: {greatest_inc_month}($ {greatest increase})")
    #print(f"Greatest Decrease in Profits: {greatest_dec_month}($ {greatest decrease})")