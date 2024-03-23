from rest_framework import serializers
from .models import MainService,Service
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainService
        fields = '__all__'
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token