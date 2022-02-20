#intro to dictionaries
#they're different than tuples or lists because they always come in pairs like word and definition. 

#create a dictionary of terms:

terms = {'variable': 'represents a value stored in memory', 'string':'a sequence of characters'}

#how to access something, first with the variable then with []
#print(terms['variable'])

#to check if a key is stored in a variable: 
if 'string' in terms:
    print(terms['string'])
else:
    print('key not in variable')




