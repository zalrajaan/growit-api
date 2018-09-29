from django.contrib import admin
from django.urls import path
from backendapp.views import PlantsList, UserCreateAPIView, AccessoriesList,DetailViewPlant, DetailViewAccessories,Orderlist, CreateorderAPIView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
#Users
	path('login/', obtain_jwt_token, name='login'),
    path('admin/', admin.site.urls),
#ListView
    path('plantslist/', PlantsList.as_view(), name='plantslist'),
    path('accessorieslist/', AccessoriesList.as_view(), name='accessorieslist'),
    path('orderlist/', Orderlist.as_view(), name='orderlist'),
#Create
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('createorder/', CreateorderAPIView.as_view(), name='createorder'),

#DetailView
    path('plant/<int:object_id>/', DetailViewPlant.as_view(), name='plant'),
    path('accessories/<int:object_id>/', DetailViewAccessories.as_view(), name='accessories'),
   



]
