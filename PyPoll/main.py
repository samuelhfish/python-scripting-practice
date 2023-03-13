#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#Create a script that analyzes the votes and calculates the following

#Import and read CSV file.
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

#Determine the total number of votes cast.

        rowcount+= 1

#Create a complete list of candidates who received votes.
        if row[2] not in candidate:
            candidate.append(row[2])
            print(candidate) 

#Determine total number of votes each candidate won.

        if row[2] == 'Charles Casper Stockham':
            Stockham_Count += 1
        elif row[2] == 'Diana DeGette':
            DeGette_Count += 1
        elif row[2] == 'Raymon Anthony Doane':
            Doane_Count += 1


#Print the analysis to the terminal and export a text file with the results.
print("Total number of votes in dataset: ", rowcount)
print("Stockham received: ", Stockham_Count, " votes.")
print("DeGette received: ", DeGette_Count, " votes.")
print("Doane received: ", Doane_Count,"votes.")

#Determine percentage of votes each candidate won.

Stockham_Percent = round((Stockham_Count / rowcount) * 100, 3)
DeGette_Percent = round((DeGette_Count / rowcount) * 100, 3)
Doane_Percent = round((Doane_Count / rowcount) * 100, 3)

print("Stockham receuved: ",Stockham_Percent,"%")
print("DeGette received: ",DeGette_Percent,"%")
print("Doane received: ",Doane_Percent,"%")



#Create dictionary to store numeric vote value along with the candidate name.
Election_Results = {'Charles Casper Stockham':Stockham_Count, 'Diana DeGette':DeGette_Count, 'Raymon Anthony Doane':Doane_Count}

#Determine the winner of the election based on popular vote using max.
Winner = max(Election_Results, key=Election_Results.get)

print(Winner," is the winner")

#Print results in desired format
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

fname = os.path.join('.','Analysis','PyBank_Results.txt')

with open(fname,"w") as sample:
    sample.writelines(toprint)