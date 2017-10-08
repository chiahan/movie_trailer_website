import webbrowser


class Movie():
    """This class provides a  way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

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
