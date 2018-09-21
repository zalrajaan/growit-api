from rest_framework import serializers
from .models import Plant
from django.contrib.auth.models import User


class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['local_name', 'scientific_name', 'location', 'watering_frequency','fertilizing_frequency','date_created','description','description_short','color', 'img', 'quantity']

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data