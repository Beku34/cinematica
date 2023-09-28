from django.contrib import admin
from movie.models import *

admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Room)
admin.site.register(RoomFormat)
admin.site.register(ShowTime)
admin.site.register(MovieFormat)


