import urllib
import json

def get_rating(movie_title, movie_year):
	imdb_movie_info = get_imdb_movie_info(movie_title, movie_year)
	
	return imdb_movie_info[0]['rating']

def get_imdb_movie_info(movie_title, movie_year):
	imdb_api_url = "http://www.theimdbapi.org/api/find/movie?title="+movie_title+"&year="+movie_year
	urllib.URLopener.version = "ozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0"
	connection = urllib.urlopen(imdb_api_url)
	response = connection.read()
	connection.close()
	imdb_movie_info = json.loads(response)

	return imdb_movie_info