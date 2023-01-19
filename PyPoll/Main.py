# Import dependencies
import os
import csv

# Path to collect data from the Resources folder
pollcsv = os.path.join('PyPoll/Resources/election_data.csv')

# Opening CSV file to be read
with open(pollcsv, encoding = 'utf8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skipping header row
    next(csvreader)

    # Creating the lists to hold the candidates and votes
    candidates = []
    all_names = []

    #For loop to find the unique candidates and get all votes listed
    for rows in csvreader:
        # Identifying candidate name
        candidate_name = str(rows[2])
        # Collect Votes
        all_names.append(candidate_name)
        # Find out if the name is already in our candidate list or if we need to add it
        if candidate_name not in candidates:
            candidates.append(candidate_name)

    # Finding the total votes cast
    total_votes = int(len(all_names))

    # Creating dictionary and variable to count each candidates votes and store the results
    candidate_votes = dict()
    y = 0

    # While loop to cycle through each candidate
    while y < len(candidates):
        # Loop to count the votes of the indicated candidate 
        for z in range(len(candidates)):
            cand_votes = all_names.count(candidates[y])
            # Finding the percent of the total votes
            vote_percent = round((cand_votes/total_votes)*100,3)
            # Creating the dictionary entry
            total_candidate = {candidates[y]:[vote_percent, cand_votes]}
            candidate_votes.update(total_candidate)
        # Moving to the next candidate
        y = y + 1

    # Finds the candidate with the highest value
    winner = max(candidate_votes, key=candidate_votes.get)

    # Prints results to the terminal
    print('Election Results')
    print('--------------------------')
    print(f'Total Votes: {total_votes}')
    print('--------------------------')
    for key, value in candidate_votes.items():
        print(f'{key}: {value[0]}% ({value[1]})')
    print('--------------------------')
    print(f'Election Winner: {winner}')
    print('--------------------------')
    

# Set path for analysis file
outpath = os.path.join('PyPoll/Analysis/Election_Analysis.txt')

# Opens or creates new file to write to
with open(outpath, 'w', encoding = 'utf8') as text:
    
    #Writes text to file
    text.write('Election Results\n')
    text.write('--------------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write('--------------------------\n')
    for key, value in candidate_votes.items():
        text.write(f'{key}: {value[0]}% ({value[1]})\n')
    text.write('--------------------------\n')
    text.write(f'Election Winner: {winner}\n')
    text.write('--------------------------')

