### 26 enero 2022
### modificar una lista desde una function

# se va a crear un código para poder documentar a pasajeros en un aeropuerto
# primero se crea una función para listar los pasajeros que no han documentado
# se crea una segunda función para documentar los pasajeros
# se ejecuta la función para listar los pasajeros que se están documentando

def passengers(not_checked, checked):
    while not_checked:
        current_passanger = not_checked.pop()
        print('checking in ' + current_passanger)
        checked.append(current_passanger)

def show_checked(checked):
    print('The following passengers have been checked in')
    for passengers in checked:
        print(passengers.title())

not_checked = ['alfredo santos', 'sady garzon', 'lili ruiz']
checked = []

passengers(not_checked, checked)

show_checked(checked)