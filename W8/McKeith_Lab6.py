#Duncan McKeith
#3-2-2025
#SE 126: Intermidiate Python
#Lab 6


#Program Prompt:

#Variable Dictionary:



#----------------------MAIN CODE BELOW-------------------------------------

#Imports:
import csv

#Functions
def menu():
    '''This Menu Function will display the 4 options the user can use, then prompt the user for their choice. Then will return the choice back into the executing code.'''
    print("\t\tHi Welcome to Python Words Dictionary")
    print("\t1.Show all current words")
    print("\t2.Search for a word!")
    print("\t3.Add a word to the dictionary")
    print("\t4.Exit")
    menu_opt= input("Please Select From the options above!")
    while menu_opt not in ['1','2','3','4']:
        print("Error Option Not avalible Please choose from listed options.")
        menu_opt= input("Please Select From the options above!")
    return menu_opt
#Executing Code:
#Opening Variables: Including empty lists and loop keys
ans = "y"
words = {
    
}

with open ('Txt_Files/words.csv') as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        words.update({rec[0] : rec[1]})



#Original Test to make sure dictionary was populating, will be used later on for the keywords. 
'''
for key in words:
    print(f"{key:20}:\t{words[key]}")
   '''     
while ans == "y":
    opt = menu()
    if opt == "1":
        print (f"{'Words':20}:\t{'Definitions'}")
        print('-'*50)
        for key in words:
            print(f"{key:20}:\t{words[key]}")
        print('-'*50)
    elif opt == "2":
        print("search for a word")
    elif opt == "3":
        print("Add a word")
    elif opt == "4": #Funny enough this is always the first code i add to my loops even before i make a menu functions. WHEN YOU MAKE A LOOP YOU SURE HAVE A WAY TO CLOSE IT
        ans = "n"