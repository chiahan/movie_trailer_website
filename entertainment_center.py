import media
import fresh_tomatoes

zootopia = media.Movie(
	"Zootopia",
	"A modern civilized world and it is entirely, animal.",
	"https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
	"https://www.youtube.com/watch?v=g9lmhBYB11U")

v = media.Movie(
	"V for Vendetta",
	"works to bring down an oppressive fascist government, profoundly affecting the people he encounters.",
	"https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
	"https://www.youtube.com/watch?v=qxyUl9M_7vc")

lalaland = media.Movie(
	"La La Land",
	"A jazz pianist who falls for an aspiring actress in Los Angeles.",
	"https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
	"https://www.youtube.com/watch?v=0pdqf4P9MB8")


her = media.Movie(
	"Her",
	"A lonely writer who develops an unlikely relationship with his newly purchased operating system that's designed to meet his every need.",
	"https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
	"https://www.youtube.com/watch?v=ne6p6MfLBxc")

kingsman = media.Movie(
	"Kingsman",
	"It follows the recruitment and training of a potential secret agent, Eggsy, into a secret spy organization.",
	"https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg",
	"https://www.youtube.com/watch?v=m4NCribDx4U")

the_intern = media.Movie(
	"The intern",
	"Ben's charm, wisdom and sense of humor help him develop a special bond and growing friendship with Jules.",
	"https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
	"https://www.youtube.com/watch?v=ZU3Xban0Y6A")

movies = [zootopia, v, lalaland, her, kingsman, the_intern]
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__) # class document
print(media.Movie.__module__) # file name
print(media.Movie.__name__) # class name

