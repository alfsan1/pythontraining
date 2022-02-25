#25 febrero 2022
# usar json para guardar data
#open a file in write mode is "w" = with open(filename, "w")

import json 

phone_numbers = []
phone_number = int(input("Please write your phonenumber "))

#quiero crear un loop para que los items se guarden en el json file. 
for item in phone_numbers:
    phone_numbers.append(item)


filename = ("phone_number.json")

with open(filename, "w") as file_object:
    json.dump(str(phone_numbers), file_object )
    
