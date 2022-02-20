### 27 enero 2022
## se va a crear un module o módulo que realmente es una función o programa dentro de un archivo .py que se importa en otro programa
## aqui en este archivo se va a crear una función y en otro archivo se va a importar y pasar argumentos. 

def books_available(books):
    for book in books:
        book_in_stock =  "The following Book is available " + book   
        print(book_in_stock)