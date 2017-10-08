import urllib
import json

"""
This module provides methods to get the imdb information for movies.
"""


def get_rating(movie_title, movie_year):
    """
    Get the imdb rating for the movie

    Parameters
    ----------
    movie_title : string
        The title of the movie
    movie_year : string
        The year of first public screening

    Returns
    ----------
    int
        The imdb rating for the movie
    """
    imdb_movie_info = get_imdb_movie_info(movie_title, movie_year)

    return imdb_movie_info['rating']


def get_imdb_movie_info(movie_title, movie_year):
    """
    Get all imdb information for the movie

    Parameters
    ----------
    movie_title : string
        The title of the movie
    movie_year : string
        The year of first public screening

    Returns
    ----------
    dictionary
        The imdb information provided by http://www.theimdbapi.org/
    """
    imdb_api_url = ("http://www.theimdbapi.org/api/find/movie?"
                    "title={t}"
                    "&year={y}").format(t=movie_title, y=movie_year)
    urllib.URLopener.version = ("ozilla/5.0 (Windows NT 6.1) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/35.0.1916.153 "
                                "Safari/537.36 SE 2.X MetaSr 1.0")
    connection = urllib.urlopen(imdb_api_url)
    response = connection.read()
    connection.close()
    imdb_movie_info = json.loads(response)

    return imdb_movie_info[0]
