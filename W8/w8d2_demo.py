#Duncan McKeith
#Dictionary and text file data




#Imports
import csv

#Main Executing code

with open('Txt_Files/dictionary_file.csv')as csvfile:
    file = csv.reader(csvfile)
    library = {
        #Indexes are STRINGS set by the developer
        #key : value pair. 
        '1230': 'Red Rising',
        '1231': 'The Little Prince'
    }
    
    for rec in file:
        #add each records data as a new key + value pair from the text file
        #key ---> rec[0] ; value -----> rec[1]
        library.update({rec[0] : rec[1]})
        
        
#Disconnect from file.
print(F"{'KEY':6}\t{'TITLE'}")
print("-"*50)
for key in library:
    #for every key(and value): pair found within the 'library' dictionary
    print(f"{key:6}\t{library[key]}")
print("-"*50)


#SEQUENTIAL SEARCH FOR A TITLE
search = input({"Enter the TITLE you are looking for: "})
found = 0 #Dictionarys are strings so using a int is fine

for key in library:
    
    if search.lower() == library[key].lower():
        found = key
    
if found != 0:
    print(f"Key:{found}\tTitle:{library[found]}")
else:
    print(f"\n Your search for {search} came up EMPTY!")


if type(library) is list:
    print("'library' is a Dictionary")
#Binary Sort for LIBRARY NUMBER(dictonary KEYS)
#in order to binary search a set of keys you must FIRST ...
id_list = []

