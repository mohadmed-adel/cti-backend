from rest_framework import serializers
from .models import Category, Service, RequestedServices,Comment
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


def get_full_image_url(request, image_url):
    current_site = get_current_site(request)
    return f"{request.scheme}://{current_site.domain}{image_url}"


class MainServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = [
            "id",
            "comment",
            "requestedServices",
            "user",
        ]  # Include 'user' field
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
        ]


class RequestedServicesSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(required=False)  # Make the field not required
    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RequestedServices
        fields = [
            "id",
            "status",
            "service",
            "service_id",
            "description",
            "location",
            "building_name",
            "building_number",
            "asset_number",
            "created_at",
            "user",
            "attachment",
        ]  
    
    def create(self, validated_data):
        service_id = validated_data.pop("service_id")
        validated_data["user"] = self.context["request"].user
        service = Service.objects.get(pk=service_id)
        validated_data["service"] = service
        return super().create(validated_data)
    
class RequestedServicesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedServices
        fields = ('id', 'attachment')