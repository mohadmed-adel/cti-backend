import datetime
from rest_framework import status

from rest_framework import generics, permissions
from .models import Category, Service, RequestedServices, Comment
from .serializers import (
    MainServiceSerializer,
    ServiceSerializer,
    UserSerializer,
    RequestedServicesSerializer,
    CommentSerializer,
)
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
)  # Add authentication for security
from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class MainServiceViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = MainServiceSerializer
    http_method_names = ["get"]

    def get(self, request, main_cate_id=None):

        if main_cate_id is not None:
            services = Service.objects.filter(category_id=main_cate_id)
            serializer = ServiceSerializer(
                services, many=True, context={"request": request}
            )
            return Response(serializer.data)
        else:
            return super().get(request)


# Create your views here.
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:

            refresh = RefreshToken.for_user(user)
            refresh.access_token.set_exp(365 * 100 * 24 * 60 * 60)  # 100 years
            # Return the tokens as a JSON response
            return JsonResponse(
                {
                    "refresh-token": str(refresh),
                    "access-token": str(refresh.access_token),
                    "code": 200,
                }
            )
        else:
            # If authentication fails, return an error response
            return JsonResponse({"error": "Invalid credentials", "code": 400})


class UserRetrieveView(APIView):

    permission_classes = [IsAuthenticated]  # Only allow authenticated users to access

    def get(self, request):
        user = request.user  # Get the currently authenticated user

        serializer = UserSerializer(user)
        return Response(serializer.data)


class RequestedServicesListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        requested_services = RequestedServices.objects.filter(user=user)
        serializer = RequestedServicesSerializer(
            requested_services, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):

        request.data["user"] = request.user.id
        serializer = RequestedServicesSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save(
                user=request.user
            )  # Pass the user directly to the serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestedComments(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, requested_services_id=None):
        if requested_services_id is not None:
            comments = Comment.objects.filter(
                requestedServices_id=requested_services_id
            )
            serializer = CommentSerializer(
                comments, many=True, context={"request": request}
            )
            return Response(serializer.data)
        else:
            return super().get(request)
    def post(self, request,requested_services_id):
        request.data["user"] = request.user.id
        request.data['requestedServices']=requested_services_id
        serializer = CommentSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    
