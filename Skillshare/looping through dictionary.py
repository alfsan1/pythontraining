### 18 enero 2022
### curso skillshare de pythond
### looping through dictionary

birthday_months = {
    'tony' : 'august',
    'alfredo': 'september',
    'rami':'may',
    'alexa':'july',
    'topa':'june',
}

print(birthday_months)
for key, value in birthday_months.items():
    print("\n Nombre : " + key  )
    print("Mes: " + value)




### looping through key value pairs
book_1 = {
    'name' : 'elon musk',
    'author' : 'ashlee vance',
    'price' : 14.99,
    'publisher' : 'virgin books',
}
print(book_1)
for key, value in book_1.items():
    print("\nllave: " + key)
    print("valor: " + str(value))

print(book_1)
for key, value in book_1.items():
    print(key + ": " + str(value))
   


