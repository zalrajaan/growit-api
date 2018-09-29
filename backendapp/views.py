from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import PlantsSerializer, UserCreateSerializer, AccessoriesSerializer, OrderSerializer
from .models import Plant, Accessory, Order, Product, ProductItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class PlantsList(ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantsSerializer

class AccessoriesList(ListAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessoriesSerializer

class Orderlist(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Order.objects.filer(request)
        json_query = OrderSerializer(queryset, many=True).data
        return Response(json_query)

class CreateorderAPIView(APIView):
    def post(self, request, *args, **kwargs):
        cart = request.data["items"]
        order_obj = Order.objects.create(user=request.user)
        print (request)
        for order in cart:
            print (order)
            product_id = order.get("productID")
            quantity = order.get("quantity")
            product_obj = Product.objects.get(id=product_id)
            product_item = ProductItem.objects.create(
                quantity=quantity, order=order_obj, product=product_obj)
        return Response(status=status.HTTP_201_CREATED)

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