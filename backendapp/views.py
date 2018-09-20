from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import PlantsSerializer
from .models import Plant


class PlantsList(ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantsSerializer