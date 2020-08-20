# import OS module
import os

# import CSV module
import csv

# set file path
csv_path = os.path.join('Resources', 'election_data.csv')

### Variables


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

    # Calculate total number of votes cast

    # Compile a list of candidates that received votes

    # Percentage of votes each candidate won

    #total number of votes each candidate won

    # winner of the election

    # Analysis Header
    print("")
    print("Election Results")
    print("-"*30)
    #print(f"Total Votes: {}")    
    print("-"*30)
    #print candidate: % votes (num votes)
    print("-"*30)
    #print(f"Winner: {}")
    print("-"*30)    


    #print analysis
