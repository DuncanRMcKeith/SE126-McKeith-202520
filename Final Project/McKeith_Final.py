#Duncan McKeith
#3-11-2025
#SE 126: Intermidiate Python
#Final Project


#Program Prompt: This program Is a DND notes app, That will allow the user to view, edit, search, and add to a csv file. The catagories are names, organization, location, and additional notes. The CSV file is also designed to be created as soon as its run for the first time. 

#Variable Dictionary:
#names = Names list variable
# org = organization list variable(orgainization in this means group associated with npc)
# location = last location list variable. 
# notes = Notes list variable
# ans = while loop variable
# fun = Okay this is a weird tracker i made to allow a opening msg if = 0 then changing the value so the opening msg doesnt replay. Needed to be done both at a local(within the function) and global(within the code) scale.
# campaign_notes = Starting csv data, Just  a user input on if they would like them or not(if no they create a blank csv file named the same thing just without data)
# found = sequential search for when we find something
# search = user input for what they are searching for
# add_name = Variable for what they want the new name to add into the csv file
# add_org = variable for what organization that NPCS org belongs to
# add_location = variable for what location that NPC was last seen in
# add_notes = variable for notes for that npc
# edit = While loop variable for editing, if y they continue editing data, if no they stop and return to the main user menu
# edit_name = Variable input for what the user would like to change the specific NPCS name to
# edit_org = variable input for what the user would like to change the NPCS associated org to 
# edit_location = variable input for what they user would like to change the NPCS last location to
# edit_notes1 = Variable input for what the user would like to ADD to the NPCs notes
# edit_notes2 = Variable input for the entire notes that allows the user to change the Notes, this will replace the current notes in its entirty. 

#-----IMPORTS--------------------------------------------
import csv
import os
from os import system, name 
from time import sleep 
#-----FUNCTIONS-------------------------------------------
def menu(fun):
    '''This is a basic menu function, that will handle the print statments and return the choice back to the main program.'''
    #Fun print statement, We should only have this trigger the first time so lets create a variable that then will increase after the print statment
    #fun = 0 <---- note This didnt work, since we always reset it to 0.... Dumb 
    if fun == 0:
        print("\t\tWelcome Adventurer! To the Arcanum Of NOTES!")
        print("This magical index will allow you to keep track of details along you travel, this way you may stop asking the gods of this realm who or what is happening.")
        fun += 1 #Okay so we need to change this on both a global scale and a non global scale
    else:
        print("Welcome Back Adventurer")
  
    
    print("1.Show All Records")
    print("2.Search By Name")
    print("3.Search By Organization")
    print("4.Search by Last know Location")
    print("5.Add an entry")
    print("6.Edit an entry")
    print("7.Seal the Index.... for now")
    menu_choice = input("Please Select from The Index [1-7]")
    while menu_choice not in ['1','2','3','4','5','6','7']:
        print("Ah... please select a proper entry")
        menu_choice = input("Please Select from The Index [1-7]")
    return menu_choice 
# import only system from os 

  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def check(var):
    '''This is a system of checks to make sure the user doesnt add in bad stuff to the variable
    Var = Varaible input required to check pass input check '''
    var = var.replace(",","")
    while var == "":
        print("Pardon me but you cant add blanks into the index")
        var = input("Name You would like to add to the index: ").strip()
    return var
    
    


