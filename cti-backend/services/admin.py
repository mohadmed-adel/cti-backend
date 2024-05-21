from django.contrib import admin
from .models import Category,Service,RequestedServices,Comment,Maincategory,Status
from django.contrib.auth.models import Group

# Define an inline admin descriptor for Comment model
# which acts a bit like a singleton
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
     

class RequestedServicesAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # If user is superuser or in admin group, return unfiltered queryset
        if request.user.is_superuser or request.user.groups.filter(name='admin').exists():
            return queryset

        # Define group-category mapping
        group_main_category_map = {
            'IT Group': 2,
            'non-IT Group': 1,
            'Electricity Group': 3
        }

        # Filter queryset based on user's group membership
        for group_name, main_category in group_main_category_map.items():
            try:
                group = Group.objects.get(name=group_name)
                if group in request.user.groups.all():
                    return queryset.filter(service__category__main_category=main_category)
            except Group.DoesNotExist:
                pass

        # If user doesn't belong to any mapped group, return an empty queryset
        return queryset.none()

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'requestedServices', 'user')
    search_fields = ('comment', 'requestedServices__id', 'user__username')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        # If user is superuser or in admin group, return unfiltered queryset
        if user.is_superuser or user.groups.filter(name='admin').exists():
            return queryset

        # Define group-category mapping
        group_main_category_map = {
            'IT Group': 2,
            'non-IT Group': 1,
            'Electricity Group': 3
        }

        # Collect requestedServices accessible by the user
        accessible_requested_services_ids = []

        for group_name, main_category in group_main_category_map.items():
            try:
                group = Group.objects.get(name=group_name)
                if group in user.groups.all():
                    accessible_requested_services = RequestedServices.objects.filter(service__category__main_category=main_category)
                    accessible_requested_services_ids.extend(accessible_requested_services.values_list('id', flat=True))
            except Group.DoesNotExist:
                pass

        # Filter comments based on accessible requestedServices
        return queryset.filter(requestedServices__id__in=accessible_requested_services_ids)


 

admin.site.register(Maincategory)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(RequestedServices,RequestedServicesAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Status)