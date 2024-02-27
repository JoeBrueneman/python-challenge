import os
import csv

# Create file path to store csvpath
csvpath = os.path.join("Resources", "election_data.csv")

# Create file path to store Analysis text
txtpath = os.path.join("Analysis", "Analysis.txt")

# Create lists, dicts to store data
candidates = []
election_results_full = []
percentage_results = {}
vote_results = {}


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print("CSV Header: " + str(csv_header))

    # Read each row of data after the header
    # all_lists = [row for row in csvreader]
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
        election_results_full.append(row[2])

# Store results data with % and total vote count
for x in candidates:
    vote_results[x] = election_results_full.count(x)
    percentage_results[x] = round((election_results_full.count(x)/len(election_results_full) * 100),3)

# Write analysis results to text file
file = open(txtpath, 'w')
file.write(f'''Election Results
-------------------------
Total Votes: {len(election_results_full)}
-------------------------
{candidates[0]}: {percentage_results[candidates[0]]}% ({vote_results[candidates[0]]})
{candidates[1]}: {percentage_results[candidates[1]]}% ({vote_results[candidates[1]]})
{candidates[2]}: {percentage_results[candidates[2]]}% ({vote_results[candidates[2]]})
-------------------------
Winner: {max(vote_results, key=vote_results.get)}
-------------------------''')

# Print out final analysis
print(f'''Election Results
-------------------------
Total Votes: {len(election_results_full)}
-------------------------
{candidates[0]}: {percentage_results[candidates[0]]}% ({vote_results[candidates[0]]})
{candidates[1]}: {percentage_results[candidates[1]]}% ({vote_results[candidates[1]]})
{candidates[2]}: {percentage_results[candidates[2]]}% ({vote_results[candidates[2]]})
-------------------------
Winner: {max(vote_results, key=vote_results.get)}
-------------------------''')