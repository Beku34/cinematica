from rest_framework import serializers
from movie.models import Booking
from tickets.models import Ticket


def validate(self, data):
    seat = data['seat']
    show_time = data['show_time']

    if Booking.objects.filter(seat=seat, show_time=show_time).exists():
        raise serializers.ValidationError({"message": "Данное место забронировано!"})

    if Ticket.objects.filter(seat=seat, show_time=show_time).exists():
        raise serializers.ValidationError({"message": "Данное место уже куплено!"})