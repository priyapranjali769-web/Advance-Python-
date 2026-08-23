from abc import ABC, abstractmethod


# Abstract Class
class Movie(ABC):

    @abstractmethod
    def category(self, rating):
        pass


# Child Class 1
class HitMovie(Movie):

    def category(self, rating):
        if rating >= 8:
            print("Movie Category: Hit")
        else:
            print("Rating is not high enough for Hit category")


# Child Class 2
class AverageMovie(Movie):

    def category(self, rating):
        if 5 <= rating < 8:
            print("Movie Category: Average")
        else:
            print("Rating is not in Average category")


# Child Class 3
class FlopMovie(Movie):

    def category(self, rating):
        if rating < 5:
            print("Movie Category: Flop")
        else:
            print("Rating is not in Flop category")


# Main Program
m1 = HitMovie()
m1.category(9)

m2 = AverageMovie()
m2.category(7)

m3 = FlopMovie()
m3.category(4)