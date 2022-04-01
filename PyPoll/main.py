#Modules
import os
import csv

# Set variables
Total_votes = 0
Candidate_votes = {}


# Set path for election_data csvfile
election_data_csv = os.path.join("PyPoll/PyPoll/Resources/election_data.csv")

#Open and read election_data.csv
with open(election_data_csv) as read_csvfile:
    csv_reader = csv.reader(read_csvfile, delimiter=",")

    # Read header row first
    csv_header = next(read_csvfile)
    #print(f'Header: {csv_header}')

    # Read each row after header (1) to total votes
    for row in csv_reader:
        Total_votes += 1
        if row[2] not in Candidate_votes:
            Candidate_votes[row[2]] = 1
        else: 
            Candidate_votes[row[2]] =+ 1

#Test print output
#print(str(Total_votes))