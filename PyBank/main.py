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

# Track month changes
for x in range(len(change_diff)-1):
    Monthlychng = (change[x+1] - change[x])
    month_month_change.append(Monthlychng)

avgchange = statistics.mean(month_month_change)


# Read through each row of data after the header
for row in csv_reader:
    #print (row)
    Month_Count += 1
    Profil_Losses_Tot += int(row[1])

    if int(row[1]) > Greatest_Incr:
        Best_month = (row[0])Greatest_Incr = int(row[1])

    elif int(row[1]) < Greatest_Decr:
        Worst_Month = (row[0])
        Greatest_Decr = int(row[1])

    change_diff.append(int(row[1]))





