#Duncan McKeith
#1-26-2025 
#SE 126: Intermidate Python
#Lab 3



#Program Prompt

#Variable Prompt: 

#MAIN CODE BELOW

#imports
import csv
#Functions

#CODE BELOW

#First our lists variables
non_eligable = 0
registared = []
non_registared = 0
didnt_vote = 0
voted = []
vote_count = 1
records_processed = 0
vote_id = []
age = []
#In order to read the code we first open and connect
with open ("Txt_Files/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        records_processed += 1
        vote_id.append(rec[0])
        age.append(int(rec[1]))
        registared.append(rec[2])
        voted.append(rec[3])

for i in range(0,len(vote_id)):
    if age < 18:
        non_eligable += 1
    elif age > 18 and registared == "Y":
        non_registared += 1
    elif registared == "Y" and voted =="N":
        didnt_vote += 0 
    elif voted == "Y":
        vote_count += 1
    else:
        print("This shouldnt be seen when executing code")

print("Analyis of voters complete")
print(F"Records Processed: {records_processed}")