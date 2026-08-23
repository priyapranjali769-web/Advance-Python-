class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def display(self):
        if self.rating >= 8:
            category = "Hit"
        elif self.rating >= 5:
            category = "Average"
        else:
            category = "Flop"

        print(f"Movie: {self.movie_name}")
        print(f"Rating: {self.rating}")
        print(f"Ticket Price: ₹{self.ticket_price}")
        print(f"Category: {category}")


class Cinema:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Movie '{movie.movie_name}' added successfully.")

    def display_movies(self):
        print("\nCinema Movie Collection:")
        for movie in self.movies:
            movie.display()


# Main Program
cinema = Cinema("PVR Cinema")

cinema.add_movie(Movie("Avengers", 9.0, 250))
cinema.add_movie(Movie("Dunki", 7.0, 200))
cinema.add_movie(Movie("Example Movie", 4.0, 150))

cinema.display_movies()