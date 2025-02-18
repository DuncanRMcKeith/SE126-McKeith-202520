#Duncan McKeith
#2-18-2025
#SE 126: Intermidiate Python
#W7 D2: 2 dimensional listing: AKA FUN


#Program Prompt

#Variable Dictonary


#------MAIN CODE BELOW------


#Imports
import csv
#Functions
def swap (index, listname):
    temp = listname[index]
    listname[index] = listname[index+1]
    listname[index+1] = temp
def menu():
    print("\tSimple Searching Menu")
    print("1. Search By NAME")
    print("2. Search By NUM")
    print("3. Search By COLOR")
    print("4. EXIT")
    menu_choice = input("Enter your search type [1-4]: ")
    return menu_choice
#-----Executing Code--------------------------------------------------
names = []
nums = []
colors = []

with open("Txt_Files/simple.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2].title())

ans = "y"
valid_menu = ["1","2","3","4"]
while ans == "y":
    choice = menu()
    if choice not in valid_menu:
        print("INVALID! Please try again!")
    elif choice == "1":
        print("search by name")
        min = 0     #always starting value --->first index
        max = len(names)-1      #LAST INDEX / highest value in ascending ordered lists. 
        mid = int((min+max) /2)     #MIDDLE INDEX: Middle value in ascending order.
        
        search = input("Enter the NAME you are looking for: ")
        
        while min<max and search.lower() != names[mid].lower():
            if search < names[mid]:
                max = min - 1
            else:
                min = mid + 1
            mid = int((min+max) / 2)
        if search.lower() == names[mid].lower():
            #FOUND IT
            print(f"Congrats your Search for {search} was FOUND!")
            print(f"{'NAME':8}  {'NUM':3}   {'COLOR'}")
            print("---------------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}   {colors[mid]}")
            print("---------------------------------------------------")
        else:
            print(f"Sorry Your Search for {search} Was not found. Please try again")
            
    elif choice == "3":
        print("Search by colors")
        
        #WE BUBBLE BEFORE BINARY
        for i in range(0,len(colors)-1):
            for j in range(len(colors)-1):
                #see if "larger" value is in front of "smaller" value
                if colors[j] < colors[j+1]:
                    #SWAP Places! - not just this value, but all associated values
                    swap(j,colors)
                    swap(j,nums)
                    swap(j,names)
        min = 0     #always starting value --->first index
        max = len(colors)-1      #LAST INDEX / highest value in ascending ordered lists. 
        mid = int((min+max) /2)     #MIDDLE INDEX: Middle value in ascending order.
        
        search = input("Enter the COLORS you are looking for: ")
        
        while min<max and search.lower() !=colors[mid].lower():
            if search < colors[mid]:
                max = min - 1
            else:
                min = mid + 1
            mid = int((min+max) / 2)
        if search.lower() == colors[mid].lower():
            #FOUND IT
            print(f"Congrats your Search for {search} was FOUND!")
            print(f"{'NAME':8}  {'NUM':3}   {'COLOR'}")
            print("---------------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}   {colors[mid]}")
            print("---------------------------------------------------")
        else:
            print(f"Sorry Your Search for {search} Was not found. Please try again")
    elif choice == "2":
        print("search by num")
    elif choice == "4":
        ans = "n"

print("Thank you for using our progam. Good Day!")
    
        