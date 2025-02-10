##Duncan McKeith
#2-10-2025 
#SE 126: Intermidate Python
#WEEK 6 DAY 1 DEMO: Binary Search


import csv

lib_num = []
title = []
author = []
genre = []
pages = []

with open("Txt_Files/library_books.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file: 
        lib_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pages.append(rec[4])

print(f"{'Lib #':5}   {'Title':25}   {'Author':15}   {'Genre':20}   {'Pages':5}")
print("--------------------------------------------------------------------------------------------")
for i in range(0,len(lib_num)):
    print(f"{lib_num[i]:5}   {title[i]:25}   {author[i]:15}   {genre[i]:20}   {pages[i]:5}")
    
#Sequential Search: Allow a user to search for a specific title, 
#title[] is NOT ordered

found=[]
search_num = input("Which libraty num, are you looking for?")
seq_count = 0
for i in range(0,len(lib_num)):
    seq_count +=1
    if search_num in lib_num[i]:
        found.append(i)
        
print(f"search iterations:{seq_count}")
if not found:
    print(f"Sorry, your search for {search_num} was NOT found")
else:
    print(f"Your search for {search_num} was FOUND!")
    print(f"{'Lib #':5}   {'Title':25}   {'Author':15}   {'Genre':20}   {'Pages':5}")
    print("--------------------------------------------------------------------------------------------")
    for i in range(0,len(found)):
            print(f"{lib_num[found[i]]:5}   {title[found[i]]:25}   {author[found[i]]:15}   {genre[found[i]]:20}   {pages[found[i]]:5}")
    print("--------------------------------------------------------------------------------------------")
    
    
    
#BINARY SEARCH: must be performed upon ORDERED LISTS (lib_num)

min = 0
max =len(lib_num) - 1
mid = int((min + max) / 2)

bin_count = 0

while min < max and search_num != lib_num[mid]:
    #min < max ----> list has not been exhausted of potential values yet
    #search_num != library_nums[mid] ----> what we are looking for is not in the mid position. 
    
    
    if search_num < lib_num[mid]:
        #Everything after mid point is not possible ------> Change our max
        max = mid - 1 
    else:
        #Everything before pid point isnt possible ------> change our min
        min = mid + 1
    mid = int((min + max)/2)
    bin_count += 1
    
if search_num == lib_num[mid]:
    print(f"Search Iterations{bin_count}")
    print(f"Your search for {search_num} was FOUND!")
    print(f"{'Lib #':5}   {'Title':25}   {'Author':15}   {'Genre':20}   {'Pages':5}")
    print("--------------------------------------------------------------------------------------------")
    print(f"{lib_num[mid]:5}   {title[mid]:25}   {author[mid]:15}   {genre[mid]:20}   {pages[mid]:5}")
    print("-------------------------------------------------------------------------------------------")

else:
    print(f"Sorry your search for {search_num} was NOT found")