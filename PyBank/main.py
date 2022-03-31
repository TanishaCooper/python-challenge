# Modules
import os
import csv
import statistics 

#Setup variables integers and strings to start at 0
Month_Count= 0
Profil_Losses_Tot = 0
Profit_Losses_Diff_Average = 0.0
Greatest_Incr = 0
Best_month = ''
Greatest_Decr = 0
Worst_Month = ''

month_month_change = []
change_diff = []

#Set path for csv file
budget_data_csv = os.path.join("PyBank/Resources/budget_data.csv")

#Open and read budget_data csv
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Read the header row first
    csv_header = next(csvfile)
    #print(f'Header: {csv_header}')



