## how to add input to a dictionary
### 22 enero 2022

## create an empty dictionary

from audioop import add
from turtle import clear


properties = {}

## set a flag to indicate we're taking applications
## now ask for users for name and address in a loop
rental_open = True

while rental_open:
    user = input("Please give your name ")
    address = input("plase give your address ")
    properties[user] = address
    repeat = input("Do you want to list more properties? ")
    if repeat != "no":
        rental_open: False


print("\nAdding property to rent") 
for user, address in properties.items():
    print("the person " + user + "has a property in " + address + "to rent")

### clase 65 de skillshare > no se pudo lograr que parara el ciclo con "false", pero el texto es igual que el del profe, falta copiarlo igual. 