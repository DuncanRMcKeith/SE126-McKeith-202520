#Duncan McKeith
#2-24-2025 
#SE 126: Intermidate Python
#W8 D1 - INTRO TO DICTIONARYS


#Dictionaries in Python are a collection set similar to associative arrays in JavaScript but also look similar to JS object builds. Most importantly, they store data in key and value pairs. They keys are referred to as properties and the values can be any data type. 


#-------IMPORTS-------------------------------------------------

#-------MAIN EXECUTING CODE--------------------------------------------------------------

#start by creating a populated dictionary
myCar = {
    #'key' : value, 
    "make": 'Ford',
    'model': 'SE Hatchback',
    'year': '2014',
    'name': 'Gwendoline',
    'color': 'black',
    #Keys cannot be repeated/NO DUPLICATES ALLOWED. 
    # 'color': 'red', = repeated keys will always use the most recent KEY VALUE. 
}


#display the entire dictionary -> 'myCar'
print(myCar)
#Display just the 'make' and 'model' values of the dictionary of 'myCar'
print(f"My car is a {myCar['make']} {myCar['model']}")
#keys cannot be repeated within a dictionary, but they can be reused across unique dictionary names: myCar vs yourCar
yourCar = {
    #'key' : value, 
    "make": 'GMC',
    'model': 'Canyon',
    'year': 2019, #Dont have to use the same data type within diciotnary 
    'name': 'Jolly',
    'color': 'black',
    #Keys cannot be repeated/NO DUPLICATES ALLOWED. 
    # 'color': 'red', = repeated keys will always use the most recent KEY VALUE.
    'friends': ["Ray",'Matt','Duncan'] 
}
print(f"Rob's Car is a {yourCar['make']} {yourCar['model']}")
print(f"{yourCar["friends"][2]}")

#processing through a dictionary and its key
for key in yourCar:
    print(f"{key.upper()} : {myCar[key]}")
    
#add a key and value to a pre-existing dictionary
yourCar["plate"] = "12345"
