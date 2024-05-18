from django.contrib import admin
from .models import Category,Service,RequestedServices,Comment,Maincategory
from django.contrib.auth.models import Group


class RequestedServicesAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Get the original queryset
        queryset = super().get_queryset(request)
        
        # Check if the user is an admin
        if request.user.is_superuser or request.user.groups.filter(name='admin').exists():
            return queryset  # Return the original queryset without any filtering
        
        # Check if the user belongs to IT Group
        it_group = Group.objects.get(id=1)
        non_it_group = Group.objects.get(id=2)
        electricity_group = Group.objects.get(id=3)
        if it_group in request.user.groups.all():
            # Filter queryset based on MainCategory for IT Group
            main_category = 2
            if main_category:
                # Filter RequestedServices based on related MainCategory
                queryset = queryset.filter(service__category__main_category=main_category)
        elif non_it_group in request.user.groups.all():
            # Filter queryset based on MainCategory for non-IT Group
            main_category = 1
            if main_category:
                # Filter RequestedServices based on related MainCategory
                queryset = queryset.filter(service__category__main_category=main_category)
        elif electricity_group in request.user.groups.all():
            # Filter queryset based on MainCategory for non-IT Group
            main_category = 3
            if main_category:
                # Filter RequestedServices based on related MainCategory
                queryset = queryset.filter(service__category__main_category=main_category)

        return queryset
        

admin.site.register(Maincategory)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(RequestedServices,RequestedServicesAdmin)
admin.site.register(Comment)