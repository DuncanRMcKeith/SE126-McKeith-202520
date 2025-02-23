#Duncan McKeith
#2-17-2025
#SE 126: Intermidiate Python
#Lab 5


#Program Prompt:


#Variable Dictionary


#--------------MAIN CODE BELOW-------------------------

#imports
import csv

#Functions
def menu():
    '''This function is designed to handle the menu for the entire program, just to minimize the amount of indentation below. This program will return the option choice back to the program to sort and catagorize everything.'''
    print("\t\tLibrary Options")
    print("\t1. Show All titles")
    print("\t2. Search by Title")
    print("\t3. Search by Author")
    print("\t4. Search by Genre")
    print("\t5. Search by Library Number")
    print("\t6. Show All Avaliable")
    print("\t7. Show All on Loan")
    print("\t8. Exit")
    search_opt = input("Please Select An option: [1-8] ")
    while search_opt not in ["1","2","3","4","5","6","7","8"]:
        print("ERROR! Invalid Option Please try again")
        search_opt = input("Please Select An option: [1-8] ")
    return search_opt

def swap(i, listname):
    '''Used to swap when doing bubble sort, do not touch'''
    temp = listname[i] #temp stands for tempory value. 
    listname[index] = listname[index + 1]
    listname[index + 1] = temp


#Executable Code
lib_num = []
title = []
author = []
genre = []
page_count = []
status = []
answer = "y"
with open("Txt_Files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        lib_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        page_count.append(rec[4])
        status.append(rec[5])
        
#empty list variables from csv file book_list.csv 
while answer == "y":
    search =menu()
    if search == "1":
        print ("Show all titles, via althebetical order")
        #Althebetical order means to sort. BUBBLE SORT NEEDS TO BE ACTIVE: 
        for i in range(0, len(title) - 1):#outter loop

            for index in range(0, len(title) - 1):#inner loop

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing


                if(title[index] > title[index + 1]):
                    #if above is true, swap places!

        

                    swap(index, title)
                    swap(index, lib_num)
                    swap(index, author)
                    swap(index, genre)
                    swap(index, page_count)
                    swap(index, status)
                    #swap all other values THIS IS THE BUBBLE SORT FOR TITLES, NOW WE CAN COPY AND SWAP STUFF AROUND AS NEED BE 
                  

    
        #PRINT STATMENT FOR OUR LAB- Could put in a function but will not since all my stuff got deleted :(
        print(f"{'LIB #':5}  {'TITLE ':35}  {'AUTHOR':20}  {'GENRE':20}  {'PAGES':5} {'STATUS'}")
        print("-------------------------------------------------------------------------------------------------------------------------------")
        for i in range(0,len(title)):
             print(f" {lib_num[i]:5}  {title[i]:35}  {author[i]:20}  {genre[i]:20}  {page_count[i]:5} {status[i]}")
    
    if search == "2":
        print ("Seach By title(CAN BE KEYWORDS)")
        #sequential search 
        search_title = input("Please enter the Title Your Searching for: ")
        found = [] #Have to do this in order to allow for terms and phrases. 
        for i in range(0,len(title)):
            if search_title.lower() in title[i].lower():
                found.append(i)
        if not found:#AKA LIST IS EMPTY
            print(f"Sorry your search for {search_title} is not in our Library please try again")
        else:#FOUND YOUR SEARCH, 
            print(f"{'LIB #':5}  {'TITLE ':35}  {'AUTHOR':20}  {'GENRE':20}  {'PAGES':5} {'STATUS'}")
            print("-------------------------------------------------------------------------------------------------------------------------------")
            for i in range(0,len(found)):
                print(f" {lib_num[found[i]]:5}  {title[found[i]]:35}  {author[found[i]]:20}  {genre[found[i]]:20}  {page_count[found[i]]:5} {status[found[i]]}") #FOUND= Found at this point in the list, kinda weird 

        

    if search == "3":
        print ("Search by Authors")
        #sequential search for a singular author needs to be a list, really just what above was except we dont allow words just specifics. 
        search_author = input("Please enter the Author your searching for: ")
        found = []
        for i in range (0,len(author)):
            if search_author.lower() == author[i].lower():
                found.append(i)
        if not found:
            print(f"Your search for {search_author} was NOT FOUND\n Make sure you correctly spelled the authors name and try again")
        else:#Found search for author
            print(f"{'LIB #':5}  {'TITLE ':35}  {'AUTHOR':20}  {'GENRE':20}  {'PAGES':5} {'STATUS'}")
            print("-------------------------------------------------------------------------------------------------------------------------------")
            for i in range(0,len(found)):
                print(f" {lib_num[found[i]]:5}  {title[found[i]]:35}  {author[found[i]]:20}  {genre[found[i]]:20}  {page_count[found[i]]:5} {status[found[i]]}")
    #quite literally the same as before except now we doing specific authors
        
    
    if search == "4":
        print("Search By Genre")
        #AGAIN ANOTHER SEQUENTIAL SEARCH
        #sequential search 
        search_title = input("Please enter the Genre Searching for: ")
        found = [] #Have to do this in order to allow for terms and phrases. 
        for i in range(0,len(title)):
            if search_title.lower() in title[i].lower():
                found.append(i)
        if not found:#AKA LIST IS EMPTY
            print(f"Sorry your search for {search_title} is not in our Library please try again")
        else:#FOUND YOUR SEARCH, 
            print(f"{'LIB #':5}  {'TITLE ':35}  {'AUTHOR':20}  {'GENRE':20}  {'PAGES':5} {'STATUS'}")
            print("-------------------------------------------------------------------------------------------------------------------------------")
            for i in range(0,len(found)):
                print(f" {lib_num[found[i]]:5}  {title[found[i]]:35}  {author[found[i]]:20}  {genre[found[i]]:20}  {page_count[found[i]]:5} {status[found[i]]}")
    if search == "5":
        print("Search by Library Num")
        search_num = input("Please Enter The Library Number Your searching For: ")
        #Okay First to do binary search we need to have a sorted list.
        for i in range(0, len(lib_num) - 1):#outter loop

            for index in range(0, len(lib_num) - 1):#inner loop

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing


                if(lib_num[index] > lib_num[index + 1]):
                    #if above is true, swap places!

        

                    swap(index, lib_num)
                    swap(index, title)
                    swap(index, author)
                    swap(index, genre)
                    swap(index, page_count)
                    swap(index, status)
        #Bubble sort that we did above now just for library numbers

        #Now Binary Search
        min = 0
        max = len(lib_num)
        mid = int((min + max) /2)
        
        while min < max and search_num != lib_num[mid]:
            if search_num <lib_num[mid]:
                #Everything afte5r mid point is not possible -------> change our max
                max= mid + 1
            else:
                #Everything before mid point isnt possible -------> Change our min
                min = mid + 1
            mid = int((min+max) / 2)
        if search_num == lib_num[mid]:
            print(f"{'LIB #':5}  {'TITLE ':35}  {'AUTHOR':20}  {'GENRE':20}  {'PAGES':5} {'STATUS'}")
            print("-------------------------------------------------------------------------------------------------------------------------------")
            print(f" {lib_num[mid]:5}  {title[mid]:35}  {author[mid]:20}  {genre[mid]:20}  {page_count[mid]:5} {status[mid]}")
        else:
            print(f"Sorry Your search for {search_num} was NOT found")
    if search == "6":
        print("6")
    if search == "7":
        print("7")
    if search == "8":
        answer = "n"

