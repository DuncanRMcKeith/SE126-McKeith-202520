#Duncan McKeith
#W2D1- In class Practice: Text File Handling  Intro
#1-13-2025
#SE 126: Inter. Programing Using Python


#Step 1 Import the csv (comma seperated value) library
import csv



total_records = 0 #the total number of records(rows in the file)

#STEP 2:
#connecting to the files path - switch \ to /
print(f" {'NAME':10}\t {'NUMBER':3}\t {'COLOR'.title()}")
with open ("Txt_Files/simple.csv") as csvfile:
    #ident 1 level! (new block)
    
    
    
    #allow the processor to read the file data
    file = csv.reader(csvfile)
    
    #loop through every record(row in the file)
    for record in file: #Record could mean anything it is just a variable assigned to the file to denote a list. Again think 2d lists
        
        
        #add =+1 to total records
        total_records += 1 
        
        
        #print(record) #The List view of each record (Row) Will print out into a flat bracket and is really only good for data scientists and software eng
        
        
        name = record [0]
        number = record [1]
        color = record [2]        
        print(f" {name:10}\t {number:3}\t {color:10}")
#---------------diconnected from file--------------------------------------

print(f"\n TOTAL RECORDS: {total_records}\n")