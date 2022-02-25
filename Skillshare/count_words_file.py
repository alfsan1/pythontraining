## 25 febrero 2022
## Primero marcar errores en caso que no se pueda encontrar el archivo
# Si se encuentra el archivo, contar las palabras que hay usando métodos split y len

#filename = "movies.txt"
#try:
#    with open(filename) as file_object:
#        contents = file_object.read()
#except FileNotFoundError:
#    message = "Sorry, the file " + filename + " Hasn't been found in the server"
#else:
#    words = contents.split()
#    count_words = len(words)
#    print("the requested file has " + str(count_words) + " words")
    
 
 #now we can create a function with the upper code so it can read any text and see if it's there.
 # maybe i can create an input that will search for filename and then sort out all the words in the file, and this could be the basis for howlong to read this. 
 

def word_count(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
            message = "Sorry, the file " + filename + " Hasn't been found in the server"
    else:
            words = contents.split()
            count_words = len(words)
            print("the requested file has " + str(count_words) + " words ")
            
filenames = ["movies.txt" , "weekend.txt" , "programming.txt" , "favorite_films.txt" ]
#for filename in filenames:
 #   word_count(filename)
    
choose_film = input("escribe el nombre del archivo ")

for filename in filenames:
    if choose_film == filename:
        word_count(filename)
    


    