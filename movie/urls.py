from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movie.views import *


movie_router = DefaultRouter()

movie_router.register(r"movie", MovieViewSet, basename="movie")
movie_router.register(r"cinema", CinemaViewSet, basename="cinema")
movie_router.register(r"show-time", ShowTimeViewSet, basename="show-time")
movie_router.register(r"movie-format", MovieFormatViewSet, basename="movie-format")
movie_router.register(r"room", RoomViewSet, basename="room")
movie_router.register(r"room-format", RoomFormatViewSet, basename="room-format")
movie_router.register(r"booking", BookingViewSet, basename="booking")
movie_router.register(r"seat", SeatViewSet, basename="seat")

urlpatterns = [
    path('', include)

]

urlpatterns = movie_router.urls