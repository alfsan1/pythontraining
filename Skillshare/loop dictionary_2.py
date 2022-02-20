### looping through key of dictionary
### 20 enero 2022

birthday_months = {
    'tony' : 'november',
    'alf' : 'september',
    'topa' : 'june',
    'rami' : 'may',
}

#print(birthday_months)

for item in birthday_months.keys():
    print(item.title())

for item in birthday_months.values():
    print('Su cumpleaños es en: ' + item.title())