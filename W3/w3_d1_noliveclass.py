##Duncan McKeith
#1-19-2025 
#SE 126: Intermidate Python
#W3 In Class Lab


#Program Prompt:Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.




#Variable Dictionary:
#type_ = Type of computer, D = Desktop L= Laptop
#manu = Manufacture of Said computer 
#proc = Processor for computer
#ram = how much ram does the computer have
#hdd1 = 1st Hard drive
#no_hdd = number of hard drives
#hdd2 = 2nd hard drive
#os = OS System used by computer
#yr = Year computer was made
#dReplace = Amount of money it costs to replace all desktops
#dReplace_total = The total amount of desktops needing to be replaced
#lReplace = amount of money it costs to replace all laptops
#lReplace_total = the total amount of laptops needing to be replaced. 


#--------------------MAIN CODE BELOW-----------------------------

#Imports
import csv

#Functions none for this problem but could be added on in future 


#Executabe code below
#First list out all our variables and lists

type_ = []
manu = []
proc = []
ram = []
hdd1 = []
no_hdd = []
hdd2 = []
os = []
yr = []
dReplace = 0
dReplace_total = 0
lReplace = 0
lReplace_total= 0

print(f"{'Type':5} {'Manu':5} {'Proc':5} {'Ram':5} {'1st HD':5} {'Num.HD':5} {'2nd HD':7} {'OS':6} {'Year':3}")
#okay now we can start the code
with open("Txt_Files/filehandling-1.csv") as csvfile:
    file = csv.reader(csvfile)#Gotta read our file
    
    for rec in file: #We gotta store all our data to seperated lists, that way we can manipulate it easier. 
        type_.append(rec[0])
        manu.append(rec[1])
        proc.append(rec[2])
        ram.append(rec[3])
        hdd1.append(rec[4])
        no_hdd.append(int(rec[5]))
        if int(rec[5]) == 1: #This one is to deal with the number of hard drives and adding in a blank space for the current no_hdd
            hdd2.append("")
            os.append(rec[6])
            yr.append(int(rec[7]))
        else:
            hdd2.append(rec[6])
            os.append(rec[7])
            yr.append(int(rec[8]))
#Disconnect from the csv file now        
        
for i in range(0,len(type_)):
    if yr[i] <= 16: #This one is to calculate the desktop laptop money to replace
        #Now we seperate the two catagories for laptop and desktop moneys. 
        if type_[i] == "D":
            dReplace +=2000
            dReplace_total += 1
        if type_[i] == "L":
            lReplace += 1500
            lReplace_total += 1
    #Note this is just to print the list from before, NOT HAVING ANYTHING TO DO WITH UP ABOVE. 
    print(f"{type_[i]:5} {manu[i]:5} {proc[i]:5} {ram[i]:5} {hdd1[i]:5} {no_hdd[i]:5} {hdd2[i]:8} {os[i]:6} {yr[i]:3}") 
    
    
#Final print
print("{-------------------------------------------------------------}")
print(f"To replace {dReplace_total:1} it will cost ${dReplace:8}")
print(f"To replace {lReplace_total:1} it will cost ${lReplace:8}")