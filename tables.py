import random

# this function will create 10 random table for our game
def random_Tables():
    tables = [] #tables list
    
    table_choices = ("evet","hayir") #choices
    for i in range(10): #loop
        table = {
        "bahis" : random.randint(2, 26)*100 ,
        "hizli" : random.choice(table_choices), #all here python generate random table 
        "teke_tek" : random.choice(table_choices),
        "rovans" : random.choice(table_choices),
        "Total" : None # for total, we will use bit flag option
    }
       
        table["Total"] = (table["rovans"] == "evet") * 4 + (table["teke_tek"] == "evet") * 2 + (table["hizli"] == "evet") * 1 # using bitflag method
        tables.append(table)

    return tables



"""
bit flag in Total:
rovans, teke_tek and the hizli are assig these values to a bit number

You can think like

rovans  teke_tek  hizli
 0        0        0

these 3 variables we assign like bit numbers. so we can filter our tables.

if user select them by "evet" then these bit numbers will be "1"
else these bit number will be "0"
because of that, we can define our filter method like that.

example:

rovans  teke_tek  hizli
 1        0        1

 that mean rovans = 'evet', teke_tek = 'hayir', hizli = 'evet'
 so if we convert these binary numbers to integer we will get: 4 + 0 + 1 = 5
Then we will assing the 'Total' to 5 for conditions above.



"""