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

#-----EXECUTING CODE BELOW--------------------------------
dnd_notes = {

}
total_rec = 0 
# checks for file, if not found, generates new list:
if not os.path.exists('Final Project/dndnotes.csv'):
    print("\n No Notes File Found. Generating New Notepad Adventurer!")
    #create and save a fresh csv file below

else:
    with open("Final Project/dndnotes.csv",'r') as file:
        #here you open csv file and then populate the lists. SO HERE:
        file = csv.reader(file)
        for rec in file: