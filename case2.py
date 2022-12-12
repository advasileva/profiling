from sources import Cart1, Movie, Book

c1 = Cart1(Book("1984"))
c2 = c1.withMovie(Movie("Godfather"))
for i in range(100000000):
    c2.total()