#Duncan McKeith
#1-21-2025
#SE 126: Inter. Programiming with Pyhton
#W3D2 - List Review - 1Dimensional Lists & Parallel Lists

#this file uses class_grades.csv file located in Txt_files

#Imports
import csv
#Functions

#Main Executuing codes
total_records = 0


#Create an empty list for every potential field. 
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []


print(f"{'First Name':10} {'Last Name':10} {'Test 1':3} {'Test 2':3} {'Test 3':3} {'Avg':6}")


with open("Txt_Files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        #For every record in the file do the following
        
        
        #add the record data to its corresponding list (1 list per field)
        #append ---> to add to the end
        total_records += 1 
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#Dissconnect from file

#basic processing - use the 1d Parallel lists to print all data to the console. 

#create a NEW list to hold each students test score average
avg = []

#Process the current student data to find and store each student's test score avg to the avg list
for i in range(0, len(test1)):
    
    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)
    #could also avg.append((test1[i] + test2[i] + test3[i]) / 3)
    
for index in range(0,len(firstName)): #len()-----. length of collection, returns # of items
    #index = key for the list, allows acess to one specific value at a time
    print(f"{firstName[index]:10} {lastName[index]:10} {test1[index]:3} {test2[index]:3} {test3[index]:3} {avg[index]:6.2f}")
    
    