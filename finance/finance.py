import os
import csv
csvpath = os.path.join("financedata.csv")
with open(csvpath, newline='') as csvfile:
    

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    total_profit =0
    number_of_months = 0
    
    # Read each row of data after the header
    for row in csvreader:
        number_of_months = number_of_months + 1
        current_month_profit = int(row[0])
        #add all values to column 1
        total_profit = total_profit + current_month_profit 
        #find the sum diffrence in change except the first month
        if number_of_months ==1:
            previous_month_profit = current_month_profit
            sum_changein_profit = 0
            greatest_increase = 0 
            greatest_decrease = 0
            greatest_increase_date = row[1]
            greatest_decrease_date = row[1]

            continue
        change_in_profit = current_month_profit - previous_month_profit  
        sum_changein_profit = sum_changein_profit + change_in_profit
        
        if change_in_profit > greatest_increase:
            greatest_increase = change_in_profit 
            greatest_increase_date =  row[1]
            
            
        if change_in_profit < greatest_decrease :
           greatest_decrease = change_in_profit
           greatest_decrease_date = row[1]

        
                    
        
        #store this month profit to be used for next month
        previous_month_profit = current_month_profit
    print("number_of_months",number_of_months)
#end for loop
print("total_profit",total_profit)
print(f"Average  Change: ${sum_changein_profit/(number_of_months-1)}")
print("greatest_increase",greatest_increase,greatest_increase_date)
print("greatest_decrease ",greatest_decrease,greatest_decrease_date)

