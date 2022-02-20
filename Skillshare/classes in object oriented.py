### 28 enero 2022
# crear book class, que es una clase, siempre se empieza la clase con una mayúscula al nombre. para diferenciarse 
# a function that is part of a class is called a Method. 
# the __init__ is a method exclusive of python, and not my code, it has two underscores to differentiate it. 
# the first attribute in the parenthesis after init inside the method (function) is always SELF. 
# the self method has to come first before the other parameters , but why?

class Book():
    def __init__(self, name, price, publisher):
        self.name = name 
        self.price = price
        self.publisher = publisher
# we are creating a variable that contains the attributes like self.name, we create the variable name to be used later and that means it will call the attribute of the function
#the book class will have other three method defined, that means three other functions
    def hardback(self):
        print(self.name.title() + " is a hardback book")

    def softback(self):
        print(self.name.title() + " is a Softback book")

    def ebook(self):
        print(self.name.title() + " is an ebook")

# the functions inside a class define the functions or usability of that class, of that item, 
# like a book, has a cover, a back, pages, the pages turn,etc. 

my_book = Book('Elon Musk', 399, 'random house')

print("I'm Currently readling " + my_book.name.title() + " published by " + my_book.publisher.title())

my_book.softback()

### you can create new instances by creating new variable, in this case second_book and has new arguments that are later call with the hardback method (function)

second_book = Book('everything store', 499, 'Pinguin house')

second_book.hardback()