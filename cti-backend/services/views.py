from rest_framework import generics, permissions
from .models import MainService, Service
from .serializers import MainServiceSerializer, ServiceSerializer
from rest_framework.response import Response
 


class MainServiceViewSet(generics.ListAPIView):
    queryset = MainService.objects.all()
    serializer_class = MainServiceSerializer
    http_method_names = ["get"]

    def get(self, request, main_service_id=None):
        if main_service_id is not None:
            services = Service.objects.filter(main_service_id=main_service_id)
            serializer = ServiceSerializer(services, many=True)
            return Response(serializer.data)
        else:
            return super().get(request)


 
