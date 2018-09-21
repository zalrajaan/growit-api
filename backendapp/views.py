from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import PlantsSerializer, UserCreateSerializer
from .models import Plant



class PlantsList(ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantsSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer