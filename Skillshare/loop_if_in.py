### using loop "if and in"
##python, 16 enero 2022

users = ['alf', 'jaime', 'jorge', 'pepe', 'pedro', 'paco']

username = input("Ingresa tu usuario deseado ")
if username in users:
    print("Sorry, username already registered ")
else:
    print("Great, username Available ")


admins = ['alf', 'jaime', 'jorge', 'pepe', 'pedro', 'paco']

admin = input("Ingresa tu usuario Administrador ")
if admin not in admins:
    print("sorry, no tienes privilegios de administrador ")
else:
    print("Bienvenido administrador " + admin )
