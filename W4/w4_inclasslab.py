#Duncan McKeith
#1-27-2025
#SE 126: Intermidiate Python
#W4 In Class Lab


#Program Prompt

#Variable Dictionary


#--------MAIN CODE BELOW-------------------
#Import
import csv
#Functions


#CODE BELOW
#VARIABLE LISTS
fName = []
lName = []
test1 = []
test2 = []
test3 = []



with open("Txt_Files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file: 
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(rec[2])
        test2.append(rec[3])
        test3.append(rec[4])
    