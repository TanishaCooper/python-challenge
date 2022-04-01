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

float = 0.000000
format_float = "{:.2f}".format(float)
monthlychange = 0
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


# Read through each row of data after the header
    for row in csv_reader:
        #print (row)
        Month_Count += 1
        Profil_Losses_Tot += int(row[1])

        if int(row[1]) > Greatest_Incr:
          Best_month = (row[0])
          Greatest_Incr = int(row[1])

        elif int(row[1]) < Greatest_Decr:
            Worst_Month = (row[0])
            Greatest_Decr = int(row[1])

        change_diff.append(int(row[1]))

    # Track month changes
for i in range(len(change_diff)-1):
    monthlychange = (change_diff[i+1] - change_diff[i])
    month_month_change.append(monthlychange)

avgchange = statistics.mean(month_month_change)

# Setup output view
print("Financial Analysis")
print("----------------------------------")

print("Total Months: " + str(Month_Count))
print("Average Change is: $" + str(format_float(avgchange)))





