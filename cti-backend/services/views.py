from rest_framework import generics, permissions
from .models import Category, Service
from .serializers import MainServiceSerializer, ServiceSerializer ,UserSerializer 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Add authentication for security
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
            serializer = ServiceSerializer(services, many=True)
            return Response(serializer.data)
        else:
            return super().get(request)


 

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate (username=username, password=password)
        if user is not None:
           
            refresh = RefreshToken.for_user(user)
            refresh.set_exp(timezone.now() + timedelta(days=36500))
            # Return the tokens as a JSON response
            return JsonResponse({
                'refresh-token': str(refresh),
                'access-token': str(refresh.access_token),
                'code': 200
            })
        else:
            # If authentication fails, return an error response
            return JsonResponse({'error': 'Invalid credentials','code': 400})

class UserRetrieveView(APIView):
    
    permission_classes = [IsAuthenticated]  # Only allow authenticated users to access

    def get(self, request):
        user = request.user  # Get the currently authenticated user
        print("user ",user)
        serializer = UserSerializer(user)
        return Response(serializer.data)