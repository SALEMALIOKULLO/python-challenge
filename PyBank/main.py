import os
import csv 

#directory
path = "/tmp/om"
os.mkdir(path)
print ("Successfully created the directory %s " % path)
Successfully created the directory /tmp/om

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv_path, newline="") as csvfile:
       
csvreader = csv.reader(csvfile, delimiter = ',')
next(csvreader)
#Excluding first month from looping
budget_data = [next(csvreader)]
#Net amount with first profit or loss 
net_amount = int(budget_data[0][1])
changes = []

#vaiables
net_profit_loss = 0
profit_loss_change = 0

#Calculating change inside for loop
previous_profit_loss = net_amount

for line in csvreader:
#Total months 
budget_data.append(line)
       
#Net total amount of Profit/Losses over entire period
net_amount = net_amount + int(line[1])
       
# Biggest Change in profit/loss over entire period
changes.append(int(line[1])-previous_profit_loss)

# Average changes of profit/loss
previous_profit_loss = int(line[1])

# Greatest increase in profit 
index_max_change = changes.index(max(changes))
# print(budget_data[index_max_change+1])

#Greatest decrease in profit 
index_max_loss = changes.index(min(changes))
# print(budget_data[index_max_loss+1])

# Export result and print analysis to terminal
output = '''Financial Analysis
  ----------------------------
  Total Months: {len(budget_data)}
  Total: ${net_amount}
  Average Change: ${round(sum(changes)/(len(changes)),2)}
  Greatest Increase in Profits: {budget_data[index_max_change+1][0]} (${max(changes)})
  Greatest Decrease in Profits: {budget_data[index_max_loss+1][0]} (${min(changes)})
  
  '''
print(output)
csvpath = os.path.join('Analysis', 'Financial_Analysis.txt')

 # Export a text file with the results
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")
