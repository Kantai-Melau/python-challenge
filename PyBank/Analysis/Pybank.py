import os
import csv
import sys

#link and collect data from the CSV
budget_csv = os.path.join("..","Resources","budget_data.csv")
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    
    file_path = 'Pybank.txt'
    sys.stdout = open(file_path, "w")
   
    months_count = 0; total_net = 0; revenue_change = 0; initial_value = 0; greatest_increase = 0; greatest_decrease = 0; 
    first_row = True
    revenue_change_list = []
    for row in csv_reader:
        profit = int(row[1])
        month = row[0]
        #Calculate the total number of months
        months_count += 1
        #The net total amount of "Profit/Losses" over the entire period
        total_net += profit
        #The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if not first_row:
            revenue_change= profit - initial_value
            revenue_change_list.append(revenue_change)
            #Get greatest increase and decrease within the same value
            if revenue_change > greatest_increase:
                greatest_increase = revenue_change
                greatest_increase_month = month
            if revenue_change < greatest_decrease:
                greatest_decrease = revenue_change
                greatest_decrease_month = month

        initial_value = profit
        first_row =False
    #Calculate the average
    def average (revenue_change_list):
        countall = len(revenue_change_list)
        total = sum(revenue_change_list)
        return total/countall

 #Display Results
print("Financial Analysis")
print("-"*20)
print(f"Total Months: {months_count}")
print(f"Total: ${total_net}") 
print(f"Average Change: ${round(average(revenue_change_list),2)}") 
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

sys.stdout.close()
  

