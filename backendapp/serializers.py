from rest_framework import serializers
from .models import Plant, Accessory, Product,Category, Stage, PlantCycle, Order, ProductItem
from django.contrib.auth.models import User


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

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data
