from django.urls import path, include
from .views import RoomViev

urlpatterns = [
    path('room', RoomViev.as_view())
]