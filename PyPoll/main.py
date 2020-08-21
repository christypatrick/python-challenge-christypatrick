# import OS module
import os

# import CSV module
import csv

# set file path
csv_path = os.path.join('Resources', 'election_data.csv')

### Variables
num_votes = 0
candidate_votes = 0


candidate_list = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []

# Read using CSV module

with open(csv_path, 'r') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    #print(csv_reader)

    # Read the header row first (skip this step if there is no header)
    #csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csv_reader:
        #print(row) 

    for row in csv_reader:
    
    # Calculate total number of votes cast (expect 3521001)
        num_votes = num_votes + 1  

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



    #unique List by candidate, if the name is the same then add it to the vote list. length of the list is the count - outside of the loop.
 
    # Percentage of votes each candidate won
        #



    # winner of the election

    #Analysis Header
    print("")
    print("Election Results")
    print("-"*30)
    print(f"Total Votes: {num_votes}")    
    print("-"*30)
    print (f"Khan: {len(khan_votes)}")
    print (f"Correy: {len(correy_votes)}")
    print (f"Li: {len(li_votes)}")
    print (f"O'Tooley: {len(otooley_votes)}")
    # #print candidate: % votes (num votes)
    # print("-"*30)
    # #print(f"Winner: {}")
    # print("-"*30)    


    #print analysis
