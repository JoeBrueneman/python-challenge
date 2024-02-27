import os
import csv

# Create file path to store csvpath
csvpath = os.path.join("Resources", "budget_data.csv")

# Create file path to store Analysis text
txtpath = os.path.join("Analysis", "Analysis.txt")

# Create lists, dicts to store data
months = []
Profit_losses = []
budget = {}

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print("CSV Header: " + str(csv_header))

    # Read each row of data after the header
    # all_lists = [row for row in csvreader]
    for row in csvreader:
        months.append(row[0])
        Profit_losses.append(int(row[1]))
        budget[row[0]] = int(row[1])

# Function for finding average changes, greatest increase, and greatest decrease in a dictionary
def changes(dict):

    # Create variables to return later, and temp values as the list iterates
    increase_date = ""
    increase_diff = 0
    decrease_date = ""
    decrease_diff = 0
    container = []
    x = 0
    y = 0

    # Read each key-value pair in the dictionary
    for key,value in dict.items():

        # Calculate difference between the current value and previous value
        x = value
        diff = x - y
        container.append(diff)

        # Check to see if current difference should be saved as the greatest increase or decrease
        if diff > increase_diff:
            increase_diff=diff
            increase_date = key
        elif diff < decrease_diff:
            decrease_diff=diff
            decrease_date = key
        y = value

    # Remove first entry of list (because the first entry is "current value - 0" and therefore incorrect data), and calculate average change
    container.pop(0)
    average_change = round((sum(container) / len(container)),2)

    return increase_date,increase_diff,decrease_date,decrease_diff,average_change

# Write analysis results to text file
file = open(txtpath, 'w')
file.write(f'''Financial Analysis
----------------------------
Total Months: {len(months)}
Total: ${sum(Profit_losses)}
Average Change: (${changes(budget)[4]})
Greatest Increase in Profits: {changes(budget)[0]} (${changes(budget)[1]})
Greatest Decrease in Profits: {changes(budget)[2]} (${changes(budget)[3]})''')

# Print out final analysis
print(f'''Financial Analysis
----------------------------
Total Months: {len(months)}
Total: ${sum(Profit_losses)}
Average Change: (${changes(budget)[4]})
Greatest Increase in Profits: {changes(budget)[0]} (${changes(budget)[1]})
Greatest Decrease in Profits: {changes(budget)[2]} (${changes(budget)[3]})''')