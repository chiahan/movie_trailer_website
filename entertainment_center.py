import media
import imdb
import fresh_tomatoes

rating = imdb.get_rating("Zootopia", "2016")
zootopia = media.Movie(
    "Zootopia",
    "2016",
    "A modern civilized world and it is entirely, animal.",
    rating,
    "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
    "https://www.youtube.com/watch?v=g9lmhBYB11U")

rating = imdb.get_rating("V for Vendetta", "2005")
v = media.Movie(
    "V for Vendetta",
    "2005",
    "works to bring down an oppressive fascist government, "
    "profoundly affecting the people he encounters.",
    rating,
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
    "https://www.youtube.com/watch?v=qxyUl9M_7vc")

rating = imdb.get_rating("La La Land", "2016")
lalaland = media.Movie(
    "La La Land",
    "2016",
    "A jazz pianist who falls for an aspiring actress in Los Angeles.",
    rating,
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")

rating = imdb.get_rating("Her", "2013")
her = media.Movie(
    "Her",
    "2013",
    "A lonely writer who develops an unlikely relationship "
    "with his newly purchased operating system "
    "that's designed to meet his every need.",
    rating,
    "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
    "https://www.youtube.com/watch?v=ne6p6MfLBxc")

rating = imdb.get_rating("Kingsman", "2014")
kingsman = media.Movie(
    "Kingsman",
    "2014",
    "It follows the recruitment and training of a potential secret agent, "
    "Eggsy, into a secret spy organization.",
    rating,
    "https://upload.wikimedia.org/wikipedia/en/8/8b/"
    "Kingsman_The_Secret_Service_poster.jpg",
    "https://www.youtube.com/watch?v=m4NCribDx4U")

rating = imdb.get_rating("The intern", "2015")
the_intern = media.Movie(
    "The intern",
    "2015",
    "Ben's charm, wisdom and sense of humor help him develop a special bond "
    "and growing friendship with Jules.",
    rating,
    "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
    "https://www.youtube.com/watch?v=ZU3Xban0Y6A")

movies = [zootopia, v, lalaland, her, kingsman, the_intern]
fresh_tomatoes.open_movies_page(movies)
