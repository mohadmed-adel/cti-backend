from django.db import models
from django.contrib.auth.models import User
class Maincategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="images/")
    main_category= models.ForeignKey( Maincategory, models.DO_NOTHING, blank=True, null=True,)
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey( Category, models.CASCADE, blank=True, null=True,)
    def __str__(self):
        return self.name


class RequestedServices(models.Model):
    service = models.ForeignKey(Service, models.CASCADE, blank=False, null=False)
    status = models.CharField(max_length=100, null=True, default="معلق")
    description = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=False)
    building_name = models.CharField(max_length=100, null=False)
    building_number = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    asset_number = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False)
    attachment=  models.ImageField(upload_to="images/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username + " " + self.service.name


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    requestedServices = models.ForeignKey(   RequestedServices, models.CASCADE, blank=False, null=False )
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False)
    def __str__(self):
        return self.comment
