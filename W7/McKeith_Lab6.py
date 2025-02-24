#Duncan McKeith
#2-23-2025 
#SE 126: Intermidate Python
#LAB 6

#Program Prompt:


#Variable Dictonary


#--Imports----------------------------------------------
import csv

#--Functions---------------------------------------------
def seatMap():
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
seat_choosen = [seatA,seatB,seatC,seatD]
seat_opt = ["A","B","C","D"]
'''for i in range(0,len(seat_choosen)):
    print(seat_choosen[i])'''
answer = "y"
while answer == "y":
    '''for i in range(0,seatA):
        if seat_opt not in seat_choosen: #AKA IF ALL ARE X
            print("This current flight is fully booked sorry for the inconvience.")
            answer == "n"'''
    #Else there are still seats avaliable
    option = menu()
    
    if option == "1":
        seatMap()
    if option == "2":
        print("Reserving Seats")
        #Now we make the inputs for seat and row, with loops to trap the person if they dont choose between 1-7 and A-D
        row = int(input("Enter which row you'd like to sit in [1-7]: "))
        while row not in [1,2,3,4,5,6,7]:
            print("Error Row Not found Please try again")
            row = int(input("Enter which row you'd like to sit in [1-7]: "))


        seat = input("Enter which seat you'd like to sit in [A/B/C/D]: ")
        while seat not in ["A","B",'C','D']:
            print("Error Seat Not Found Please try Again")
            seat = input("Enter which seat you'd like to sit in [A/B/C/D]: ")
        
        #We know Row = i +1 and we know which seat they wanna replace so now we set conditional statments to check each index essentially till we reach the one we wanna replace
        for i in range(0,len(seatA)):
            if row - 1 == i:
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
        
                

    if option == "3":
        print("Thank you Now Charging card on file for these seats")
        answer == "n"

    