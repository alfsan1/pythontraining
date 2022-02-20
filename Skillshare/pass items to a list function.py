## 26 enero 2022
### Como pasar una items a una lista mediante función

def books_available(books):
    """show list of all available books"""
    for book in books:
        books_in_store = "The following books are available: " + book.title()
        print(books_in_store)

book_list = ['the everything store', 'dune', 'jurassic park', 'the fountainhead']

books_available(book_list)