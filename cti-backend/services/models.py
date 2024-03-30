from django.db import models
from django.db.models import  ManyToManyField

from django.contrib.auth.models import Group  # Import both

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=20)
    description =models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to="images/",null=True, height_field=None, width_field=None, max_length=100,  )

    def __str__(self):
        return self.name



class Service (models.Model):
    name = models.CharField(max_length=20)
    description =models.CharField(max_length=100,null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING,  blank=True, null=True,)
    image = models.ImageField(upload_to="images/",null=True, height_field=None, width_field=None, max_length=100, )

    def __str__(self):
        return self.name
 

class User(AbstractUser):
    # Your custom fields and methods here
    phone=models.CharField(max_length=20)
    groups = ManyToManyField(Group, related_name="service_users")
    
    class Meta:
        db_table = 'custom_user'  # Use a unique db_table name for your custom User model

    # Override the groups field to specify a unique related_name attribute
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )

    # Override the user_permissions field to specify a unique related_name attribute
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
     )

    
