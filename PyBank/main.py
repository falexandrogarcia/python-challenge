# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# Dependencies
import os
import csv
    
# reading our csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# open file
with open(budget_data_csv) as csvfile:
        
    # using csv.reader function to read in csvfile 
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Next skips the first line
    header = next(csv_reader)

    # Read through each row of data after the header
    rowcount = 0
    total = 0
    prev_month = 0
    profit = []
    changes = []
    dict = {}


    for row in csv_reader:

        rowcount += 1
        total = total + int(row[1])
        changes.append(int(row[1]) - prev_month)
        dict[row[0]]= int(row[1]) - prev_month
        prev_month = int(row[1])
        profit.append(int(row[1]))
        
        



# Diplay title as per the requirements
print("\nFinancial Analysis\n")
print('----------------------------\n')

# The total number of months included in the dataset
print(f"Total months: {rowcount}\n")

# The net total amount of "Profit/Losses" over the entire period
print(f"Total: ${total}\n")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print(f"Average Change: ${(sum(changes)-profit[0])/(rowcount-1):.2f}\n")

# The greatest increase in profits (date and amount) over the entire period
changes[0] = 0
position_max = changes.index(max(changes))
key_list = list(dict.keys())
print(f"Greatest Increase in Profits: {key_list[position_max]} (${max(changes):.0f})\n")

# The greatest decrease in profits (date and amount) over the entire period
position_min = changes.index(min(changes))
print(f"Greatest Decrease in Profits: {key_list[position_min]} (${min(changes):.0f})\n")


# Specify the file to write to
output_path = os.path.join("analysis", "Results.txt")

# Export a text file with the results.
with open(output_path, 'w') as f:
    f.write("Financial Analysis\n\n")
    f.write('----------------------------\n\n')
    f.write(f"Total months: {rowcount}\n\n")
    f.write(f"Total: ${total}\n\n")
    f.write(f"Average Change: ${(sum(changes)-profit[0])/(rowcount-1):.2f}\n\n")
    f.write(f"Greatest Increase in Profits: {key_list[position_max]} (${max(changes):.0f})\n\n")
    f.write(f"Greatest Decrease in Profits: {key_list[position_min]} (${min(changes):.0f})\n\n")