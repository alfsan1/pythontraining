### 26 enero 2022
### Usar while loop con una function


def get_formatted_name(first_name, last_name):
    """return a full name neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    first_name = input("\nWhat is your first name: ")
    if first_name == 'q':
        break
    last_name = input("What is your last name: ")
    if last_name == "q":
        break

## you can't concatenate a function to a string. 

## if you want to concatenate a function you have to put it inside a variable with its arguments:
    formatted_name = get_formatted_name(first_name, last_name)

    print("\nHi " + formatted_name + " welcome")

## todo debe de ir dentro del while loop o sea con el dent. 