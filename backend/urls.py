from django.contrib import admin
from django.urls import path
from backendapp.views import PlantsList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantslist/', PlantsList.as_view(), name='plantslist'),

]
