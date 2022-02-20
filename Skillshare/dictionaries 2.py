## 18 enero 2022
## crear diccionarios vacios

terms = {}

terms['variable'] = 'represents a value stored in the computer inside the word'
terms['integer'] = 'is a whole number'

print(terms['variable'])

### GET method for python

print(terms.get('variable'))
print(terms.get('float', 'not in the dictionary'))

print(terms)

#### edit a dictionary

terms['integer'] = ' a very large number'

print(terms['integer'])


### delete

del terms['integer']
print(terms)


