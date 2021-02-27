#need to import file first

import csv
import os

file = r"C:\Users\Patrick Holyoake\Desktop\DA_Bootcamp\Homework\Week_3\python-challenge\PyBank\Resources\budget_data.csv"

months=[]
profit=[]
dif=[]

with open(file, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    

# Count months and calculate total profit
    csv_header = next(reader)
    for row in reader:
        months.append(row[0])
        profit.append(int(row[1]))
        #print(" Total Months: " + str(total_row))
        #print("Total: $ " + str(total))

# Calculate average change between rows
    x=0
    for x in range(len(profit)-1):
        dif.append(profit[x+1]-profit[x])

max_increase_value = max(dif)
max_decrease_value = min(dif)
        

max_increase = dif.index(max(dif)) + 1
max_decrease = dif.index(min(dif)) + 1


#Print

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change:$ {round(sum(dif)/len(dif),2)}")
print(f"Greatest increase in profits: {months[max_increase]} (${(str(max_increase_value))})")
print(f"Greatest decrease in profits: {months[max_decrease]} (${(str(max_decrease_value))})")

output_file = os.path.join("Resources", "Financial_Summary.csv")

with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("---------------------")
    txtfile.write(f"Total Months: {len(months)}")
    txtfile.write(f"Total: ${sum(profit)}")
    txtfile.write(f"Average Change:$ {round(sum(dif)/len(dif),2)}")
    txtfile.write(f"Greatest increase in profits: {months[max_increase]} (${(str(max_increase_value))})")
    txtfile.write(f"Greatest decrease in profits: {months[max_decrease]} (${(str(max_decrease_value))})")




        
 
    

