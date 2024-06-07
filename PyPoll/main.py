import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidate_votes = {}

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(f"Header: {header}")

    for row in csvreader: 
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

print(f"Total Votes: {total_votes}")

print("Candidate Votes:")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {votes} votes ({percentage:.3f}%)")

winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
