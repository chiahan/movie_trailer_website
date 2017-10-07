# Movie Trailer Website
A website of my favorite movies' trailers, posters and ratings.

## Intallation
```
git clone https://github.com/chiahan/movie_trailer_website
```

## Execution
This website will be opened in the browser after executeing the `entertainment_center.py` (python version: 2.7)
```
python entertainment_center.py
```

## Document
- `entertainment_center.py`
The main function of this website. It creates Movie instances for my favorite movies and use **fresh_tomatoes.py** to generate the website.

- `media.py`
The Movie class, provides a way to store movie related information, is defined here.

- `imdb.py`
Get the imdb rating for movies using [theimdbapi](http://www.theimdbapi.org/) API

- `fresh_tomatoes.py`
Generate the html file and open it in the browser with the movie list.