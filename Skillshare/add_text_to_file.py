## how to add text to a new file from user input. 
## 18 febrero 2022


def Question():
    message = input("What are your favorite films? ")

    file_path = "favorite_films.txt"

    with open(file_path, "a") as file_object:
        file_object.write(message.title() + "\n")

    print("Thanks for adding " + message.title() + ", it has been registered")
Question()