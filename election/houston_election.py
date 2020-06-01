#read the data from the given files
import os 
import csv

# Read each row of data after the header
csvpath = os.path.join("houston_election_data.csv")
with open(csvpath, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    number_of_votes = 0

    candidates = {}
    # "Silvester Turner": 0,
    # "": "Action",
    # "nationality": "United States"


    for row in csvreader:
        # count the number of votes
        number_of_votes = number_of_votes + 1
        # count the given vote to the canditates
        current_candidate = row[0]
        if current_candidate not in candidates:
            candidates[current_candidate]=1
        else:
            candidates[current_candidate]+=1


# print(row[0])


largest_value = 0
second_largest_value = 0
first_candidate = "none"
# after the for loops complete calculate the % of votes each candiadate won.
# print the number of votes and % of total for each candidate
for key, value in candidates.items():
    print (f"{key}: {value} ({round(value/number_of_votes*100, 2)}%)")
    # print the first and second candidate 
    if value > largest_value:
        second_candidate = first_candidate
        first_candidate = key 
        largest_value = value

        
    elif value > second_largest_value:
        second_candidate = key 
        second_largest_value = value

print("\nfirst_candidate",first_candidate)
print("second_candidate",second_candidate)