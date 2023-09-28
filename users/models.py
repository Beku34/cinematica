from django.db import models
from users.managers import SuperUser
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models import Sum


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = SuperUser()

    def __str__(self):
        return self.first_name


class ClubCard(models.Model):
    balance = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def update_discount(self):
        total_spent = self.user.ticket_set.filter(is_paid=True).aggregate(Sum('price'))['price__sum']
        if total_spent is not None:
            if total_spent >= 1000:
                self.discount = 7
            elif total_spent >= 700:
                self.discount = 5
            elif total_spent >= 500:
                self.discount = 3
            else:
                self.discount = 0




    def __str__(self):
        return f"Club card for {self.user.email}"


class FeedBack(models.Model):
    RATE = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=RATE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
