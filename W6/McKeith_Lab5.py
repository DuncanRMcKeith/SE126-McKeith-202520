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
                    swap(index, )
                    #swap all other values
                  

    
        #PRINT STATMENT FOR 
        print(f"{'LIB #':5}  {'TITLE ':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5} {'STATUS'}")
        print("-------------------------------------------------")
        for i in range(0,len(title)):
             print(print(f" {lib_num[i]:5}  {title[i]:25}  {author[i]:15}  {genre[i]:20}  {page_count[i]:5} {status[i]}"))
    if search == "2":
        print ("2")
    if search == "3":
        print ("3")
    if search == "4":
        print("4")
    if search == "5":
        print("5")
    if search == "6":
        print("6")
    if search == "7":
        print("7")
    if search == "8":
        answer = "n"
