### 27 enero 2022
### importar más de una función dentro de un módulo, archivo .py

from module_example1 import books_available as ba, book_description as bd


print("first function")
ba("elon musk", "land before time", "marley and me")

print("Second function")
bd("ashlee vance", "non-fiction", "random house")

### al importar las funciones se les puede dar un alias,para hacerlo mas corto o evitar confusión con as
## ejemplo from module_example1 import books_available as ba