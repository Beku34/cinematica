from rest_framework import serializers
from tickets.models import *
from movie.models import Booking
from tickets.utils import validate


class TicketSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

    def validate(self, data):
        return validate(self, data)

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'