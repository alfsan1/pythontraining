### 26 enero 2022
### return a dictionary in a function. 

## vamos a crear una función con argumentos para crear un diccionario adentro

def build_book(name, author, publisher):
    book = {'name': name, 'author': author, 'publisher': publisher}
    return book
# las funciones deben llevar return siempre

my_book = build_book('elon musk', 'ashlee vance', 'pinguin house')

print(my_book)

print(my_book['author'])

print(my_book['publisher'])

