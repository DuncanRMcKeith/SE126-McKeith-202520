#Duncan McKeith
#2-4-2025
#SE 126: Intermidiate Python
#Midterm 


#Program Prompt


#Variable Dictionary
#fName = List variable used to keep track of first names (rec 0)
# lName = list variable used to store last names (rec 1) into a list
# email = list variable used to store emails (rec 2)  into a list
# dept = list variable used to store departments (rec 3) into a list
# phone = list variable used to phone extensions (rec 4) into a list
# office = This is our created list, which we do by rec_processed + 100 so we stay in between the nesscary 100-200. This then is stored into a list, and stand for the individuals office number. 
# rec_processed = How many records have been processed. Also used in some calculations or, could be used for length. 
# answer = while loop key for out sequential search
# search = what our users attempt to search for, this is essentially the users input for what they want to search/
# found = sequential search -Either an item is or isnt found and stored its value to this thing. 
# search_mail = user input for searching by email
# search_dept = user input for searchy by department. Could have condesnsed with search_mail but i decided to make two seperate search variables. 


#-------------------------------------MAIN CODE BELOW-----------------------------------------------------------------------------------------------------------------

#IMPORTS
import csv

#FUNCTIONS
def menu():
    '''Menu function for controlling the sequential search later on in the program'''
    print("WESTEROS SERVICES DIRECTORY SEARCH")
    print("1.Search by EMAIL")
    print("2.Search by DEPARTMENT")
    print("3.EXIT")
    a = input("Please Pick from the Menu options as listed above ")
    while a != '1' and a != '2' and a != '3':
        a = input("Invalid Input Please Try Again!")
    return a
#CODE
#Start by creating empty lists for us to use CSV info
fName = [] 
lName = []
email = []
dept = []
phone = []
office = [] #Office numbers need to between 100-200 

#Then create a space where any additional variables can be added to at the start
rec_processed = 0 #Used to help create office numbers and display the data at the end
answer = "y"
#Now we intialize the File, and store the inital data given to us!
with open('Txt_Files/westeros.csv') as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        email.append(rec[2])
        dept.append(rec[3])
        phone.append(rec[4])
#Disconnect Here


#Now we need to create the office numbers for each of the people, easy way to do this

for i in range(0,len(fName)):
    office.append(rec_processed+100)
    rec_processed +=1



#Okay all info has now been gathered/made so we can now do the display
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3} {'OFFICE':3}")
print("-------------------------------------------------------------------------------------")
for i in range (0,len(fName)):
    print(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {dept[i]:23} {phone[i]:3} {office[i]:3}")
    
# Now finally we have this write out the end piece, which is how many records have been processed and writing a new csv file for the info

file = open('Txt_Files/midterm_choice1.csv','w')
for i in range(0,len(fName)):
    if i < len(fName) -1:
        file.write(f"{fName[i]}, {lName[i]}, {email[i]}, {dept[i]}, {phone[i]}, {office[i]}\n")
    else:
        file.write(f"{fName[i]}, {lName[i]}, {email[i]}, {dept[i]}, {phone[i]}, {office[i]}")
file.close()
    
    
print(f"Congrats You have Processed {rec_processed} Records.")
input("Now creating Additional file! Press enter to begin Searching. ")
print("\n\n\n\n")




#Okay so now we create sequential search
while answer == "y":
    search = menu() 
    #made a menu function i find it easier and much neater than having a bunch of lines during my sequential search
    if search == '1':
        found = -1 #Invalid INDEX- Will change if we find the ONE email address otherwise wont 
        
        search_mail = input("Please Enter in the Email Address for the Employee: ")
        
        for i in range(0,len(fName)):
            if search_mail.lower() == email[i].lower(): 
                found = i #NEW FLAG FOR SEARCH ONLY()
    
        if found != -1:  #AKA If we found it then we changed this to not equal -1
            print(f"Your Search for {search_mail}, HAS been found!")
            print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3} {'OFFICE':3}")
            #Added in to make the prompt not look so ugly
            print(f"{fName[found]:8} {lName[found]:10} {email[found]:30} {dept[found]:23} {phone[found]:3} {office[found]:3}")
        else:
            print(f"Your Search for {search_mail}, HAS NOT been found. Please Try again")
    
    
    
        
    elif search =='2':
        found = [] #Found needs to be a list cause there are multiples in each department, 
        search_dept = input("Which Department are you searching for?: ")
        
        #Now we search the entire list
        for i in range(0,len(fName)):
            if search_dept.lower() == dept[i].lower():
                found.append(i) #ADDS THE ENTIRE CURRENT ROW, meaning we found something 
        
        if not found: #List be empty
            print(f"Your Search for {search_dept} was not found. Please Try Again")
        else: 
            print(f"Your Search for {search_dept} WAS FOUND!")
            print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3} {'OFFICE':3}")
            for i in range(0, len(found)):
                print(f"{fName[found[i]]:8} {lName[found[i]]:10} {email[found[i]]:30} {dept[found[i]]:23} {phone[found[i]]:3} {office[found[i]]:3}")
      
      
      
        
    elif search == '3': #ONLY IF THEY SELECT 3 CAN THEY EXIT THIS PROGRAM
        answer = "n"
    else:
        print("ERROR PLEASE RELAUNCH PROGRAM") #SHOULD NEVER BE SEEN BUT HERE IN CASE I BREAK 
print("Thank you for Choosing Westeros Services. Where you Sit On the Iron Throne") #i had to end it in a joke... cant stop myself