#-----EXECUTING CODE BELOW--------------------------------
clear()#Gotta clear away all the excesses junk.
names = []
org = []
location = [] #Note this stands for last location not current location as npcs and people can move,
notes = []
ans = "y"
fun = 0
# checks for file, if not found, generates new list:
if not os.path.exists('Final Project/dndnotes.csv'):
    print("\n No Notes File Found. Generating New Notepad Adventurer!")
    #create and save a fresh csv file below
    campaign_notes = input("Would you like to generate starting notes?[y/n] ").lower() #For this sake, would you like the Starting Csv Or not
    while campaign_notes not in ["y",'n']:
        print("Error, Please Select y or n")
        campaign_notes = input("Would you like to generate starting notes?[y/n] ").lower()
    if campaign_notes == 'y':
        file = open("Final Project/dndnotes.csv", 'w')
        file.write("Gargus,unafiliated,Rotwood,Investigator whose slightly unstable\n")
        file.write("Tyrus The Unfallen,Covenant of The Abyss,Church of The Damned, a former religous zelot who abadoned his faith. Lusts after power and tricked into service by the demon kings promises\n")
        file.write('Calico,Clan of Wu,36 Chambers, Wanted Criminal: Guilty of kidnapping and murder of the king\n')
        file.write('Relic,Shadow Assassins,Forest of Lost Souls, No current informations....\n')
        file.write('Seramua,unafiliated,Waterdeep Woods,Sage ; Pstuodragon Familiar; Mystery Solver\n')
        file.write('Donut,Church of Aeyri Faeydrun,FaeWild,Crazy Blue Kobold Obsessive with donuts and Lightning. Tempest Cleric\n')
        file.write('Zacharius,Hunters Guild,Underdark,Aasimar of the fair gods. Detective Who lost his arm on a case.\n')
        file.write('Dustin Hazel,Hunters Guild,Underdark,Sleezy Scam artist bound in service to baba yaga. Warlock capable of inflicting unknown amounts of damage to the world\n')
        file.write('Giocomo,Larona,Underdark,Teacher to princess Isabella(AKA Fig). Former War Vet. Kind of an alcholic...\n')
        file.write('Finnella,Spring Court,Wilds of Edramis,Patron of Swan-mays Swans and communication. Currently in a relationship with Verenestra although maybe isnt? Kinda weird')
    else:
        file = open("Final Project/dndnotes.csv", 'w')


#Alright! Now by this point we have guarenteed a file is generated at the right spot. 
with open ("Final Project/dndnotes.csv", 'r') as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        names.append(rec[0])
        org.append(rec[1])
        location.append(rec[2])
        notes.append(rec[3])
