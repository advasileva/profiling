from sources import Cart, Movie, Book

c = Cart(Book("1984"))
c.p = Movie("Godfather")
for i in range(100000000):
    c.total()