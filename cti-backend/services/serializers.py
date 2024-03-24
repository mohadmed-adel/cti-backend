from rest_framework import serializers
from .models import MainService,Service
 

class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainService
        fields = '__all__'
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
 