# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# Dependencies
import os
import csv
    
# reading our csv file
budget_data_csv = os.path.join("Resources", "election_data.csv")

# open file
with open(budget_data_csv) as csvfile:
        
    # using csv.reader function to read in csvfile 
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Next skips the first line
    header = next(csv_reader)

    # Read through each row of data after the header
    rowcount = 0
    names = {}
    # total = 0
    # prev_month = 0
    
    # changes = []
    # dict = {}


    for row in csv_reader:

        rowcount += 1

        if row[2] not in names.keys():
            names[row[2]] = 1

        else:
            names[row[2]] += 1


        
        # total = total + int(row[1])
        # changes.append(int(row[1]) - prev_month)
        # dict[row[0]]= int(row[1]) - prev_month
        # prev_month = int(row[1])
        # profit.append(int(row[1]))
        
        



# Diplay title as per the requirements
print("\nElection Results\n")
print('----------------------------\n')

# TThe total number of votes cast
print(f"Total Votes: {rowcount}\n")
print('----------------------------\n')

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
for i in names.keys():
    print(f"{i}: {names[i]/rowcount*100:.3f}% ({names[i]})\n")

print('----------------------------\n')

# The winner of the election based on popular vote
value_list = list(names.values())
key_list = list(names.keys())
position_max = value_list.index(max(value_list))
print(f"Winner: {key_list[position_max]}\n")
print('----------------------------\n')



# Specify the file to write to
output_path = os.path.join("analysis", "Results.txt")

# Export a text file with the results.
with open(output_path, 'w') as f:
     f.write("Election Results\n\n")
     f.write('----------------------------\n\n')
     f.write(f"Total Votes: {rowcount}\n\n")
     f.write('----------------------------\n\n')
     for i in names.keys():
        f.write(f"{i}: {names[i]/rowcount*100:.3f}% ({names[i]})\n\n")
     f.write('----------------------------\n\n')
     f.write(f"Winner: {key_list[position_max]}\n\n")
     f.write('----------------------------\n\n')