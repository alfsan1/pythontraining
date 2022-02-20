numbers = []
for value in range(1,10):
    numbers.append(value)
    print(numbers)


print(numbers[:3])
print(numbers[2:4])
print(numbers[-3:])
print(numbers[:-3])


#loop through slicing

names = ['maria', 'dali', 'nancy', 'sady', 'lore']
print("here are the names of the last 3")
for name in names[:3]:
    print(name.title())


#copy a list and also parts of a list. you just create another variable and add the original content of the 1st variable. 

names = ['maria', 'dali', 'nancy', 'sady', 'lore']
copy_list = names[:]

print(copy_list)

slice_copy_list = names[2:]
print(slice_copy_list)
