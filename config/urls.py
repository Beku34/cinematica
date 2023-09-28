from django.contrib import admin
from django.urls import path, include
from patches import routers
from movie.urls import movie_router
from tickets.urls import tickets_router
router = routers.DefaultRouter()
router.extend(movie_router)
router.extend(tickets_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('', include(router.urls)),
]