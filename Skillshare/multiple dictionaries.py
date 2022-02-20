### crear listas con dictionar adentro, para productos. 
# Crear varios productos dentro y cambiar algunos de precio
# 20 enero 2022 

stock_items = []

for blue_pen in range(0,50):
    new_blue_pens = {
        'color' : 'blue',
        'type':'ballpoint',
        'price':'1.99'
            }
    stock_items.append(new_blue_pens)

print(stock_items)
print("break ")

for blue_pen in stock_items[0:5]:
    if blue_pen['price'] == '1.99':
        blue_pen['price'] = '0.99'

for blue_pen in stock_items[0:1]:
    print(blue_pen)

## why do i have to do a loop inside stock items in order to print blue_pen??