class Book1:
    def __init__(self, title):
        self.title = title
        self.curr_price = 40
    
    def price(self):
        return self.curr_price