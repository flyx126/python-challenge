import csv
import os

total_months = []
total_amount = []
total_avg = []

pybank_csv = os.path.join(".","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")


with open(pybank_csv,"r",encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(float(row[1]))

    for i in range(len(total_amount)-1):
        total_avg.append(total_amount[i+1]-total_amount[i])


max_increase = max(total_avg)
min_increase = min(total_avg)
maxmonth = total_avg.index(max_increase)
minmonth = total_avg.index(min_increase)



outputFile = os.path.join(".","PyBank_Solved.txt")               #direction to the folder we want to store the new file

with open(outputFile,"w") as file:
    
    file.write("Financial Analysis \n")
    file.write("-----------------------------\n")
    file.write("Total Months: ")
    file.write(str(len(total_months)))
    file.write("\n")
    file.write("Total: $")
    file.write(str(sum(total_amount)))
    file.write("\n")
    file.write("Avergae Change: $")
    file.write(str(sum(total_avg)/len(total_avg)))
    file.write("\n")
    file.write("Greatest Increase in profits: ")
    file.write(str(total_months[maxmonth+1]))
    file.write(" $")
    file.write(str(max_increase))
    file.write("\n")
    file.write("Greatest Decrease in profits: ")
    file.write(str(total_months[minmonth+1]))
    file.write(" $")
    file.write(str(min_increase))
    #datafile.write(str(min))     

print("\n")
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months:", len(total_months))
print(f"Total: $", sum(total_amount))
print(f"Average Change: $", sum(total_avg)/len(total_avg))
print(f"Greatest Increase in profits: ", total_months[maxmonth+1] , "$",max_increase)
print(f"Greatest Decrease in profits: " , total_months[minmonth+1], "$", min_increase)