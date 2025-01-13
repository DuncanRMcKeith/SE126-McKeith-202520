#Duncan McKeith
#1-7-2025 
#SE 126: Intermidate Python
#Lab 1


#Program Prompt:a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program

#Variable Dictionary
#seats_total = within a function call, used to give us the amount of people within a room(Could be either positive or negative)
#max_cap = maximum amount of people allowed in a room
#people = amount of people actually in the room
#ans = just a short term for answer 
#answer = loop key
#final_room = total amount for the final room that we use to sort and tell the person if they have to many, too few, or just the right amount of people

#------------------MAIN CODE BELOW----------------------------
#Imported Functions- Noted None for this prompt. 


#Created Functions
def difference (people, maxcap): #Hey look its the function header
    '''This function is designed to figure out the diffrence between the amount of people in the room and its total max seats'''

    seats_total = maxcap - people #Note we could have set this number to be the absolute value however we are going to do that later on in our code so that its easier to sort. 
    return seats_total 

def decision (response):
    '''This is how we close our while loop. This function will then return the users response only if valid'''

    ans = input("Would you like to check another room? [y/n]").lower()

    #Time to trap the user
    while ans != "y" or ans != "n": #Note this needs to be a while loop otherwise if they put in the improper code twice then they lock themselves into going even if they did not.
        print("***Error Improper Character Used Please try again!")
        ans = input("Would you like to check another room? [y/n]").lower()
    
    return ans #Finally return the function

#------------Program Code------------------

#First define all known variables

answer = "y"
room_cap = 0
people = 0 
final_room = 0 

#Then begin the actual loop for our code--->Always start by importing our way out that way we can test to make sure it works as well as to be able to test our code at any point without repeating it infitely.
while answer == "y":
    #Remember to get our inputs before calling the function
    room_cap = int(input("What is the maximum amount of people allowed in the room?"))
    people = int(input ("How many people are currently in the room?"))
#Note i set the inputs above as integers so that i could later on sort them easier. 



    #Now call the main function ****ONLY AFTER ASSIGNING IT TO A VARAIABLE****
    final_room = difference({people},{room_cap})
    if final_room < 0 : 
        print(f"Woah There Slow Down! You have to many people! \n Please remove {abs(final_room)} people to meet the room cap")
    if final_room == 0 : 
        print(f"Nice Job there Champ! You are currently at the room capacity please dont add anyone else though \n If you do your breaking the law")
    if final_room > 0:
        print(f"Alright! Your still not at room capacity yet so you can add in {final_room} people!")
    else:
        print("This statment shouldnt be seen please relaunch the code") #This is just a test line to make sure everything is going fine. 
    answer = decision()


print("Thanks for checking your rooms, Thank you and have a wonderful day.")

#END OF CODE
