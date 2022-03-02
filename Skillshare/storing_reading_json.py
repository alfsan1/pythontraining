# 27 febrero 2022
# store and read data directly to and from a json file. 

import json

filename = "username.json"

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your username? ")
    with open(filename, "w") as file_object:
        json.dump(username, file_object)
        print("thank you for registering " + username)
else:
    print("welcome back " + username)
    
# we are combining two methods, first check if we've already registered
#second we add something into a json if there was no file created or empty. 
# refactoring is important > research more. 