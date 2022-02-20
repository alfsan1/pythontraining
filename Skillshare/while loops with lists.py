### 21 enero 2022
## usar while loop y agregando data
### se usan 3 variables, una para los datos, otra para agarrar temporalmente los datos y la tercera se usa para recibir los datos

unconfirmed_users = ['alf', 'tony', 'jorge']

confirmed_users = []

## ahora tengo que pasar la lista con datos en un "while loop"

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying " + current_user)
    confirmed_users.append(current_user.title())

print(confirmed_users)

##  y podemos imprimir los nombres 1 x 1
print("\n Estos son los usuarios confirmados: ")
for item in confirmed_users:
    print(item.title())


### remove item from a list with the method remove, which is attached to the variable: 

books = ["tesla", "tesla", "batman", "attack on titan", "castlevania", "7 deadly", "tesla"]
print(books)

while "tesla" in books:
    books.remove("tesla")

print(books)