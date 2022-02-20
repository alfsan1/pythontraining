### 21 enero 2022
### flags que son? las flags hace que el if statement sea simple y se usan booleanos. 

prompt = '\n Enter the right answer to continue'
prompt = 'what is 9 x 7? '

## the flag is set to true

active = True
while active: 
    message = input(prompt)
    if message == str(9*7):
        active = False
        print('right answer mate')
    else:
        print('your answer ' + message + ' is wrong')


## le agregué de mi cosecha y convertí a str la multiplicación en la línea 12 para no tener que buscar la respuesta. 