# función para poder seleccionar que media se va a guardar
# primero tener el input en base a la selección de media
# validar error que se haya escrito bien el formato de la media, comparando con una lista
# en base a la media seleccionada, correr la función adecuada por tipo de media
# confirmar que se seleccionó la media correctamente 
# esta función sólo sirve para seleccionar la media. 

from user import User
from media_movie import Movie 
movie = Movie()

print("What type of media do you want to save? ")

while True: 
    media_select = input("\n press 'm' for Movie, y for youtube, p for podcast, s for series, and q for exit ")
    if media_select == "m":
        # activate F-movie function
        movie.describe_movie()
    elif media_select == "y":
        # activate youtube function
        pass
    elif media_select == "p" :
        #activate podcast function
        pass
    elif media_select == "s":
        #activate series function
        pass
    else:
        break  