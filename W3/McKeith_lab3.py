#Duncan McKeith
#1-26-2025 
#SE 126: Intermidate Python
#Lab 3



#Program Prompt: Construct a program that will analyze potentital voters. The program should generate, the number of individuals not eligable to registar, the number of individuals who are old enough to vote but are not, number of individuals who did vote, number of records proceessed. 

#Variable Dictionary
# registared = List variable used to assign the rec [2]
# vote_id = List Variable used to keep track of rec [0]
# age = List variable used to keep track of rec[1]
# voted = List variable used to keep track of rec [3]
# Non_eligable = if they arent old enough to registar
#  non_registared = all users old enough but arent registared
# didnt_vote = users that are registared but didnt vote
# vote_count = the amount of users who voted
# record_processed = how many records in total did the program scan. 
#
#
# 

#MAIN CODE BELOW

#imports
import csv
#Functions

#CODE BELOW

#First our lists variables
registared = []
voted = []
vote_id = []
age = []

#Then our regular variables. 
non_eligable = 0
non_registared = 0
didnt_vote = 0
vote_count = 0
records_processed = 0

#In order to read the code we first open and connect
with open ("Txt_Files/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:#assign all data in a csv file to a list now. 
        records_processed += 1
        vote_id.append(rec[0])
        age.append(int(rec[1]))
        registared.append(rec[2])
        voted.append(rec[3])

for i in range(0,len(vote_id)):
    if age[i] < 18:
        non_eligable += 1
    elif age[i] >= 18 and registared[i] != "Y":
        non_registared += 1
    elif registared[i] == "Y" and voted[i] =="N":
        didnt_vote += 1 
    elif voted[i] == "Y":
        vote_count += 1
    else:
        print("This shouldnt be seen when executing code")

print("Analyis of voters complete")
print(F"Records Processed: {records_processed} Non Eligable Voters: {non_eligable} Voters Not Registered: {non_registared} Eligable Voters Who Didnt Vote: {didnt_vote} People Who Did Vote: {vote_count}")