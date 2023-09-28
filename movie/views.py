from rest_framework.viewsets import ModelViewSet
from movie.serializers import *
from movie.models import *


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaViewSet(ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomFormatViewSet(ModelViewSet):
    queryset = RoomFormat.objects.all()
    serializer_class = RoomFormatSerializer


class ShowTimeViewSet(ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializer


class MovieFormatViewSet(ModelViewSet):
    queryset = MovieFormat.objects.all()
    serializer_class = MovieFormatSerializer


class SeatViewSet(ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer