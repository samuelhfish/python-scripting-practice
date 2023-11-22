# Import data from CSV file and create CSV reader
import csv
import os

csvpath = os.path.join('.','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


# Recongize variables after the header line and also define starting points for variables we will need to complete the task.

    csvheader  = next(csvreader)

    rowcount = 0
    profitlosstotal = 0
    current = 0
    previous = 0
    change = 0
    month =[]
    total_changes=[]

# Start loop to go throuch sheet and retrieve required info

    for row in csvreader:

# Calculate the total number of months included in the dataset
        
        rowcount+= 1

# Calculate the net total amount of "Profit/Losses" over the entire period

        profitlosstotal += int(row[1])

#  Calculate the changes in "Profit/Losses" over the entire period
        current = int(row[1])
        change = current-previous
        previous = current
    
        total_changes.append(change)

        month.append(row[0])

 # Remove 1 month as there would be no change on this month and also the corresponding month to correctly insert the date.     
total_changes.pop(0)
month.pop(0)

#  And then the average of those changes

average_change = sum(total_changes) / len(total_changes)

# Calculate the greatest increase in profits (date and amount) over the entire period

greatest_increase = max(total_changes)

# Calculate the greatest decrease in profits (date and amount) over the entire period

greatest_decrease= min(total_changes)

# Print and format all the information

print("Total number of months in dataset:-", rowcount)
print("Total Profits & Losses are:-", '${:,.2f}'.format(profitlosstotal))
print("Total changes over period are:-", total_changes)
print("Average Change is:-", '${:,.2f}'.format(average_change))
print("The greatest increase in profits is:-", month[total_changes.index(greatest_increase)], '${:,.2f}'.format(greatest_increase))
print("The greatest decrease in profits is:-", month[total_changes.index(greatest_decrease)], '${:,.2f}'.format(greatest_decrease))

# Print the analysis to the terminal and export a text file with the results.

line1 = "Financial Analysis\n"
line2 = "----------------------------\n"
line3 = ("Total Months: " + str(rowcount) + "\n")
line4 = ("Total: " + str('${:,.2f}'.format(profitlosstotal)) + "\n")
line5 = ("Average Change: " + str('${:,.2f}'.format(average_change)) + "\n")
line6 = ("Greatest Increase in Profits: " + str(month[total_changes.index(greatest_increase)]) + " " + str('${:,.2f}'.format(greatest_increase)) + "\n")
line7 = ("Greatest Decrease in Profits: " + str(month[total_changes.index(greatest_decrease)]) + " " + str('${:,.2f}'.format(greatest_decrease)) + "\n")


lines_to_print = [line1,line2,line3,line4,line5,line6,line7]

fname = os.path.join('.','Analysis','PyBank_Results.txt')

with open(fname,"w") as sample:
    sample.writelines(lines_to_print)