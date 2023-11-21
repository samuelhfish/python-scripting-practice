```python
# python-challenge
Homework for the Python module of DataViz bootcamp.


# PyBank Task

# Import data from CSV file and create CSV reader

    import csv
    import os

    csvpath = os.path.join('.','Resources','budget_data.csv')

    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")


# Recongize variabls after the header line and also define starting points for variables we will need to complete the task.

        csvheader  = next(csvreader)

        rowcount = 0
        profitlosstotal = 0
        current = 0
        previous = 0
        change = 0
        month =[]
        total_changes=[]

# start loop to go throuch sheet and retrieve required info

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

# remove 1 month as there would be no change on this month and also the corresponding month to correctly insert the date.     
    
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
```
```python

# RESULTS

    Financial Analysis
    ----------------------------
    Total Months: 86

    Total: $22,564,198.00

    Average Change: $-8,311.11

    Greatest Increase in Profits: Aug-16 $1,862,002.00

    Greatest Decrease in Profits: Feb-14 $-1,825,558.00
```
```python

# PyPoll Task

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# Create a script that analyzes the votes and calculates the following

# Import and read CSV file.
    import csv
    import os

    csvpath = os.path.join('.','Resources','election_data.csv')

    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")


# Recongize variables after the header line and also define starting points for variables we will need to complete the task.

        csvheader  = next(csvreader)

        rowcount = 0
        DeGette_Count = 0
        Stockham_Count = 0
        Doane_Count = 0
        candidate =[]


# start loop to go throuch sheet and retrieve required info

        for row in csvreader:

# Determine the total number of votes cast.

            rowcount+= 1

# Create a complete list of candidates who received votes.
            if row[2] not in candidate:
                candidate.append(row[2])
                print(candidate) 

# Determine total number of votes each candidate won.

            if row[2] == 'Charles Casper Stockham':
                Stockham_Count += 1
            elif row[2] == 'Diana DeGette':
                DeGette_Count += 1
            elif row[2] == 'Raymon Anthony Doane':
                Doane_Count += 1


# Print the analysis to the terminal and export a text file with the results.

    print("Total number of votes in dataset: ", rowcount)
    print("Stockham received: ", Stockham_Count, " votes.")
    print("DeGette received: ", DeGette_Count, " votes.")
    print("Doane received: ", Doane_Count,"votes.")

# Determine percentage of votes each candidate won.

    Stockham_Percent = round((Stockham_Count / rowcount) * 100, 3)
    DeGette_Percent = round((DeGette_Count / rowcount) * 100, 3)
    Doane_Percent = round((Doane_Count / rowcount) * 100, 3)

    print("Stockham receuved: ",Stockham_Percent,"%")
    print("DeGette received: ",DeGette_Percent,"%")
    print("Doane received: ",Doane_Percent,"%")



# Create dictionary to store numeric vote value along with the candidate name.
    Election_Results = {'Charles Casper Stockham':Stockham_Count, 'Diana DeGette':DeGette_Count, 'Raymon Anthony Doane':Doane_Count}

# Determine the winner of the election based on popular vote using max.
    Winner = max(Election_Results, key=Election_Results.get)

    print(Winner," is the winner")

# Print results in desired format

        toprint = f"""
        -----------------------
        Election Results
        -----------------------
        Total Votes: {rowcount} 
        -----------------------
        Stockham: {Stockham_Percent}% ({Stockham_Count})
        DeGette: {DeGette_Percent}% ({DeGette_Count})
        Doane: {Doane_Percent}% ({Doane_Count})
        -----------------------
        Winner: {Winner} 
        -----------------------"""

    print(toprint)

# Print the analysis to the terminal and export a text file with the results.

    fname = os.path.join('.','Analysis','PyPoll_Results.txt')

    with open(fname,"w") as sample:
        sample.writelines(toprint)
```
```python
    
# RESULTS


    -----------------------
    Election Results
    -----------------------
    Total Votes: 369711 
    -----------------------
    Stockham: 23.049% (85213)
    DeGette: 73.812% (272892)
    Doane: 3.139% (11606)
    -----------------------
    Winner: Diana DeGette 
    -----------------------
```
