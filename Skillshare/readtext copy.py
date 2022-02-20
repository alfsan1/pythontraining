### Aprender a leer un dociumento en python con read


with open('movies.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())

