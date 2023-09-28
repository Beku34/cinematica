from django.db import models
from movie.models import ShowTime, Seat
from users.models import User, ClubCard



class Ticket(models.Model):
    METHODS = [
        (1, "Bank-card"),
        (2, "Balance.kg"),
        (3, "Mbank"),
    ]
    type = models.ForeignKey("TicketType", on_delete=models.CASCADE, null=True)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0)
    payment_methods = models.IntegerField(choices=METHODS, default=1)
    club_card = models.ForeignKey(ClubCard, on_delete=models.CASCADE, null=True)
    is_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        price = (
            self.type.price +
            self.show_time.movie_format.price +
            self.seat.room.format.price
        )
        if (
            self.type.name == "Взрослый билет" or
            self.type.name == "Детский билет" or
            self.type.name == "Студенческий билет" and
            self.show_time.movie_format.name == "2-D" or
            self.show_time.movie_format.name == "3-D" and
            self.seat.room.format.name == "Большая комната" or
            self.seat.room.format.name == "Средняя комната" or
            self.seat.room.format.name == "маленькая комната" or
            self.seat.room.format.name == "Imax"
        ):
            if self.club_card.discount == 0:
                self.price = price
            else:
                price_with_discount = (
                    price / 100 * self.club_card.discount
                )
                self.price = (
                    price - price_with_discount
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.email


class TicketType(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f'Cart for {self.user}'






