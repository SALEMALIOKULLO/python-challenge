import os
import csv

# open and read csv
csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
 csvreader = csv.reader(csvfile, delimiter=',')
 csv_header = next(csvreader)
 print(f"Header: {csv_header}")
    
# Declaring variables
votes = []
county = []
candidates = []
Charles_Casper_Stockham = []
Diana_DeGette = []
Raymon_Anthony_Doane = []
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

# read each row of data after header
for row in csvreader:
votes.append(int(row[0]))
county.append(row[1])
candidates.append(row[2])

# counting the votes
total_votes = (len(votes))
# print(total_votes)
# Votes by Person
for candidate in candidates:
if candidate == "Charles Casper Stockham":
Charles_Casper_Stockham.append(candidates)
Charles_Casper_Stockham_votes = len(Charles_Casper_Stockham)
            
elif candidate == "Diana DeGette":
Diana_DeGette.append(candidates)
Diana_DeGette_votes = len(Diana_DeGette)
            
else:
Raymon_Anthony_Doane.append(candidates)
Raymon_Anthony_Doane_votes = len(Raymon_Anthony_Doane)
    
# print(Charles_Casper_Stockham_votes)
# print(Diana_DeGette_votes)# print(Raymon_Anthony_Doane_votes)
    
# Percentages
Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 3)
Diana_DeGette_percent = round(((Diana_DeGette_votes / total_votes) * 100), 3)
Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 3)
# print(Charles_Casper_Stockham_percent)
# print(Diana_DeGette_percent)
# print(Raymon_Anthony_Doane_percent)

    
# Winners
if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
winner = "Charles_Casper_Stockham"
elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
winner = "Diana_DeGette"  
else:
winner = "Raymon_Anthony_Doane"


# Print Results
print(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

 # Output to a text file
 file = open("output.txt","w")
 file.write(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

 file.close()
