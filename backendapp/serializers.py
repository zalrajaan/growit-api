from rest_framework import serializers
from .models import Plant

class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['local_name', 'scientific_name', 'location', 'watering_frequency','fertilizing_frequency','date_created','description','color', 'img']
