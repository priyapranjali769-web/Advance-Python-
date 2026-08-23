# Decorator
def border(func):
    def wrapper(self):
        print("-----------")
        func(self)
        print("-----------")
    return wrapper


class Movie:

    # Constructor
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    # Class method
    @classmethod
    def category_info(cls):
        print("Movie Categories: Hit, Average, Flop")

    # Decorated method
    @border
    def show(self):
        if self.rating >= 8:
            category = "Hit"
        elif self.rating >= 5:
            category = "Average"
        else:
            category = "Flop"

        print("Movie Name:", self.movie_name)
        print("Rating:", self.rating)
        print("Ticket Price:", self.ticket_price)
        print("Category:", category)

    # Magic method
    def __str__(self):
        return self.movie_name


# Main Program
Movie.category_info()

m = Movie("Avengers", 9.0, 250)

m.show()

print(m)