from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import PlantsSerializer, UserCreateSerializer, AccessoriesSerializer, OrderSerializer
from .models import Plant, Accessory, Order
from rest_framework.views import APIView
from rest_framework.response import Response



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class PlantsList(ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantsSerializer

class AccessoriesList(ListAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessoriesSerializer

class Orderlist(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CreateorderAPIView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

     # def post(self, request, format=None):

     #     return Response()

class DetailViewPlant(RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class DetailViewAccessories(RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = AccessoriesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'