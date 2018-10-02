from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from .serializers import PlantsSerializer, UserCreateSerializer, AccessoriesSerializer, OrderSerializer, ProfilSerializer, CategorySerializer, ProfilDetailSerializer, TrackingHistorySerializer, PlantHeightSerializer
from .models import Plant, Accessory, Order, Product, ProductItem, Profile, Category, TrackingHistory, PlantHeight
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

class ProfileCreateAPIView(CreateAPIView):
    serializer_class = ProfilSerializer

class ProfileDetailAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilDetailSerializer
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'

class ProfileUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilSerializer
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class PlantsList(ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantsSerializer

class AccessoriesList(ListAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessoriesSerializer

class CustomerOrder(APIView):
    def get(self, request, user_id, *args, **kwargs):
        queryset = Order.objects.filter(user=request.user)
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
            product_obj.quantity = product_obj.quantity - int(quantity)
            product_obj.save()
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

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TrackingHistoryCreateView(CreateAPIView):
    serializer_class = TrackingHistorySerializer

class TrackingHistoryListView(APIView):
    def get(self, request, *args, user_id, **kwargs):
        queryset = TrackingHistory.objects.filter(user=request.user)
        json_query = TrackingHistorySerializer(queryset, many=True).data
        return Response(json_query)

class TrackingHistoryUpdateView(RetrieveUpdateAPIView):
    queryset = TrackingHistory.objects.all()
    serializer_class = TrackingHistorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class PlantHeightCreateView(CreateAPIView):
    serializer_class = PlantHeightSerializer

# class PlantHeightListView(APIView):
#     def get(self, request, *args, track_id, **kwargs):
#         queryset = PlantHeight.objects.filter(track=request.track)
#         json_query = PlantHeightSerializer(queryset, many=True).data
#         return Response(json_query)

class PlantHeightUpdateView(RetrieveUpdateAPIView):
    queryset = PlantHeight.objects.all()
    serializer_class = PlantHeightSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
