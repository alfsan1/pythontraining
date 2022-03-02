## vamos a contar las palabras en un archivo, como lo hace word. ver cuantas palabras llevamos por ejemplo
# 20 febrero 2022

from fileinput import filename


filename = "movies.txt"

try: 
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("your file " + filename + " hasn't been found")
else:
    words = contents.split()
    word_count = len(words)
    print("the file " + filename + " has " + str(word_count)+ " words.")
