# сюда пишем домены /index, /dwd и так далее
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.


class RoomViev(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