#Disconnect now from file, from here on out we are in our menu and will be working within a while loop
while ans == "y":
    choice = menu(fun)
    fun += 1 #Okay so this the first time the code will run will read as 0 From there on out the value will change to not be 0
    if choice == "1":
        #Just show all the answers
        print(f"{'Name':20} {'Organization':25} {'Last Location'}")
        print("-"*60)
        for i in range(0,len(names)):
            print(f"{names[i]:20} {org[i]:25} {location[i]}")

    if choice == "2":
        #Simple sequential search
        found = -1
        search = input("Please Write the Name your searching for: ").lower()
        for i in range(0,len(names)):
            if search.lower() == names[i].lower():
                found = i
        if found != -1:
            print(f"{search} entry was found")
            print(f"{'Name':20} {'Organization':25} {'Last Location'}")
            print("-"*60)
            print(f"{names[found]:20} {org[found]:25} {location[found]}")
            print(f"Notes: {notes[found]}")
        else:
            print(f"Apologies There are no Entries for {search}\n Please Try again or add a new entry")


    if choice == "3":
        #Can be multiple within an organization, so its a sequential search again but this time now a list
        found = [] 
        search = input("Please Write the organization your searching for: ").lower()
        for i in range(0,len(org)):
            if search.lower() == org[i].lower():
                found.append(i)
        if not found:
            print(f"Apologies your search for {search} was not found")
        else:
            print(f"Your search for {search} was found")
            print(f"{'Name':20} {'Organization':25} {'Last Location'}")
            print('-'*60)
            for i in range(0,len(found)):
                print(f"{names[found[i]]:20} {org[found[i]]:25} {location[found[i]]}")
                print(f"Notes: {notes[found[i]]}")

    if choice == "4":
        #Another seqential search in a list, in reality just have to change org to location.     
        found = []
        search = input("What Location are you searching for?: ")
        for i in range(0,len(location)):
            if search.lower() == location[i].lower():
                found.append(i)
        if not found:
            print(f"Apologies your search for {search} was not found")
        else:
            print(f"Your search for {search} was found")
            print(f"{'Name':20} {'Organization':25} {'Last Location'}")
            print('-'*60)
            for i in range(0,len(found)):
                print(f"{names[found[i]]:20} {org[found[i]]:25} {location[found[i]]}")
                print(f"Notes: {notes[found[i]]}")

    #OKAY EASY STUFF DONE, now we enter the hell of constant checks and survalience to ensure someone doesnt break the entire code. 
    if choice == "5":
        
        found = -1 
        add_name = input("Name You would like to add to the index: ").strip()
        #First check to make sure its not a name already within our index, for this we will use found
        for i in range(0,len(names)):
            if add_name.lower() == names[i].lower():
                found = 1
        if found != -1:
            print("This Entry already exists! Please either edit or search your notes!")
        else:
            add_name = check(add_name)
            #Okay list of checks is done, now we get to all the other checks....
        add_org = input("What Organization are they a part of? [If Unafliated Type Unafilated]: ").strip()
        add_org = check(add_org)
        add_location = input("Where were they last located? ").strip()
        add_location = check(add_location)
        add_notes = input("Add in any additional notes!").strip()
        add_notes = check(add_notes)
        #OKAY ALL INFOS IN, now we need to add it to the lists
        names.append(add_name)
        org.append(add_org)
        location.append(add_location)
        notes.append(add_notes)

        
    if choice == "6":
        #print("6.Edit an entry")
        #Okay so now we split this into 3 parts, 1ST. What entry are we replacing?(Seqential search for names). 2ND We need to ask the user what there replacing, so small menu. 3RD. replacing the actual data


        edit = "y"
        found = -1
        #1ST

        search = input("Whose Entry are we editing? ")
        for i in range(0,len(names)):
            if search.lower() == names[i].lower():
                found = i
        if found != -1:
            print(f"{search} entry was found")
            print(f"{'Name':20} {'Organization':25} {'Last Location'}")
            print("-"*60)
            print(f"{names[found]:20} {org[found]:25} {location[found]}")
            print(f"Notes: {notes[found]}")
        else:
            print(f"Apologies There are no Entries for {search}\n Please Try again or add a new entry")
        #2ND.

        while edit == "y":
            print("Please Select From Menu below on what Data were editing")
            print("1.Name")
            print("2.Org")
            print("3.Location")
            print("4.Add Notes")
            print("5.Edit Current Notes")
            choice = input("").strip()
            #3RD.
            if choice == "1": #This is a fairly simple replace, replace what we found earleier with our new user input
                edit_name = input("Oh? What is their name now?: ").strip()
                check(edit_name)
                names[found] = edit_name
            if choice == "2":
                edit_org = input("PlotTwist! What Organization do they belong to now?: ").strip()
                check(edit_org)
                org[found] = edit_org
            if choice == "3":
                edit_location = input("Where are they now?: ").strip()
                check(edit_location)
                location[found] = edit_location
            if choice == "4":
                edit_notes1 = input("OH? what new lore did you find?: ") #Notice we didnt add a .strip as we dont really care if its blank, its just adding in spaces. 
                check(edit_notes1)
                notes[found] = notes[found] + edit_notes1
            if choice == "5": #OKAY, now we 
                print(notes[found]) 
                edit_notes2 = input("Please Write your replacement notes (See above for what you had before :) )").strip()
                check(edit_notes2)
                notes[found] = edit_notes2
            else:
                print("Error thats not within the choices, please Try again.")
            edit = input("Would you like to keep editing?[y/n]").lower()
            while edit != "y" and edit != "n":
                print(f"Error Im not sure what you mean by{edit}. Please try again")
                edit = input("Would you like to keep editing?[y/n]").lower()

    if choice == "7":
        print("Closing the index. Safe Travels Adventurer!")
        ans = "n"
    input("Press Enter to Continue")
    clear()

#OKAY NOW LAST BUT CERTAINLY not least. WE Overwrite the csv file so that we get all the new data in there. 
file = open("Final Project/dndnotes.csv", 'w')
for i in range(0,len(names)):
    if i < len(names)-1:
        file.write(f"{names[i]},{org[i]},{location[i]},{notes[i]}\n")
    else:
        file.write(f"{names[i]},{org[i]},{location[i]},{notes[i]}")
file.close
