from rest_framework import serializers
from .models import Category,Service
 

class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
 