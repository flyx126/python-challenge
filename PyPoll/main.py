import csv
import os

total_candidates= []
winnervotes = []


pypoll_csv = os.path.join(".","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

with open(pypoll_csv,"r",encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_candidates.append((row[2]))
        
total_votes = int(len(total_candidates))
candidates = list(dict.fromkeys(total_candidates))

cand1 = total_candidates.count(candidates[0])
cand2 = total_candidates.count(candidates[1])
cand3 = total_candidates.count(candidates[2])
cand4 = total_candidates.count(candidates[3])

cand1percent = round((cand1/total_votes)*100,3)
cand2percent = round((cand2/total_votes)*100,3)
cand3percent = round((cand3/total_votes)*100,3)
cand4percent = round((cand4/total_votes)*100,3)

if cand1 > cand2 or cand1 > cand3 or cand1 > cand4:
    winner = str(candidates[0])
elif cand2 > cand1 or cand2 > cand2 or cand2 > cand4:
    winner= str(candidates[1])
elif cand3> cand1 or cand3 > cand2 or cand3 > cand4:
    winner = str(candidates[2])
elif cand4 > cand1 or cand4 > cand2 or cand4 > cand3:
    winner = str(candidates[3])

print("Election Results")
print("-------------------\n")
print (f"Total Votes: ", total_votes)
print("\n--------------------")
print(candidates[0],": ",cand1percent,"% ", cand1)
print(candidates[1],": ",cand2percent,"% ", cand2)
print(candidates[2],": ",cand3percent,"% ", cand3)
print(candidates[3],": ",cand4percent,"% ", cand4)
print("\n--------------------")
print(f"Winner: ",winner)
print("\n---------------------")

outputFile = os.path.join(".","PyPoll_Solved.txt")               #direction to the folder we want to store the new file

with open(outputFile,"w") as file:
    
    file.write(" \n")
    file.write("Election Results\n")
    file.write("-----------------\n")
    file.write("Total Votes: ")
    file.write(str(total_votes))
    file.write("\n------------------\n")
    file.write(str(candidates[0]) + ": " + str(cand1percent) + "% " + str(cand1)+"\n")
    file.write(str(candidates[1]) +": " +str(cand2percent)+"% "+str(cand2)+"\n")
    file.write(str(candidates[2])+": "+str(cand3percent)+"% "+str(cand3)+"\n")
    file.write(str(candidates[3])+": "+str(cand4percent)+"% "+str(cand4)+"\n")
    file.write("\n------------------\n")
    file.write("Winner: "+winner+"\n")
    file.write("--------------------")

   




