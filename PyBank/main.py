# Import data from CSV file
import csv
import os

csvpath = os.path.join('.','Resources','budget_data.csv')

with open(csvpath, 'r') as csvfile:
    print("It worked!")



# Calculate the total number of months included in the dataset

# Calculate the net total amount of "Profit/Losses" over the entire period

#  Calculate the changes in "Profit/Losses" over the entire period
#  And then the average of those changes

# Calculate the greatest increase in profits (date and amount) over the entire period

# Calculate the greatest decrease in profits (date and amount) over the entire period

# Print the analysis to the terminal and export a text file with the results.