#Modules
import os
import csv

# Set variables
total_votes = 0

candaidate_vote_list = []
candidates = []
candidate_percent = []
candidate_count = 0
voter_count = 0
last_count = 0


# Set path for election_data csvfile
election_data_csv = os.path.join("PyPoll/PyPoll/Resources/election_data.csv")

#Open and read election_data.csv
with open(election_data_csv) as read_csvfile:
    csv_reader = csv.reader(read_csvfile, delimiter=",")

    # Read header row first
    csv_header = next(read_csvfile)
    #print(f'Header: {csv_header}')

    
    for row in csv_reader:
        candaidate_vote_list.append(row[2])

    total_votes = len(candaidate_vote_list)
#print(total_votes)

# Name all candidates
for name in candaidate_vote_list:
    if name not in candidates:
        candidates.append(name)
        x = name
#print(candidates)

# Set first candadidate on the dandidate_vote_list for loop
candidates = candaidate_vote_list[0]

#print(candidates)




  




    
