#Modules
import os
import csv

# Set variables

Total_votes = 0

# Set path for csvfile
election_data_csv = os.path.join("PyPoll/PyPoll/Resources/election_data.csv")

#Open and read election_data.csv
with open(election_data_csv) as read_csvfile:
    csv_reader = csv.reader(read_csvfile, delimiter=",")

    # Read header row first
    csv_header = next(read_csvfile)
    print(f'Header: {csv_header}')
