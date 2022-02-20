### 24 enero 2022
### Default value
### Functions

## it means that when we create our function, we can but default value in some of the parameters. 

def book_descrption(author_name, type="non-fiction"):
    """to display books"""
    print("The author of this book is " + author_name.title() + ".")
    print("This is a  " + type.title() + " book.")

book_descrption("gabriel garcia")

### you can also change the order of the arguments since there are only two and one is left without argument
