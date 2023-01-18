import os
import csv

# Path to collect data from the Resources folder
pollcsv = os.path.join('PyPoll/Resources/election_data.csv')

# Opening CSV file to be read
with open(pollcsv, encoding = 'utf8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    candidates = []
    all_names = []

    for rows in csvreader:
        candidate_name = str(rows[2])
        # Collect Votes
        all_names.append(candidate_name)
        # Get the names and total number of candidates
        if candidate_name not in candidates:
            candidates.append(candidate_name)

    total_votes = int(len(all_names))
    candidate_votes = dict()
    y = 0

    while y < len(candidates):
        for z in range(len(candidates)):
            cand_votes = all_names.count(candidates[y])
            vote_percent = round((cand_votes/total_votes)*100,3)
            total_candidate = {candidates[y]:[vote_percent, cand_votes]}
            candidate_votes.update(total_candidate)
        y = y + 1

    winner = max(candidate_votes, key=candidate_votes.get)

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

# opens or creates new file to write to
with open(outpath, 'w', encoding = 'UTF8') as text:
    
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

