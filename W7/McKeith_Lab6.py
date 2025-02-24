#Duncan McKeith
#2-23-2025 
#SE 126: Intermidate Python
#LAB 6

#Program Prompt:Write a Python program using lists (1D or 2D) to assign passengers seats in an airplaneAfter displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated. This continues until all seats are filled or until the user signals that the program should end. If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice. You must use a function to display the seating map 


#Variable Dictonary
#seatA = List variable for seats in collum A
# seatB = List variable for seats in collum B
# seatC = List variable for seats in collum C
# seatD= List variable for seats in collum D
# opt = option within menu: User input to control menu
# valid_opt = just a list used to check if a valid choice was made
# row = row is the row chosen to be reserved
# seat = which seat they would like to reserve
# answer = while loop key

#--Imports----------------------------------------------
import csv

#--Functions---------------------------------------------
def seatMap(): #Shout outs to week 7 day 1 demo wooooo. 
    print(f"{'ROW':3}   {'A':3} {'B':3}   {'C':3} {'D':3}")
    print("---------------------------------------------------------------")
    for i in range(len(seatA)):
        print(f"{i + 1:3}   {seatA[i]:3} {seatB[i]:3}   {seatC[i]:3} {seatD[i]:3}")
    print("---------------------------------------------------------------")
    
    
    
    
def menu():
    '''This is the main menu for the people to choose what they would like to do, going to have a display seats, and choose seats as well as end the program essentially allowing the user to reserve more seats or stop''' 
    print("\tSerpents Airline Flight 727")
    print("1.Display Seats")
    print("2.Choose from Avalaible Seats")
    print("3.Exit")
    opt = input("Please Select from the options above: ")
    valid_opt  = ["1","2","3"]
    while opt not in valid_opt:
        print("ERROR IMPROPER OPTION CHOSEN")
        opt = input("Please Select from the options above: ")
    return opt

#--Executable Code
#Starting off with the seating lists, these are handpopulated lists, now we need to make sure we write a program to edit it
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']
seat_total= [seatA,seatB,seatC,seatD]
seat_opt = ["A","B","C","D"]
'''for i in range(0,len(seat_choosen)):
    print(seat_choosen[i])''' #These lines were originally a check to see if i could put all the lists together then have seat options as a sort of check to see if all seats were taken up. 
answer = "y"



while answer == "y": #USER CANT EXIT UNLESSS THEY PICK OPTION 3. AKA USER IS ASKED IF THEY WANNA KEEP BOOKING THEN AFTER THEY ARE DONE THE PROGRAM ENDS. 
    for i in range(0,len(seat_total)):
        for x in range(0,len(seat_total[i])):
            if seat_opt[0] not in seat_total[i] or seat_opt[1] not in seat_total[i] or seat_opt[2] not in seat_total[i] or seat_opt[3] not in seat_total[i]: #AKA ALL ARE X
                print("This current flight is fully booked sorry for the inconvience.")
                answer = "n"
                
                
    #Else there are still seats avaliable
    option = menu()
    
    if option == "1":
        seatMap() #Just Prin the seatmap
        
        

    if option == "2":
        print("Reserving Seats")
        #Now we make the inputs for seat and row, with loops to trap the person if they dont choose between 1-7 and A-D
        seat_ans = "y"
        while seat_ans == 'y':
            row = int(input("Enter which row you'd like to sit in [1-7]: "))
            while row not in [1,2,3,4,5,6,7]:
                print("Error Row Not found Please try again")
                row = int(input("Enter which row you'd like to sit in [1-7]: "))


            seat = input("Enter which seat you'd like to sit in [A/B/C/D]: ").upper()
            while seat not in ["A","B",'C','D']:
                print("Error Seat Not Found Please try Again")
                seat = input("Enter which seat you'd like to sit in [A/B/C/D]: ")
            
            #We know Row = i +1 and we know which seat they wanna replace so now we set conditional statments to check each index essentially till we reach the one we wanna replace.
            
            for i in range(0,len(seatA)):
                if row - 1 == i: #If i+1 = row then row-1 = i. This line is saying okay if we reach the correct row in this file, THEN WE REPLACE. otherwise we dont do anything. 
                    if seat == 'A' and seatA[i] != 'X':
                        seatA[i] = 'X'
                    elif seat == 'B' and seatB[i] != 'X':
                        seatB[i] = 'X'
                    elif seat == 'C' and seatC[i] != 'X':
                        seatC[i] = 'X'
                    elif seat =='D' and seatD[i] != 'X':
                        seatD[i] = 'X'
                    else:
                        print("Choosen Seat Has Already Been reserved Please Try again")
        
            seat_ans = input("Would you like to continue reserving seats? [y/n]".lower())
            while seat_ans not in ["y","n"]:
                print("Error Improper Syntax")
                seat_ans = input("Would you like to continue reserving seats? [y/n]".lower())

    if option == "3":#Cheeky fun for exiting the file. B
        print("Thank you Now Charging card on file for these seats")
        answer = "n"

print("Have a Fantastic Flight!")

    