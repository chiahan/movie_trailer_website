import webbrowser


class Movie():
    """
    This class provides a  way to store movie related information.

    Attributes:
        movie_title: The title of the movie
        movie_year: The year of first public screening
        movie_storyline: The movie storyline
        movie_rating: The imdb rating for the movie
        poster_image_url: The wiki image url for the movie poster
        trailer_youtube_url: The youtube url for the movie trailer
    """

    def __init__(self, movie_title, movie_year, movie_storyline, movie_rating,
                 poster_image, trailer_youtube):
        self.movie_title = movie_title
        self.movie_year = movie_year
        self.movie_storyline = movie_storyline
        self.movie_rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
