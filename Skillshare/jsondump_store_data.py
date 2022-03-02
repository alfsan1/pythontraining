#25 febrero 2022
# usar json para guardar data
#open a file in write mode is "w" = with open(filename, "w")

import json 

phone_numbers = []
add_phone = int(input("Please write your phone number "))

while add_phone >= 0:
    for phone in phone_numbers:
        phone.append(add_phone) 
    else:
        break


 # Aquí creé un loop para que siga preguntando telefonos hasta que se use la letra q para quit y hacer que se graben más teléfonos.    
  
#quiero crear un loop para que los items se guarden en el json file. 

 #aqui es donde se guardan los datos en el json file, puede ser hasta el final del código.
filename = ("phone_number.json")

with open(filename, "w") as file_object:
    json.dump(str(add_phone), file_object )
