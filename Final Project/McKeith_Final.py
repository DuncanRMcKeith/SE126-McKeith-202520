#Duncan McKeith
#2-28-2025
#SE 126: Intermidiate Python
#Final Project


#Program Prompt:

#Variable Dictionary:


#-----IMPORTS--------------------------------------------
import csv
import os


#-----FUNCTIONS-------------------------------------------
def menu(fun):
    '''This is a basic menu function, that will handle the print statments and return the choice back to the main program.'''
    #Fun print statement, We should only have this trigger the first time so lets create a variable that then will increase after the print statment
    #fun = 0 <---- note This didnt work, since we always reset it to 0.... Dumb 
    if fun == 0:
        print("\t\tWelcome Adventurer! To the Arcanum Of NOTES!")
        print("This magical index will allow you to keep track of details along you travel, this way you may stop asking the gods of this realm who or what is happening.")
        fun +=1
    else:
        print("\t\tWelcome Back advenuture!")
    
    print("1.Show All Records")
    print("2.Search By Name")
    print("3.Search By Organization")
    print("4.Search by Last know Location")
    print("5.Add an entry")
    print("6.Seal the Index.... for now")
    menu_choice = input("Please Select from The Index")
    return fun, menu_choice




#-----EXECUTING CODE BELOW--------------------------------
name = []
org = []
location = [] #Note this stands for last location not current location as npcs and people can move,
notes = []
fun = 0 
ans = "y"
total_rec = 0

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
        name.append(rec[0])
        org.append(rec[1])
        location.append(rec[2])
        notes.append(rec[3])
#Disconnect now from file, from here on out we are in our menu and will be working within a while loop
while ans == "y":
    menu(fun)
    