# We'll open a file that doesnt exist, it will mark error and we need error handling exceptions
# 20 febrero 2022

filename = "alf.txt"
# el archivo alfredo no existe

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    error_message = "The file you're looking for doesn't exist"
    print(error_message)
     
