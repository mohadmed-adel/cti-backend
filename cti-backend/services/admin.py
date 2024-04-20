from django.contrib import admin
from .models import Category,Service,RequestedServices,Comment

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(RequestedServices)
admin.site.register(Comment)