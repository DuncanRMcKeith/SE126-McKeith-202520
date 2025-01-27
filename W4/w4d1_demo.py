#Duncan McKeith
#1-27-2025
#SE 126: Intermidate Python
#W4D1 DEMO: Sequential Search

#Program Prompt:


#------------------IMPORTS-----------------------
import csv
#------------------FUNCTIONS---------------------
def letter(num):
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
#------------------MAIN CODE----------------------
f_name = []
l_name = []
test1 = []
test2 = []
test3 = []



with open("Txt_Files\class_grades.csv") as csvfile:
    
    file = csv.reader(csvfile)
    
    #Store data in lists
    for rec in file:
        f_name.append(rec [0])
        l_name.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
        
#File closed: But we can still acess the data via the lists weve created

#process the list data to calc an avg score for each student, aand find a letter grade equivelent

num_avg = [] #Holds the students numeric average of test scores
l_avg = [] #Will hold the students letter avg

for i in range(0,len(f_name)):
    a = (test1[i] + test2 [i] + test3 [i] / 3)
    num_avg.append(a)
    
    #Can also be num_avg.append(test1[i] + test2 [i] + test3 [i] / 3)
    l=letter(a)
    l_avg.append(l)
    #l_avg.append(letter(num_avg[i]))
    
print(f"{"f_name":10} {"l_name":10} {"test1":3} {"test2":3} {"test3":3} {"num_avg":6} {"l_avg"}")
for i in range (0, len(f_name)):
    print(f"{f_name[i]:10} {l_name[i]:10} {test1[i]:3} {test2[i]:3} {test3[i]:3} {num_avg[i]:6.2f} {l_avg[i]}")