#Duncan McKeith
#1-28-2025
#SE 126: Intermidiate Python
#W4D2 - Sequential search review + creating & writing to text files. 


#Program Prompt:In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.



#Variable Dictionary


#--------MAIN CODE BELOW-------------------



#---IMPORTS---------------------------------
import csv
#---FUNCTIONS-------------------------------

#--MAIN EXECUTING CODE------------------------------------------------------------------------------
dragons = []
riders = []
count = []
color1 = []
color2 = []

with open("Txt_Files/dragons.csv") as csvfile: 
    file= csv.reader(csvfile)
    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(int(rec[2]))
        color1.append(rec[3])
        if rec[2] == "2":
            
            color2.append(rec[4])
        else:
            color2.append('---')
#Disconnect now from the file

#process the lists to display

print(f"{'DRAGONS':15}  {'RIDERS':30} {'  #':4} {'COLOR1':8} {'COLOR2':8}")
print("----------------------------------------------------------------")
for i in range (0,len(dragons)):
    print(f"{dragons[i]:15}  {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]:8}")
print("-----------------------------------------------------------------")

#SEARCH FOR A SPECIFIC DRAGON

#Step 1 set-up and gain of search
found = "x"
search = input("Which dragon are you looking for?")

#step 2: perform the search
for i in range(0,len(dragons)):
    if search.lower() in dragons[i].lower():
        #hold onto the found location of our seached for value
        found = i

if found != "x":
    print(f"Your search for {search} was found")
    print(f"{dragons[found]:15}  {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]:8}")
else:
    print(f"Your search for {search} was NOT FOUND")


#Search for a color set
found = []
search = input("Enter the dragon color you are looking for: ")

for i in range (0,len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)

if not found:
    print(f"Your search for {search} was NOT FOUND")
else:
    print(f"You search for {search} WAS FOUND")
    for i in range(0,len(found)):
        print(f"{dragons[i]:15}  {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]:8}")
        
        
        
file = open('Txt_Files/targs', 'w')
file.write(f"{dragons[i]}, {riders[i]}\n")
file.close()