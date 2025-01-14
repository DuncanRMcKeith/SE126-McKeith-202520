#Duncan McKeith
#1-14-2025 
#SE 126: Intermidate Python
#Week 2 In Class Lab


#Program Prompt:Using a CSV file containing a list of rooms (Along with their room caps, and the current amount of people). Then, using that file, determine which rooms are overcapped and by how much, and display them back to the user. Along with how many total rooms have been checked. 


#Variable Dictionary
#people = the amount of people within the room
#maxcap = the maximum amount of people allowed in a room
#seats total = amount that allows us to check if the rooms overcapped(negative number) full or undercapped
#total_rec = total amount of records recorded
#rooms_overlimit = how many rooms are over the limit of people
#file = our csv file
#rec = record or row within the file
#room = catagory of rooms within the csv file
#maxx = maximum amount of people within the csv file



#-------MAIN CODE BELOW-----------------


#IMPORTS
import csv
#Two defined variables that directly are effected by the CSV


#FUNCTIONS

#Reusing functions from lab 1 along with some other elements
def difference (people, maxcap): #Hey look its the function header
    '''This function is designed to figure out the diffrence between the amount of people in the room and its total max seats'''

    seats_total = maxcap - people #Note we could have set this number to be the absolute value however we are going to do that later on in our code so that its easier to sort. 
    return seats_total 


#CODE
#Initializing variables
total_rec = 0
rooms_overlimit = 0 
#CONNECT THE CSV FILE
print (f"{'ROOM':20}             {'MAX':5}           {'OVER':5}")
print("------------------------------------------------------------------")
with open("Txt_Files/classLab2.csv") as csvfile:
    
    
    file = csv.reader(csvfile) #allowing it to read the csv file
    
    
    for rec in file: 
        total_rec += 1
        #We dont count rooms overlimit just yet, as we havent actually done the math to check it out
        
        
        #Now going to print out the room, max, and min to just double check that stuffs working
        room = rec [0]
        maxx = int(rec [1]) #Extra x and n here with max and min as they are both functions and i dont feel like having it overlap.
        people = int(rec [2])
        remaining = difference(people,maxx)
        if remaining <0:
            print (f"{room:20}           {maxx:5}          {abs(remaining):5}")
            rooms_overlimit += 1 
        
#Display the final data
print("------------------------------------------------------------------")
print(f"Rooms Over:{rooms_overlimit}")
print(f"Total Rooms Recorded {total_rec}")