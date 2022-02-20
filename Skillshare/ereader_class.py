### 1ro febrero 2022
### crear una clase de ereader con todos sus argumentos

class Ereader():

    def __init__(self, make, model, backlight, battery,  screen):
        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen = screen
        self.library_count = 0

    def get_ereader_name(self):
        long_name = self.make + "-" + self.model + "- " + self.backlight + "- " + str(self.battery) + " - " + self.screen
        return long_name.title() 

       # print("this ereader is " + make.title() + " and the model " + model + " and it has " + backlight + " and a " + str(battery) + " battery with a screen resolution " + screen)
    def read_library_count(self):
        print("you have " + str(self.library_count) + " books in your ereader")

my_new_ereader = Ereader("amazon", "paperwhite", "backlight", 2000, "480 dpi")
print(my_new_ereader.get_ereader_name())
print(my_new_ereader.read_library_count())

## we can change the value in an argument like library count this way
my_new_ereader.library_count = 36
my_new_ereader.read_library_count()





