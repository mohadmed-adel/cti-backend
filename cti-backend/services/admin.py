from django.contrib import admin
from .models import Category,Service,RequestedServices,Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(RequestedServices)
admin.site.register(Comment)