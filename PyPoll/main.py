import os
import csv
# making sure to find the right path to find the file. as '..' '..' could be used. 
csvpath = os.path.join('Resources', 'election_data.csv')
# starting variables 
total_votes = 0
candidate_votes = {}
# copy and pasted code to open the file 
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(f"Header: {header}")

    for row in csvreader: 
        total_votes += 1 # this is to count every vote 
        candidate = row[2]
        if candidate in candidate_votes: # counting the candidates who they voted for 
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1 # if candidates are in the same category it will be +1 if not , it will stay the same and go to the other 

print(f"Total Votes: {total_votes}")
#printing out the total votes 
print("Candidate Votes:")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {votes} votes ({percentage:.3f}%)")
#printing out the votes for each candidate, the number of votes and finally the percentages with 3 decimal places.
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
#printing out the winner of who gets the most votes,if key=candidate_votes.get is not implemented the person with the least votes will be chosen.