from rest_framework.viewsets import ModelViewSet
from tickets.serializers import *
from tickets.models import *



class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        ticket = serializer.save()

        cart = Cart.objects.filter(user=ticket.user).first()

        cart.total_price += ticket.price

        cart.save()




class TicketTypeViewSet(ModelViewSet):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()

        tickets = Ticket.objects.filter(user=order.user, is_paid=False)

        clubcard = ClubCard.objects.get(user=order.user)

        for i in tickets:
            i.is_paid = True
            i.save()

        if clubcard:
            clubcard.update_discount()

        cart = Cart.objects.get(user=order.user)
        total_price = cart.total_price
        clubcard.balance += total_price*3//100
        clubcard.save()
        cart.total_price = 0
        cart.save()


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
