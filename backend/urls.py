from django.contrib import admin
from django.urls import path
from backendapp.views import PlantsList, UserCreateAPIView, AccessoriesList,DetailViewPlant, DetailViewAccessories, CustomerOrder, CreateorderAPIView, ProfileCreateAPIView, ProfileUpdateView,CategoryList, ProfileDetailAPIView, TrackingHistoryCreateView, TrackingHistoryListView, TrackingHistoryUpdateView, privacy_policy
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
#Users
	path('login/', obtain_jwt_token, name='login'),
    path('admin/', admin.site.urls),
    path('profiles/create/', ProfileCreateAPIView.as_view(), name='api-profile-create'),
    path('profiles/update/<int:user_id>/', ProfileUpdateView.as_view(), name='api-profile-create'),
    path('profiles/detail/<int:user_id>/', ProfileDetailAPIView.as_view(), name='api-profile-detail'),
#ListView
    path('plantslist/', PlantsList.as_view(), name='plantslist'),
    path('accessorieslist/', AccessoriesList.as_view(), name='accessorieslist'),
    path('order/<int:user_id>/', CustomerOrder.as_view(), name='order'),
    path('categorieslist/', CategoryList.as_view(), name='categorieslist'),

#Create
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('createorder/', CreateorderAPIView.as_view(), name='createorder'),

#DetailView
    path('plant/<int:object_id>/', DetailViewPlant.as_view(), name='plant'),
    path('accessories/<int:object_id>/', DetailViewAccessories.as_view(), name='accessories'),

#TrackingHistory
    path('track/', TrackingHistoryCreateView.as_view(), name='track'),
    path('tracklist/<int:user_id>', TrackingHistoryListView.as_view(), name='tracklist'),
    path('trackupdate/<int:id>/', TrackingHistoryUpdateView.as_view(), name='trackupdate'),

#HTMLPage
    path('privacypolicy/', privacy_policy, name='privacypolicy'),




]
