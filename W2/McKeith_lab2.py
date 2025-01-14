#Duncan McKeith
#1-14-2025 
#SE 126: Intermidate Python
#Lab 2


#Program Prompt:


#Variable Dictionary


#------------------------MAIN CODE BELOW--------------------------
#Imports
#Gotta import a csv to actually work with it
import csv

#Functions


#running Code Begins
#Begin with known Variables


#Initalzing the CSV FILE
print(f"{'Type':8} {'Brand':8} {'CPU':8} {'Ram':5} {'No.HDD':6} {'1st Disk':10} {'2nd Disk':10} {'OS':10} {'Year':10}")
print("-------------------------------------------------------------------------------------------------")
with open("Txt_Files/filehandling.csv") as csvfile:
    
    file = csv.reader(csvfile) #gotta be able to read the csv file
    
    for rec in file: 
        #print(rec) our check to make sure that we actually were getting the proper csv file
        #Now we get to the fun part of classifying the componets and then the annoying hard drives 
        
        
        #Type = Either Desktop or laptop (D,L): Set Type to 2 diffrent things
        type_ = rec[0]
        if type_ == "D":
            type = "Desktop"
        if type_ == "L":
            type_ = "Laptop"
 
 
    
        manu = rec[1]
        if manu == "D":
            manu = "Dell"
        elif manu == "HP":
            manu = "HP"
        elif manu == "GW":
            manu = "Gateway"
        proc = rec[2]
        ram = rec [3]
        size = rec [4]
        number_hd = rec[5]
        
        if number_hd == "2":
        
            print(f"{rec[0]:8} {rec[1]:8} {rec[2]:8} {rec[3]:5} {rec[4]:10} {rec[5]:10} {rec[6]:10} {rec[7]:10} {rec[8]:5}")
        else:
        
            print(f"{rec[0]:8} {rec[1]:8} {rec[2]:8} {rec[3]:5} {rec[4]:10} {rec[5]:10} {'':10} {rec[6]:10} {rec[7]:5}")

