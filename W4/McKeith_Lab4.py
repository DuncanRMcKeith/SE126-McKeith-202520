#Duncan McKeith
#2-2-2025
#SE 126: Intermidiate Python
#LAB 4 


#Program Prompt: This is a two part program where we populate lists based on file data, create new lists for said data, then create a brand new csv file. Specifically doing it for game of throne corp in creating new emails, departments, and unique phone extensions using data provided from got_emails.csv and then storing it into a list that is displayed back to the user. Then using that information create a brand new csvfile that will store First name, last name, email, dept, and phone extension. Then finally display all information found for each employee in department. 


#Variable Dictionary
#phone_ext = Variable used to create unique phone extension by adding this number to the respective departments range (EX:phone_ext+ 100 for R&D department)
#fName = first name list variable
# lName = last name list variable
# age = Age list variable (UNUSED DATA NOT NEEDED IN THE SLIGHTEST)
# sName = Screen Name list variable, used later on in code to create email list
# house = House allegience list, used later on in code to create department list
# email = Email list variable
# dept = department list variable
# phone = phone extension list variable,(What the actual phone_ext is)
# stark = Variable to keep track of how many are in r&d
# targ = Variable to keep track of how many are in marketing
# tully = Variable to keep track of how many are in HR
# lan = Variable to keep track of how many are in Accounting
# bar = Variable to keep track of how many are in Sales
# nWatch =Variable to keep track of how many are in auditing 
# employees = Variable to keep track of how many total employees data has been added to csv file



#---------CODE BELOW---------------------------


#IMPORTS
import csv

#FUNCTIONS


#=========================MAIN CODE===================================
#PART 1
#Start off with all of our lists
phone_ext =0 #This is what we use to make our (unique) phone numbers, also could be used to keep track of total range of people but i made an employees variable too because why not
fName = []
lName = []
age = []
sName = []
house = []
email = []
dept = []
phone = []

#List of variables used in part 2 to display totals KEEPS TRACK OF DEPT NOT HOUSE JUST EASIER TO REMEMBER THE VARIABLE NAMES AND CROSS CHECK LATER ON
stark = 0
targ = 0
tully = 0
lan = 0
bar = 0
nWatch = 0
employees = 0

with open("Txt_Files/got_emails.csv") as csvfile:

    file = csv.reader(csvfile)
    for rec in file: 
        employees += 1
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        sName.append(rec[3])
        house.append(rec[4])

#Disconnect from file
#All data from original list is now stored, now we can move on to creating additional lists that require us to do some index work in order to create UNIQUE phone numbers and set them into the proper catagories. 

for i in range(0,len(fName)):
    email.append(f"{sName[i]}@westeros.net")

    #print(email[i]) originally just a check line used in the program to make sure that we actually were creating the emails. now we move onto departments and phone extensions both of which can be done by the same exact if statement

    if "House Stark" == house[i]:
        dept.append("Research & Development")
        phone.append(phone_ext+100)
        phone_ext += 1 
        #This is to create unique phone numbers, couldnt figure out an easy way to generate ones between the ranges given but realized theres not 99 pieces of data so i am generating completely new ones every time(Still within there respectiveranges as we add the base of a phone extension to the number).
        stark += 1
    if "House Targaryen" == house[i]: 
        dept.append("Marketing")
        phone.append(phone_ext+200)
        phone_ext += 1
        targ += 1
    if "House Tully" == house[i]:
        dept.append("Human Resources")
        phone.append(phone_ext+300)
        phone_ext += 1
        tully += 1
    if "House Lannister" == house[i]:
        dept.append("Accounting")
        phone.append(phone_ext+400)
        phone_ext += 1 
        lan += 1
    if "House Baratheon" == house[i]:
        dept.append("Sales")
        phone.append(phone_ext+500)
        phone_ext += 1
        bar += 1
    if "The Night's Watch" == house[i]:
        dept.append("Auditing")
        phone.append(phone_ext+600)
        phone_ext += 1
        nWatch += 1 
    #Now we do a test print statment for the index to see if this worked
    #print(f"DEPT:{dept[i]}      Phone Ext:{phone[i]}")<---- Test worked

#NOW WE FINALLY PRINT THE FULL LIST WOHOOOO!(AKA PART 2 OF ASSIGNMENT)
print(f"{'First':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
print("-----------------------------------------------------------------------------------")
for i in range(0,len(fName)):
    print(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {dept[i]:23} {phone[i]:3}")

file = open('Txt_Files/westeros.csv', 'w') #Create new file as csv
for i in range(0,len(fName)): #AKA FOR EVERY REC WRITE A NEW ONE USING ONLY THIS DATA AS A CSV FILE.
    file.write(f"{fName[i]},{lName[i]},{email[i]},{dept[i]},{phone[i]}\n")
file.close()



print("\n\n\n") #Done to give space between first list and then the displayed total

print(f"\tCongrats A Updated File of Employee Info Has been Created")
print("-----------------------------------------------------------------------------------")
print(f"Total Employees In File: {employees}")
print(f"Total amount of Employees for Each Department on Record")
print(f"R&D: {stark} Marketing: {targ} HR: {tully} Accounting: {lan} Sales: {bar} Auditing {nWatch}")