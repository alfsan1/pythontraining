### Aprender a leer un dociumento en python con read


## First we put the path inside a variable. I tried putting hte info in the same path but didn't work
## I used the complete path from a mac perspective
file_path = '/Users/alf/Documents/Python/movies.txt'

# WE are using open and the path to open the file, and we use file object, but i need to check if it a standarised argument or just any variable name
# After we create a variable that puts the .read method in the fileobject
#then we print that variable with strip to take out white spaces
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.strip())

## here is the same but we go line by line with a for loop. 
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

## take out an item from the list with pop method. 

print("\n -------------- \n")

## here we will go line by line and sorted them all, first we create the varible with the sort method
# then we create a for loop so that it prints each line but already sorted... I need to revise the logic on this to get a better understanding. 
sorted_list = lines.sort()
for line in lines:
    print(line.strip())


#how to take one line out
print("\n 2---------------- \n")
popped_movie = lines.pop()
# primero quitamos de lines la ultima movie

# de ahi creamos una for loop para impromor todo
for line in lines:
    print(line.strip())

print("\n 3************** \n")
print(popped_movie.capitalize())

