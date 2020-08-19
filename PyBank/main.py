# import OS module
import os

# import CSV module
import csv

# set file path
csv_path = os.path.join('Resources', 'budget_data.csv')

# Variables
num_months = 0
total_profit = 0

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
        total_profit = total_profit +int(row[1])
    
    
# average of changes in profits/losses
    

# month with the greatest increase (include amount)

#  month with the greatest decrease (include amount)

    # Analysis Header
    print("")
    print("Financial Analysis")
    print("-"*30)   

    #print analysis
    print(f"Total Months: {num_months}")  
    print(f"Total: $ {total_profit}")