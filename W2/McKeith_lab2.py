#Duncan McKeith
#1-19-2025 
#SE 126: Intermidate Python
#Lab 2


#Program Prompt:Our Goal is to produce a report list of computers (And their parts) using a csv file given to us. 


#Variable Dictionary
#file = variable assigned to read the csv file
#rec  = each line of the csv file, jsut designed to keep our 
#Each one below is an assigned record value--- Note i dont record what rec it is here but do in my code cause its alot. 
#type = type of computer (either desktop or laptop)
#manu = manufactuerer or brand, bassically who built it
#proc = processor for the computer. 
#Ram = How many Gigabytes of ram does the computer have
#size how big the first Disk drive is
#number_hd = How many hard drives are (also where the code gets complicated, see notes on line 66)
#------------------------MAIN CODE BELOW--------------------------
#Imports
#Gotta import a csv to actually work with it
import csv

#Functions
#Didnt use any but you def could to filter results. 

#running Code Begins
#Begin with known Variables

#Although this was done last, this is neat and organizing the list. 


print(f"{'Type':8} {'Brand':8} {'CPU':8} {'Ram':5} {'No.HDD':6} {'1st Disk':10} {'2nd Disk':10} {'OS':10} {'Year':10}")
print("-------------------------------------------------------------------------------------------------")
#GO GO CSV FILE: Queue Power Rangers opening
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
        #Now we split it as lines (recs) 6-8 get assigned in diffrent spots depending on the number of HD in the program. If there are two then all 8 are printed otherwise only 7 are and a blank space is added. 
        if number_hd == "2":
        
            print(f"{rec[0]:8} {rec[1]:8} {rec[2]:8} {rec[3]:5} {rec[4]:10} {rec[5]:10} {rec[6]:10} {rec[7]:10} {rec[8]:5}")
        else:
        
            print(f"{rec[0]:8} {rec[1]:8} {rec[2]:8} {rec[3]:5} {rec[4]:10} {rec[5]:10} {'':10} {rec[6]:10} {rec[7]:5}")

