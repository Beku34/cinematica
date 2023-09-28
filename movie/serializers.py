from rest_framework import serializers
from movie.models import *
from tickets.utils import validate
import datetime
import pytz



utc = pytz.UTC


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


    def get_status(self, obj):
        now = datetime.date.today()
        if obj.start_movie <= now <= obj.end_movie:
            obj.status = "ongoing"
            obj.save()
        if now <= obj.start_movie:
            obj.status = 2
            obj.save()
        if now >= obj.end_movie:
            obj.status = 3
            obj.save()

        return obj.status


    def validate(self, data):
        start = data['start_movie']
        end = data['end_movie']

        if start >= end:
            raise serializers.ValidationError("Beksultan")

        return data




class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'



class RoomFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFormat
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = '__all__'


class MovieFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        return validate(self, data)