from sources import Cart1, Movie1, Book1

c1 = Cart1(Book1("1984"))
c2 = c1.withMovie(Movie1("Godfather"))
for i in range(100000000):
    c2.total()