# import OS module
import os

# import CSV module
import csv

#import statistics module
import statistics

# set file path
csv_path = os.path.join('Resources', 'election_data.csv')

### Variables
num_votes = 0
candidate_votes = 0
khan_percent = 0
correy_percent = 0
li_percent = 0
otooley_percent= 0
winner = 0

votes_list = []
candidate_list = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []
percent_list = []

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
    
    # Calculate total number of votes cast (expect 3521001)
        num_votes = num_votes + 1

    # Create votes list
        votes_list.append(row[2])

    # Compile a list of candidates that received votes
        if (row[2]) not in candidate_list:
            candidate_list.append(row[2])
        else:
            pass        

    #print(candidate_list)
     #total number of votes each candidate won
        if (row[2]) == "Khan":
            khan_votes.append(row[2])
        elif (row[2]) == "Correy":
            correy_votes.append(row[2])
        elif (row[2]) == "Li":
            li_votes.append(row[2])
        elif (row[2]) == "O'Tooley":
            otooley_votes.append(row[2])
        else:
            pass 

    # Percentage of votes each candidate won
    
    khan_percent = "{:.3%}".format(len(khan_votes)/(num_votes))
    correy_percent = "{:.3%}".format(len(correy_votes)/(num_votes))
    li_percent = "{:.3%}".format(len(li_votes)/(num_votes))
    otooley_percent= "{:.3%}".format(len(otooley_votes)/(num_votes))

    # winner of the election

    winner = (statistics.mode(votes_list))
 

    # #Analysis Header
    # print("")
    # print("Election Results")
    # print("-"*30)
    # print(f"Total Votes: {num_votes}")    
    # print("-"*30)
    # print (f"Khan: {khan_percent} ({len(khan_votes)})")
    # print (f"Correy: {correy_percent} ({len(correy_votes)})")
    # print (f"Li: {li_percent} ({len(li_votes)})")
    # print (f"O'Tooley: {otooley_percent} ({len(otooley_votes)})")
    # print("-"*30)
    # print(f"Winner: {winner}")
    # print("-"*30)    


    #Analysis 
    message = f"""
        Election Results
        {"-"*30}
        Total Votes: {num_votes}
        {"-"*30}
        Khan: {khan_percent} ({len(khan_votes)})
        Correy: {correy_percent} ({len(correy_votes)})
        Li: {li_percent} ({len(li_votes)})
        O'Tooley: {otooley_percent} ({len(otooley_votes)})
        {"-"*30}
        Winner: {winner}
        {"-"*30}
    """

    print(message)
