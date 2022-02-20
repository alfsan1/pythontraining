### 27 enero 2022
## se va a crear un module o módulo que realmente es una función o programa dentro de un archivo .py que se importa en otro programa
## aqui en este archivo se va a crear una función y en otro archivo se va a importar y pasar argumentos. 

def books_available(*books):
    for book in books:
        book_in_stock =  "The following Book is available " + book.title()   
        print(book_in_stock)


## recordar siempre indentar dentro de una función todo y dentro de un loop todo lo que se ejecutará
## se guarda en una variable lo que se va a imprimir para luego pasarlo a print mas la variable. 
## esto por que Book se cicla cada vez que se usa. 

## creamos otra función para importar en otro archivo llamado "import more modules.py" y que haya mas funciones a importar

def book_description(author, genre, publisher):
    print("The author is " + author.title())
    print("This is a " + genre.title() + " book")
    print("It is published by " + publisher)

