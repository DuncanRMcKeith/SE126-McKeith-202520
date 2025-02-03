#Duncan McKeith
#1-27-2025
#SE 126: Intermidiate Python
#W4 In Class Lab


#Program Prompt:Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file. Next, reprocess the lists to find each student's current average score, letter grade equivalent, and the class average.  While processing in the for loop, store each student's average into a new list called 'num_avg' and their letter grade into a list called 'let_avg'. Then, print each student's full information, record by record including average score and average letter equivalent.  After this print of the original file data from the lists, print to the console the total number of student's in the class along with the class numeric average.  After your final display using the 1D parallel lists, create a sequential search program which allows the user to repeatedly utilize the following menu of search types. When a searched for item is found, display all student data to the console. When a search is compete and no matching data is found, alert the user. Search options 1 and 2 should only show one found student, where search option 3 should show a potential of multiple students.



#Variable Dictionary
#fName = First name list
#lName = Last name list variable
# test1 = test 1 list variable
# test2 = test 2 list variable
# test3 = test 3 list variable
# lgrade = Average letter grade list variable
# num_avg = Average of all three tests stored to a list
# ans = while loop key
# search_type = user input for menu options
# found = key for search funtion
# search_name = name searched for
# search_grade = grade searched for
# 
# 
# -

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


def menu ():
    '''This Is a menu function created instead of writing out a whole bunch of print statments within my code easier work with. S is our search choice'''
    print("---------------------------------STUDENT INDEX FINDER---------------------------------------------")
    print(f"\t\tSelect from option below")
    print(f"\t1. Search By LAST name")
    print(f"\t2. Search By FIRST name")
    print(f"\t3. Search By LETTER grade")
    print(f"\t4. EXIT")
    s = input("What would you like to search by?")
    return s
    
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
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#Disconnect #1 from main file--- Now we can work with it 

      
'''
#Now part 1:  
print(f"{'FirstName':8}   {'LastName':8}   {'Test 1':3}   {'Test 2':3}  {'Test3':3}")
print("-----------------------------------------------------------------------")
for i in range(0,len(fName)):
    print(f"{fName[i]:8}    {lName[i]:8}     {test1[i]:3}     {test2[i]:3}     {test3[i]:3}")'''
        
#Commented out to save me the hassle of repeating lists, becomes a little to much to handle 
        
        
        
#PART 2 BELOW

for i in range (0,len(test1)):
    a = (test1[i] + test2[i] +test3[i]) / 3 #short term for average, just to make it easy
    num_avg.append(float(a))
    l = letter(a) #Used to just call letter
    lgrade.append(l)



print(f"{'FirstName':8}   {'LastName':8}   {'Test 1':3}   {'Test 2':3}  {'Test3':3}    {"Average":3}  {"Avg Letter"}")
print("------------------------------------------------------------------------------------------------------------------------------")
#Part 2 print statment
for i in range(0,len(fName)):#INDEX ARE KEY TO OUR CODE ACTUALLY WORKING
    print(f"{fName[i]:8}    {lName[i]:8}     {test1[i]:3}     {test2[i]:3}     {test3[i]:3}    {num_avg[i]:3.2f}    {lgrade[i]}")


#PART 3--- Search 
ans = "y"
while ans == "y":
    search_type = menu()
    
    print(f"{'FirstName':8}   {'LastName':8}   {'Test 1':3}   {'Test 2':3}  {'Test3':3}    {"Average":3}  {"Avg Letter"}")
    print("------------------------------------------------------------------------------------------------------------------------------")
    
    
    
    if search_type == "1":
        found = -1 #SET IT TO AN INVALID INDEX NUMBER. 
        search_name = input("Input the LAST NAME of the student your searching for: ")
        for i in range(0, len(lName)):
            if search_name.lower() == lName[i].lower():
                found = i
        
        if found != -1:
            print(f"Your Search for {search_name} WAR FOUND!")
            print(f"{fName[found]:8}    {lName[found]:8}     {test1[found]:3}     {test2[found]:3}     {test3[found]:3}    {num_avg[found]:3.2f}    {lgrade[found]}")
        
        else:
            print(f"Your Search for {search_name} want found :(")
    
    
    
    elif search_type == "2":
        found = -1 #SET IT TO AN INVALID INDEX NUMBER. 
        search_name = input("Input the LAST NAME of the student your searching for: ")
        for i in range(0, len(fName)):
            if search_name.lower() == fName[i].lower():
                found = i
        
        if found != -1:
            print(f"Your Search for {search_name} WAR FOUND!")
            print(f"{fName[found]:8}    {lName[found]:8}     {test1[found]:3}     {test2[found]:3}     {test3[found]:3}    {num_avg[found]:3.2f}    {lgrade[found]}")
        else:
            print(f"Your Search for {search_name} want found :(")
            
            
            
            
    elif search_type == "3":
        found = []
        
        
        #get the search item from the user
        search_grade = input("Enter the Letter Grade you are searching for: ")
        
        #perform the search
        for i in range (0, len(lgrade)):
            if search_grade.upper() == lgrade[i]:
                #IF STATMENTS MEAN SEARCHING
                found.append(i)#add the current index, found can be used later to display
        
        if not found: #This means the list is empty!
            print (f"Your search for {search_grade} was NOT found!")
            print(f"Remember this is case sensitive please try again")
        else:
            print (f"Your search for {search_grade} was Found!")
            for i in range (0, len(found)):
                if i < len(found) - 1:
                    print(f"{fName[found[i]]:8}    {lName[found[i]]:8}     {test1[found[i]]:3}     {test2[found[i]]:3}     {test3[found[i]]:3}    {num_avg[found[i]]:3.2f}    {lgrade[found[i]]}")
                
                
    
    elif search_type == "4":
        print("Goodbye")
        ans = "n"
    else:
        print("ERROR IMPROPER SYNTAX: Please try again")