from django.contrib import admin
from django.urls import path
from backendapp.views import PlantsList, UserCreateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantslist/', PlantsList.as_view(), name='plantslist'),
    path('register/', UserCreateAPIView.as_view(), name='register'),


]
