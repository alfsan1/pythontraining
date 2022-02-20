### 24 enero 2022
### return a value in a function

def formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

teacher = formatted_name("alfredo", "santos")

print(teacher)


### making arguments optional, adding an optional value to a function

def format_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

teacher = format_name("alfredo", "jaime", "santos")
print(teacher)

teacher = format_name("jorge", "velez")
print(teacher)


