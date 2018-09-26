from django.contrib import admin
from django.urls import path
from backendapp.views import PlantsList, UserCreateAPIView, AccessoriesList,DetailViewPlant, DetailViewAccessories,Orderlist, CreateorderAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantslist/', PlantsList.as_view(), name='plantslist'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('accessorieslist/', AccessoriesList.as_view(), name='accessorieslist'),
    path('plant/<int:object_id>/', DetailViewPlant.as_view(), name='plant'),
    path('accessories/<int:object_id>/', DetailViewAccessories.as_view(), name='accessories'),
    path('orderlist/', Orderlist.as_view(), name='orderlist'),
    path('createorder/', CreateorderAPIView.as_view(), name='createorder'),



]
