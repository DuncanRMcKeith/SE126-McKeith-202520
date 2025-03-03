#Duncan McKeith
#3-2-2025
#SE 126: Intermidiate Python
#Lab 7


#Program Prompt:Build a mini programming dictionary a user can search through and ad to using the words.csv file, along with a menu to show, search, and add words to the dictionary as well as exit the program

#Variable Dictionary:
#ans = while loop key for main executing code
# opt = menu_opt
# menu_opt = user input for menu choice, can only be the values 1-4, located within the menu function
# found = Done for seqential search = If found if not found
# search = user input for what word they are searching for
# word_add = What word are you adding to the dictionary
# bad = a flag used to check to see if the word is already within the dictionary, If true then the rest of the code does not execute
# definition = what is the definition for the word_add chosen by the user, then checked twice to make sure the user isnt adding junk(Since we didnt make a remove function)
# 



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
    print(f"{key:20}:{words[key]}")
   '''     
while ans == "y":
    opt = menu()
    if opt == "1":
        print (f"{'Words':20}\n\t-{'Definitions'}")
        print('-'*50)
        for key in words:
            print(f"{key:20}\n\t-{words[key]}")
        print('-'*50)
    elif opt == "2":
        #Simple sequential Seach function dont need to overcomplicate it. 
        found = 0
        search = input("Please enter the word your searching for: ")
        for key in words:
            if search.lower() == key.lower():
                found = key
            #If the word is the same as the search(since words are our key in this way)
            
        if found != 0:
            print(f"{found}:\n\t{words[found]}")
        else:
            print(f"Your search for {search} is not found")


        
    elif opt == "3":
        word_add = input("What word would you like to add to your definitions?")
        bad = "n" #This is a flag we are using to check our word, making sure it is not already within the dictionary. 
        definition_key = "n" #This is to give the user another chance to check their definition to make sure its correct before adding it to the dictionary since we cannot edit this later on.
        for key in words:
            if word_add.lower() == key.lower():
                bad = "y"
        if bad == "y":
            print(f"Error! {word_add} already exists within dictionary. Returning to menu, please try again with a new word!")
        else:
            definition = str(input(f"What is the Definition for {word_add}?"))
            while definition_key == "n":
                print(f"{word_add} : \n\t{definition}")
                definition_key = input("Is what listed above Correct? [y/n]").lower()
                while definition_key not in['y','n']:
                    print("Error improper syntax please try again")
                    definition_key = input("Is what listed above Correct? [y/n]").lower()
                if definition_key == "n":
                    definition = str(input(f"What is the Definition for {word_add}?"))
            #Now i need to figure out how to append something to this! Cause setting it up like i did above except now with the terms word_add and definition doesnt work. 
                words.update({word_add : definition})#)------ISNT WORKING, cant tell why its not considering its like the exact same 
                
                #Note my issue was a single bracket of curlbraces.... Not 2.
            
    elif opt == "4": #Funny enough this is always the first code i add to my loops even before i make a menu functions. WHEN YOU MAKE A LOOP YOU SURE HAVE A WAY TO CLOSE IT
        ans = "n"
        
        
print("Thanks for Using Your Python word Dictonary")
print("Have a supercalafragalisticexpealidocious day!")