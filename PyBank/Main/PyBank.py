import os
import csv

# Path to collect data from the Resources folder
budgetcsv = os.path.join('PyBank/Resources/budget_data.csv')

months = []
variance = []
difference = []
total_sum = 0

with open(budgetcsv, encoding = 'utf8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =',')

    # Skip Header
    next(csvreader)

    #Define funtion to count months
    for x in csvreader:
        months.append(x[0])
        variance.append(x[1])
        total_sum = total_sum + int(x[1])

    i = 1
    for x in range(len(variance)-1):
        difference.append(int(variance[i]) - int(variance[x]))
        i = i + 1

    maxindex = difference.index(max(difference))
    minindex = difference.index(min(difference))

    avg_variance = round(sum(difference)/len(difference),2)

    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total months: {len(months)}')
    print(f'Total variance: ${total_sum}')
    print(f'Average Change: ${avg_variance}')
    print(f'Greatest Increase in Profits: {months[maxindex+1]} (${max(difference)})')
    print(f'Greatest Decrease in Profits: {months[minindex+1]} (${min(difference)})')