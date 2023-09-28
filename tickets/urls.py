from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tickets.views import *


tickets_router = DefaultRouter()

tickets_router.register(r"ticket", TicketViewSet, basename="ticket")
tickets_router.register(r"ticket-type", TicketTypeViewSet, basename="ticket-type")
tickets_router.register(r"order", OrderViewSet, basename="order")
tickets_router.register(r"cart", CartViewSet, basename="cart")
