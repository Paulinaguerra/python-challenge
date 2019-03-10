import os
import csv

budgetCSV = os.path.join("budget2.csv")

with open(budgetCSV) as csvfile:
    reader = csv.reader(csvfile)
    content = csvfile.read()

for row in content[1:]:
    numbers = row.split(',')
    Month = Temp[0]
    Temp = info[1].split(-)
    Net_loss = numbers[2]


#Total number of months included in the dataset and total sum of values
total_months = len(numbers)
net_total = sum (Net_loss) 

#Greatest increase and decrease in profits (date &amount) over the entire period
for i in range(1, len(Net_loss)):
    Net_loss.append[(numbers[1]) - (numbers[i-1])]
    avg_change = sum(Net_loss)/len(Net_loss)

    max_change = max(Net_loss)

    min_change = min(Net_loss)

max_change_d = str(Month[Net_loss.index (max_change)])
min_change_d = str(Month[Net_loss.index (min_change)])


print ("Financial Analysis")
print ("-----------------------")
print ("Total months : ",  total_months)
print ("Total :", net_total)
print ("Average change :", avg_change)
print ("Greatest Increase in Profits: ", "max_change_d", "max_change" )
print ("Greastest Decrease in Profits: ", "min_change_d", "min_change" )



