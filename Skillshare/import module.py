##  27 enero 2022
### aqui vamos a importar un modulo
## este archivo va ligado a otro archivo llamado module_example1.py pero aqui se pone sin la extensión


import module_example1 

module_example1.books_available("Los guardianes", "la magia", "the everything store")

## para activarlo se copia el nombre del archivo, seguido del punto, seguido de la función del módulo importado y de ahí se pasan los argumentos.
## esto se importa así cuando el módulo ( el otro archivo .py con funciones) sólo tiene una función
## cambia cuando hay dos functions o más en el módulo a importar. 
