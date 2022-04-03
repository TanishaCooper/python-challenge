# Python Challenge

## PyBank and PyPoll Background

The Python challenge's output are two scripts that analyzed financial records of a company, **PyBank**, and modernize a small, rural town vote counting process, **PyPoll**.

## Python Bank Analysis

The analysis of PyBank's financial records used **budget_data.csv** financial data. The dataset composed of two columns: Date and Profit/Losses. The Python script analyzed the dataset and calculated the following:

> - Total number of months included in dataset
> - Net total amount of ***Profit/Losses*** over the entire period
> - Average of the changes in ***Profit/Losses*** over the entire period
> - Greatest increase in profits (dates and amounts) over the entire period
> - Greatest decrease in profits (dates and amounts) over the entire period

The output of the PyBank financial analysis results in a .txt file that include the following:

Financial analysis
---------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Mar-13 ($1141840)
Greatest Decrease in Pofits: Dec-10 ($-1194133)

## PyPoll Vote Analysis

PyPoll election analyzes a small, rural town voting process. The goal is to improve or modernize the voting process. PyPoll's datasets is pulled from ***election_data.csv***. The latter is composed of three columns: **Voter ID**, **County**, and **Candidate**. The Python script will analyze the votes and calcuate the following:

> - Total number of votes cast
> - Complete list of votes each candidate won
> - Percentage of votes each candidates won
> - Total number of votes each candidate won
> - Winner of the election based on popular vote

The analysis output is the following via a .txt file:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette