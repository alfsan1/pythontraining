## 26 enero 2022
## listar los extras que requiere un pasajero al viajar

def passenger(seat, *requests):
    print("Seat number assigned " + str(seat) + " with the following requests: ")
    for request in requests:
        print(request)

passenger(34, 'aile seat', 'vegan menu', 'econo plus')

