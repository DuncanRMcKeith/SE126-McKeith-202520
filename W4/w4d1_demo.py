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
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    
    #Can also be num_avg.append(test1[i] + test2 [i] + test3 [i] / 3)
    l=letter(a)
    l_avg.append(l)
    #l_avg.append(letter(num_avg[i]))
    
print(f"{"f_name":10} {"l_name":10} {"test1":3} {"test2":3} {"test3":3} {"num_avg":6} {"l_avg"}")
for i in range (0, len(f_name)):
    print(f"{f_name[i]:10} {l_name[i]:10} {test1[i]:3} {test2[i]:3} {test3[i]:3} {num_avg[i]:6.2f} {l_avg[i]}")
    
    
#write a program that allows a user to repeatdly search for a student by their last name or their letter grade; when a specific user is found, display all data relevant on that user, when not found alerat the user. When searching by letter grade, display all of the students' data when found or aleart the user that no student grades fit that description
print( "\t Welcomne to the student search program\n\n")

ans = input("Would you like to begin searching? [y/n]").lower()

while ans == "y":
    
    #get search type from user
    print("\tSearch Menu Options")
    print("1. Search By last Name")
    print("2. search By Letter Grade")
    print("3. Exit")
    search_type = input("Enter your search type [1-3]")
    
    
    if search_type == "1":
        print("Last name")
        found = -1#Invalid index number, will use to cvheck later if a student has been found
        
        #get search item from user
        search_name = input ("Enter the LAST NAME of the student your searching for: ")
        
        #perform search
        for i in range (0,len(l_name)):
            #the FOR LOOP allows for the sequence part --> from the beginning to the end
            if search_name.lower() == l_name[i].lower():
                #the IF STATEMENT allows for the search part
                found =  i #make your found the current index, can be used later to display.  Think of found like a flag, 
        
        
        if found != -1:
            print(f"Your search for {search_name} was Found!")
            print(f"{f_name[found]:10} {l_name[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {num_avg[found]:6.2f} {l_avg[found]}")
        else: 
            print(f"Your search for {search_name} was 'NOT' Found")
            print(F"This is a cAsE Sensitive program - check your spelling and casing try again!")
   
   
   
    elif search_type =="2":
        found = []
        
        
        #get the search item from the user
        search_grade = input("Enter the Letter Grade you are searching for: ")
        
        #perform the search
        for i in range (0, len(l_avg)):
            if search_grade.upper() == l_avg[i]:
                #IF STATMENTS MEAN SEARCHING
                found.append(i)#add the current index, found can be used later to display
        
        if not found: #This means the list is empty!
            print (f"Your search for {search_grade} was NOT found!")
            print(f"Remember this is case sensitive please try again")
        else:
            print (f"Your search for {search_grade} was Found!")
            for i in range (0, len(found)):
                print (f"{f_name[found[i]]:10} {l_name[found[i]]:10} {test1[found[i]]:3} {test2[found[i]]:3} {test3[found[i]]:3} {num_avg[found[i]]:6.2f} {l_avg[found[i]]}")
    elif search_type == "3":
        ans = "n"
    else:
        print("invalid entry")
        
    if search_type != 3: 
        ans = input("Would you like to search again?")
