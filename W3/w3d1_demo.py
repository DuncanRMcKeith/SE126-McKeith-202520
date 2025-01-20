#This file uses: simple.csv
#--IMPORTS---------------------------------------------------------------
import csv

#--MAIN EXECUTING CODE---------------------------------------------------
#create empty lists
name = []
number = []
color = []

#--connected to file----------------------------
with open("Txt_Files\simple.csv") as csvfile:
    file = csv.reader(csvfile)
    for record in file:

        name.append(record[0]) #name field
        number.append(int(record[1])) #number field
        color.append(record[2]) #color field

#--disconnected from file-------------------------
print(f"{'NAME':10} {'NUM'} {'COLOR'}\n-------------------------------------")

#process lists for printing
for index in range(0, len(name)):
    print(f"{name[index]:10} {number[index]:3} {color[index].title()}")
print("---------------------------------------")
print(f"\nTOTAL RECORDS: {len(name)}\n")