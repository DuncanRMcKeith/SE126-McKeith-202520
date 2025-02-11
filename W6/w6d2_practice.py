###Duncan McKeith
#2-11-2025 
#SE 126: Intermidate Python
#WEEK 6 DAY 2 DEMO: Binary Search Review+ Bubble Search\

# PROGRAM PROMPT: Build a repeatable, menu driven program to acess and search for data within this file

#--IMPORTS---------------------------------------------------
import csv

#--FUNCTIONS---------------------------------------------------
def display(x, foundList, records):
    '''PARAMATERS
        X signifier for if we are printing a single record or multiple
            when x != "x" we have one value, otherwise we have mutliple.
            
        records = the length of a list we are going to process throught (# of loops/prints) 
            really this is passed the length of a list, to set how many times it would need to print in repetable lists
        
    '''
    print(f"{'CLASS':8} {'NAME':8} {'MEANING':25} {'CULTURE'}")
    print("----------------------------------------------------------------------------------------")
    if x !="x":
        #Printing one record, 
        print(f"{class_type[x]:8} {name[x]:8} {meaning[x]:25} {culture[x]}")
    elif foundList:
        for i in range(0,records):
            print(print(f"{class_type[foundList[i]]:8} {name[foundList[i]]:8} {meaning[foundList[i]]:25} {culture[foundList[i]]}"))
    else:
        for i in range(0,records):
            print(f"{class_type[i]:8} {name[i]:8} {meaning[i]:25} {culture[i]}")

def swap(i, listname):
    temp = listname[i] #temp stands for tempory value. 
    listname[index] = listname[index + 1]
    listname[index + 1] = temp
    




#--MAIN EXECUTING CODE-----------------------------------------

class_type = []
name = []
meaning = []
culture = []

practice = ['Austin','Cory','Noah','Duncan','Justyn']

with open ("Txt_Files/party.csv", encoding= "utf-8") as csvfile: 
    file = csv.reader(csvfile)
    
    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])

display(9,0,len(class_type)) #Practice with function. 

ans = input("Would you like to enter the search program [y/n]").lower()

while ans != "y" and ans != "n":
    print("***INVALID ENTRY***")
    ans = input("Would you like to enter the search program [y/n]").lower()

while ans == "y":
    print("\tSEARCHIING MENU")
    print("1. Search by TYPE") #Shows all of either elf or dragon
    print("2. Search by NAME") #binary search review
    print("3. Search by Meaning") #Bubble 
    print("4. EXIT")
    
    search_type = input("\t How would you like to search today [1-4]: ")
    
    #using 'not in' for user validity checks
    if search_type not in ['1','2','3','4']:
        print("***INVALID ENTRY!***\nPlease try Again!")
    
    elif search_type =="1":
        print(f"You have choosen to Search by Type")
        
        search = input("Which type: 'dragon' or 'elf': ").lower()
        if search not in ['dragon','elf']:
        #could also be if search.title() not in class_type:
            print("Invalid Entry PLease try again")
        else:
            found = []
            for i in range(0,len(class_type)):
                found
                if search.lower() == class_type[i].lower():
                    found.append(i)
            
            
            if not found:
                print(f"Sorry your search for {search} could not be completed")
            else:
                print(f"Your search for {search} is complete! Details Below")
                display("x",found, len(found))
        
    elif search_type == "2":
        #BINARY SEARCH
        #               *Requires a collection of UNIQUE values to search through
        #               * Requires the collection to be sorted (ORDERED)
        #               *       ascending Decending order
        #BUBBLE SORT----------------------------------------
        for i in range(0, len(name) - 1):#outter loop

            for index in range(0, len(name) - 1):#inner loop

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing


                if(name[index] > name[index + 1]):
                    #if above is true, swap places!

        

                    swap(index, name)
                    #swap all other values
                    swap(index,class_type)
                    swap(index,meaning)
                    swap(index,culture)
        display("x",0,len(name))
        #Binary Search
        search = input("Enter the NAME you are looking for: ")
        min = 0
        max = len(name)
        mid = int((min+max) / 2)
        while min < max and search != name[mid]:
            if search < name[mid]:
                max= mid - 1
            else:
                min = mid + 1
                
            mid = int((min+max) / 2)
            
        if search == name[mid]:
            display(mid, 0, len(name))
        else:
            print(f"\n Your search for {search} came up empty :[")
            
    elif search_type == "3":
        print(f"\n You have chosen to search by MEANING")
        search = input("Which Meaning are you looking for?: ").lower()
        
        found=[]
        
        for i in range(0, len(meaning)):
            if search.lower() in meaning[i].lower():
                found.append(i)
        
        if not found:
            print(f"Sorry, We have no names Related to that meaning in our catalog: {search}")
        else:
            display("x", found, len(found))
    elif search_type == "4":
        print("GOOD BYE")
        ans = "N"