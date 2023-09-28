from django.db import models
from users.models import User


class Movie(models.Model):
    MOVIE_STATUS = [
        (1, "Ongoing"),
        (2, "Upcoming"),
        (3, "Exited"),
    ]
    name = models.CharField(max_length=255)
    descriptions = models.TextField(null=True)
    year = models.CharField(max_length=100, null=True)
    duratino = models.CharField(max_length=100, null=True)
    status = models.IntegerField(choices=MOVIE_STATUS, default=2)
    age_limit = models.CharField(max_length=50)
    start_movie = models.DateField()
    end_movie = models.DateField()
    image = models.ImageField(upload_to="movie", null=True)



    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    working_schedule = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    contacts = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    format = models.ForeignKey("RoomFormat", on_delete=models.SET_NULL, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RoomFormat(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Seat(models.Model):
    number_of_seat = models.CharField(max_length=50)
    number_of_row = models.CharField(max_length=50)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.number_of_seat}/{self.number_of_row}"


class ShowTime(models.Model):
    start_time = models.DateTimeField()
    movie_format = models.ForeignKey("MovieFormat", on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name


class MovieFormat(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Booking(models.Model):
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
