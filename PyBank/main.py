import os
import csv
#making sure correct pathway of the file is located. Implementing '..' or even '..' '..' if needed as for this it needs none since its doesnt need to go back. 
csvpath = os.path.join('Resources', 'budget_data.csv')
#listing the variables, for me sometimes it is easier to start from print and working my way up to find variables.
total_months = 0
net_total = 0
changes = []
previous_amount = None
max_increase = 0
max_increase_month = ""
max_decrease = 0 
max_decrease_month = ""
#copy and pasted code to open the file 
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#header code also located in the solved activities section 
    header = next(csvreader)
    print(f"Header: {header}")
#adding all the total months 
    for row in csvreader:
        total_months += 1
        amount = int(row[1])
        net_total += amount
#looking for the maximum and minimum decrease/increase
        if previous_amount is not None:
            change = amount - previous_amount
            changes.append(change)
            if change > max_increase:
                max_increase = change
                max_increase_month = row[0]
            elif change < max_decrease:
                max_decrease = change
                max_decrease_month = row[0]
#logic here is that if it is bigger it will be the new amount ,same as for decrease but new amount will be the lowest amount
        previous_amount = amount
# formula for average change 
average = sum(changes) / (total_months - 1)
# printing out the titles for the answers 
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average:.2f}") #set to 2 decimal places. 
print(f"Greatest Increase in Profits: {max_increase} (Month: {max_increase_month})")
print(f"Greatest Decrease in Profits: {max_decrease} (Month: {max_decrease_month})")

