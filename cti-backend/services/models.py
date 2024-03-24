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
    pass
