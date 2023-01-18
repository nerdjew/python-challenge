
import os
import csv

# Path to collect data from the Resources folder
budgetcsv = os.path.join('PyBank/Resources/budget_data.csv')

# Lists and Variable to hold CSV information
months = []
variance = []
difference = []
total_sum = 0

# Opening CSV file to be read
with open(budgetcsv, encoding = 'utf8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =',')

    # Skip Header
    next(csvreader)

    # Loop to collect all the months and variances and store them in lists
    for x in csvreader:
        months.append(x[0])
        variance.append(x[1])
        #Sums the variances to find total Profit/Loss number
        total_sum = total_sum + int(x[1])
        
    # Variable to look ahead in our variance list
    # Loop finds the difference of Profit/Loss for each month and stores in seperate list
    for i in range(len(variance)-1):
        difference.append(int(variance[i+1]) - int(variance[i]))

    # Finds the monthly average change in Profit/Loss throughout the period
    avg_variance = round(sum(difference)/len(difference),2)
    
    #Finds the Greatest increase and decrease index numbers
    maxindex = difference.index(max(difference))
    minindex = difference.index(min(difference))
   
    # Prints text analysis from collected Data
    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total months: {len(months)}')
    print(f'Total variance: ${total_sum}')
    print(f'Average Change: ${avg_variance}')
    print(f'Greatest Increase in Profits: {months[maxindex+1]} (${max(difference)})')
    print(f'Greatest Decrease in Profits: {months[minindex+1]} (${min(difference)})')

# Set path for analysis file
outpath = os.path.join('PyBank/Analysis/Budget_Analysis.txt')

# opens or creates new file to write to
with open(outpath, 'w') as text:
    
    #Writes text to file
    text.write('Financial Analysis\n')
    text.write('-----------------------------\n')
    text.write(f'Total months: {len(months)}\n')
    text.write(f'Total variance: ${total_sum}\n')
    text.write(f'Average Change: ${avg_variance}\n')
    text.write(f'Greatest Increase in Profits: {months[maxindex+1]} (${max(difference)})\n')
    text.write(f'Greatest Decrease in Profits: {months[minindex+1]} (${min(difference)})\n')