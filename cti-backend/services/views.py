from rest_framework import generics, permissions
from .models import Category, Service
from .serializers import MainServiceSerializer, ServiceSerializer
from rest_framework.response import Response
 


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


 
