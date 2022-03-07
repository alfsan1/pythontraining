


class Movie():
    def __init__(self, title, platform, date, rating, comments):
        self.title = title
        self.platform = platform
        self.date = date
        self.rating = rating
        self.comments = comments

movie_description = []
        
    def describe_movie(title,platform, date, rating, comments):
        print("Great!, let's save your movie ")
        title = input("What's the movie title?: ")
        platform = input("Where did you watch the movie?: ")
        date = input("when did you watch the movie?: ")
        rating = input("How many stars do you give the movie from 1 to 5: ")
        comments = input("What did you think about the movie?: ")

        movie_description.append(title)
        movie_description.append(platform)
        movie_description.append(date)
        movie_description.append(rating)
        movie_description.append(comments)

