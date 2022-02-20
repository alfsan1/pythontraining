## use of while loops
## 20 enero 2022

from ntpath import join


current_number = 1

while current_number <= 10:
    print(current_number)
    current_number += 1


## Keep a program running example
## se crea una variable con el texto y se le agrega otra linea de texto, de ahi
## se crea una variable vacía que es donde se recibirá el input. 
## el while loop nos dice hasta cuando va a parar el programa y de ahi se dice que se hará mientras esté corriendo
## a la variable vacía se le asigna el input que se recibirá y de ahi se im`rime lo que se recibió
prompt = "\n To end this program press the letter 'q' "
prompt += "Enter your name: "

message = ""
while message != 'q':
    message = input(prompt)
    print(message)


