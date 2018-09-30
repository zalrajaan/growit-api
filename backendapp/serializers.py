from rest_framework import serializers
from .models import Plant, Accessory, Product,Category, Stage, PlantCycle, Order, ProductItem, Profile
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class ProfilDetailSerializer(serializers.ModelSerializer):
    user = UsersListSerializer()
    class Meta:
        model = Profile
        fields = '__all__'


class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        # fields = ['id','local_name', 'scientific_name', 'location', 'watering_frequency','fertilizing_frequency','date_created','description','description_short','color', 'img', 'quantity']
        fields = '__all__'
        # exclude = []

class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class Product_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'

class Plant_cycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCycle
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email','token']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER 
        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token
        return validated_data
