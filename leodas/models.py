from django.db import models

# Create your models here.
class leodas(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    