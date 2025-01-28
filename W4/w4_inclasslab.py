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
def letter (num):
    '''This function is to take the average test scores then give back a corrisponding letter grade. '''
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:  
        let = "F"
    else:
        let = "error"
        
    return let
#CODE BELOW
#VARIABLE LISTS
fName = []
lName = []
test1 = []
test2 = []
test3 = []
num_avg = []
lgrade = []

#Data stored now to lists, still need to calculate avg amoungst test and letter grade
with open("Txt_Files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file: 
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(rec[2])
        test2.append(rec[3])
        test3.append(rec[4])
#Disconnect #1 from main file        

#Now part 1:  
print(f"{'FirstName':8}   {'LastName':8}   {'test 1':3}   {'test 2':3}  {'test3':3}")
for i in range(0,fName):
    print(f"{fName[i]:8}   {lName[i]:8}   {test1[i]:3}   {test2[i]:3}  {test3[i]:3}")
        
        
        
        
        


for i in range (0,test1):
    a = (test1[i] + test2[i] +test3[i])/3
    num_avg.append(a)
    l = letter(a)
    lgrade.append(i)