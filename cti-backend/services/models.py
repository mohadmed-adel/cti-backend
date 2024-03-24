from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MainService (models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name



class Service (models.Model):
    name = models.CharField(max_length=20)
    description =models.CharField(max_length=100)
    main_service = models.ForeignKey(MainService, models.DO_NOTHING,  blank=True, null=True,)
    def __str__(self):
        return self.name
 

class User(AbstractUser):
    # Your custom fields and methods here
    phone=models.CharField(max_length=20)

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

    
