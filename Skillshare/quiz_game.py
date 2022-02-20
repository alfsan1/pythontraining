## Create mini game

from signal import siginterrupt


print("Bienvenid@ al quiz de Capitales")

play = input("¿deseas jugar? ")
if play.lower() != "si":
    quit()
else:
    print("Vamos a Empezar el Juego ")
score = 0

answer = input("Cuál es la capital de Coahuila? ")
if answer.lower() == "torreon":
    print("Correcto!")
    score += 1
else:
    print("Respuesta Incorrecta")

answer = input("Cuál es la capital de Chiapas? ")
if answer.lower() == "tuxtla":
    print("Correcto!")
    score += 1
else:
    print("Respuesta Incorrecta")

answer = input("Cuál es la capital de Sinaloa? ")
if answer.lower() == "culiacan":
    print("Correcto!")
    score += 1
else:
    print("Respuesta Incorrecta")

answer = input("Cuál es la capital de Sonora? ")
if answer.lower() == "hermosillo":
    print("Correcto!")
    score += 1
else:
    print("Respuesta Incorrecta")

answer = input("Cuál es la capital de Tamapulipas? ")
if answer.lower() == "ciudad victoria":
    print("Correcto!")
    score += 1
else:
    print("Respuesta Incorrecta")

print("El Juego ha terminado")
print("Tu resultado es de " + str(score) + " puntos, felicidades")
print("Tu llevas " + str((score / 5) * 100) + "%" )

